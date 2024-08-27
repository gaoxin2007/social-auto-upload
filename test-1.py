import pandas as pd
import asyncio
from datetime import datetime
from uploader.douyin_uploader.main import douyin_setup, DouYinVideo

async def run():
    excel_file = 'your_excel_file.xlsx'
    df = pd.read_excel(excel_file)

    for index, row in df.iterrows():
        cookie_name = row['cookie名']
        video_title = row['标题']
        video_desc_and_tags = row['视频描述和话题']
        video_path = row['文件地址']
        cookie_path = f"cookie/{cookie_name}.json"
        publish_date = row['发布时间']

        print(publish_date)

if __name__ == '__main__':
    asyncio.run(run())