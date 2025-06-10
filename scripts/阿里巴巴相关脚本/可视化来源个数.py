import pandas as pd

# 指定 CSV 文件路径
filepath = "D:\pycharm\pycharmAPP\project\数据可视化大作业\结果数据_阿里巴巴（2）.csv"

# 使用 pandas 读取 CSV 文件
data = pd.read_csv(filepath)

# 统计 '来源' 列中每个唯一值的数量
source_counts = data['来源'].value_counts()


# 将结果另存为另一个csv文件
output_path =r'D:\pycharm\pycharmAPP\project\数据可视化大作业\source_counts.csv'
source_counts.to_csv(output_path)
