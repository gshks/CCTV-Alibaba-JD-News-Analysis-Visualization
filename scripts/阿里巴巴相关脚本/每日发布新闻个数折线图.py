from pyecharts.charts import Line
import pandas as pd

file = pd.read_csv("D:\pycharm\pycharmAPP\project\数据可视化大作业\daily_news_counts.csv")

line = Line()

X=file['日期'].astype(str).tolist()
Y=file['新闻个数'].tolist()

line.add_xaxis(xaxis_data=X)
line.add_yaxis('每日相关阿里巴巴新闻个数变化折线图',Y)


line.render("D:\pycharm\pycharmAPP\project\数据可视化大作业\Line.html")