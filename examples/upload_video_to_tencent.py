import asyncio
from pathlib import Path

from conf import BASE_DIR
from uploader.tencent_uploader.main import weixin_setup, TencentVideo
from utils.constant import TencentZoneTypes
from utils.files_times import generate_schedule_time_next_day, get_title_and_hashtags
import os
import pandas as pd
import asyncio

if __name__ == '__main__':

    excel_file = 'your_excel_file-today.xlsx'
    df = pd.read_excel(excel_file)

    for index, row in df.iterrows():
        cookie_name = row['cookie名']
        video_title = row['标题']
        video_desc_and_tags = row['视频描述和话题']
        filepath = row['文件地址']
        account_file = f"cookie/{cookie_name}.json"
        publish_date = row['发布时间']

        if not os.path.exists(account_file):
            print(f"未找到 cookie 文件: {account_file}")
            continue

    # 获取视频目录
    folder_path = Path(filepath)
    # 获取文件夹中的所有文件
    files = list(folder_path.glob("*.mp4"))
    file_num = len(files)
    publish_datetimes = generate_schedule_time_next_day(file_num, 1, daily_times=[16])
    cookie_setup = asyncio.run(weixin_setup(account_file, handle=True))
    category = TencentZoneTypes.LIFESTYLE.value  # 标记原创需要否则不需要传
    for index, file in enumerate(files):
        title, tags = get_title_and_hashtags(str(file))
        # 打印视频文件名、标题和 hashtag
        print(f"视频文件名：{file}")
        print(f"标题：{title}")
        print(f"Hashtag：{tags}")
        app = TencentVideo(title, file, tags, publish_datetimes[index], account_file, category)
        asyncio.run(app.main(), debug=False)
