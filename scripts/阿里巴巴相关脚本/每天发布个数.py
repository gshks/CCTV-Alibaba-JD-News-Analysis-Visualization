import pandas as pd

# 指定 CSV 文件路径，使用原始字符串（在路径前加 r）来避免反斜杠的转义问题
filepath = "D:\pycharm\pycharmAPP\project\数据可视化大作业\结果数据_阿里巴巴（2）.csv"

# 使用 pandas 读取 CSV 文件
data = pd.read_csv(filepath)
data['日期'] = pd.to_datetime(data['日期'])

# 接下来，我们将按日期分组并计算每个组的文章数量。
daily_news_counts = data.groupby(data['日期'].dt.date).size()

# 将结果转换为 DataFrame 以便查看和保存
daily_news_counts_df = daily_news_counts.reset_index()
daily_news_counts_df.columns = ['日期', '新闻个数']

# 显示结果
print(daily_news_counts_df)

# 将统计结果保存为 CSV 文件，同样使用原始字符串来指定路径
output_csv_path = r'D:\pycharm\pycharmAPP\project\数据可视化大作业\daily_news_counts.csv'
daily_news_counts_df.to_csv(output_csv_path, index=False)

print(output_csv_path)
