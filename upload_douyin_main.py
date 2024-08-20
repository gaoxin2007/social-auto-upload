import os

import pandas as pd
import asyncio
from datetime import datetime

from playwright.async_api import async_playwright

from uploader.douyin_uploader.main import douyin_setup, DouYinVideo

async def run():
    excel_file = 'your_excel_file-today.xlsx'
    df = pd.read_excel(excel_file)

    for index, row in df.iterrows():
        cookie_name = row['cookie名']
        video_title = row['标题']
        video_desc_and_tags = row['视频描述和话题']
        video_path = row['文件地址']
        cookie_path = f"cookie/{cookie_name}.json"
        publish_date = row['发布时间']

        if not os.path.exists(cookie_path):
            print(f"未找到 cookie 文件: {cookie_path}")
            continue


        # 创建 DouYinVideo 对象，并设置相关参数
        video = DouYinVideo(
            title=video_title,
            file_path=video_path,
            tags=video_desc_and_tags.split(","),
            publish_date=publish_date,
            account_file=cookie_path
        )

        async with async_playwright() as playwright:
            await video.upload(playwright)  # 将 playwright 对象传递给 upload 方法
            print(f"视频 {video_title} 上传成功")

if __name__ == '__main__':

    asyncio.run(run())