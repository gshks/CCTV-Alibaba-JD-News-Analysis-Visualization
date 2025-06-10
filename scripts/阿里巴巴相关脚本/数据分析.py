import pandas as pd

#标题情况
new_df = pd.read_csv('D:\pycharm\pycharmAPP\project\数据可视化大作业\结果数据_阿里巴巴（2）.csv')  # 如果需要，可以取消注释这行代码来加载CSV文件

# 描述性统计分析
length_stats = new_df['length'].describe()

# 打印描述性统计结果
print(length_stats)

#来源情况 百分比
# Distribution analysis for the '来源' column
source_distribution = new_df['来源'].value_counts(normalize=True) * 100

print(source_distribution)

