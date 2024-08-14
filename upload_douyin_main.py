def run():
    # 读取 Excel 文件
    excel_file = 'your_excel_file.xlsx'  # 替换为你的 Excel 文件路径
    df = pd.read_excel(excel_file)

    # 遍历 Excel 中的行
    for index, row in df.iterrows():
        cookie_name = row['cookie名']  # 假设第一列为 "cookie名"
        video_title = row['标题']       # 假设第二列为 "标题"
        video_desc_and_tags = row['视频描述和话题']  # 假设第三列为 "视频描述和话题"
        video_path = row['文件地址']    # 假设第四列为 "文件地址"

        # 查找对应的 cookie 文件
        cookie_path = f"cookie/{cookie_name}.json"
        if not os.path.exists(cookie_path):
            print(f"未找到 cookie 文件: {cookie_path}")
            continue

        print(f"正在使用[{cookie_name}]发布作品")
        print(f"视频标题：{video_title}")
        print(f"视频路径：{video_path}")