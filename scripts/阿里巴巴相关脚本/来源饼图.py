from pyecharts.charts import Pie
from pyecharts import options as opts
import csv

file_name = r"D:\pycharm\pycharmAPP\project\数据可视化大作业\source_counts.csv"
data_x = []
with open(file_name, encoding='utf-8') as f:  # 添加 encoding='utf-8'
    reader = csv.reader(f)
    for data_row in reader:
        data_x.append(data_row)

A = []
B = []
for index, values in enumerate(data_x):
    if index > 0:
        A.append(values[0])
        B.append(int(values[1]))  # 确保 B 中的值是整数

(
    Pie()
    .set_global_opts(title_opts=opts.TitleOpts(title="央视新闻中阿里巴巴相关来源分布情况"),
                     legend_opts=opts.LegendOpts(pos_left='right',orient='vertical'),
                     )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    .add("", [list(z) for z in zip(A, B)])
    .render("D:\pycharm\pycharmAPP\project\数据可视化大作业\央视新闻中阿里巴巴相关来源分布情况.html")
)
