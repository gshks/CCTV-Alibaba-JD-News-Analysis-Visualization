import pandas as pd
import numpy as np
df = pd.read_csv("D:\pycharm\pycharmAPP\project\数据可视化大作业\结果数据_阿里巴巴.csv")


df1=df.dropna(how='all',axis=0)
df2=df.dropna(how='all',axis=1)
df3=df.dropna(how='any',axis=0)
df4=df.dropna(how='any',axis=1)

#重复值处理
来源= '来源'
日期='日期'
标题='标题'
# 删除特定列中的特定字
df[来源] = df[来源].apply(lambda x: x.replace('来源：', '') if pd.notnull(x) else x)
df[日期] = df[日期].apply(lambda x: x.replace('发布时间：', '') if pd.notnull(x) else x)

##异常值的检测与处理

df['标题']=df['标题'].str.strip()
df['日期']=df['日期'].str.strip()
df['来源']=df['来源'].str.strip()#去除多余空格


##特征提取
df['length'] = df['标题'].str.len()
print(df['length'])
df.to_csv('结果数据_阿里巴巴（2）.csv', index=False)