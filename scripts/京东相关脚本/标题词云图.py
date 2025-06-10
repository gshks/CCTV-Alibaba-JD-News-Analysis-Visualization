import jieba
from collections import Counter
from pyecharts import options as opts
from pyecharts.charts import WordCloud

with open("D:\pycharm\pycharmAPP\project\数据可视化大作业\京东\标题汇总.txt", "r", encoding="utf-8") as f:
    text = f.read()
words = jieba.lcut(text)
with open("D:\数据可视化\实验八\cn_stopwords.txt", "r", encoding="utf-8") as f:
    text1 = f.read()
stopwords = (text1)
word_freq = {}
for word in words:
    if word not in stopwords:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1

word_counts = Counter(words)
wordcloud=(
       WordCloud(init_opts=opts.InitOpts(width="1000px", height="600px"))
       .add("词频", [(word, freq) for word, freq in word_freq.items()])
       .set_global_opts(
           title_opts=opts.TitleOpts(title="京东标题词云图",pos_left="center",  # 标题居中
            pos_top="top" )  # 添加标题和副标题
       )
       .render("D:\pycharm\pycharmAPP\project\数据可视化大作业\京东\标题词云图.html")

         )
