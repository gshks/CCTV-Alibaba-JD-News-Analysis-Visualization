import pandas as pd

# 指定 CSV 文件路径
csv_file_path = "D:\pycharm\pycharmAPP\project\数据可视化大作业\结果数据_阿里巴巴（2）.csv"

# 指定要保存的 txt 文件路径
output_txt_path = 'D:/pycharm/pycharmAPP/project/数据可视化大作业/标题汇总.txt'

# 使用 pandas 读取 CSV 文件
data = pd.read_csv(csv_file_path)

# 假设标题列名为"标题"
# 如果标题列名不是"标题"，请相应地修改下面的代码
titles = data['标题'].dropna().tolist()

# 将所有标题合并成一个长字符串，并用换行符分隔
text = '\n'.join(titles)

# 将标题保存到 txt 文件
with open(output_txt_path, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"标题已保存到: {output_txt_path}")
