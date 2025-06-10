import pandas as pd
import numpy as np
df = pd.read_csv("D:\pycharm\pycharmAPP\project\数据可视化大作业\结果数据_京东.csv")
##查看数据
#df.info()
#查看数据表的大小，返回数据表的行、列数
#d = df.shape[0] #打印行数和列数
#w = df.shape[1]
#print("数据的行数%d "%d)
#print('数据的列数 %d'%w)

#数据格式的查看
#df.describe()
#q缺失值处理
#print(df.isnull())#查找缺失值
#print(df.isnull().sum())#各列缺失值的数量

df1=df.dropna(how='all',axis=0)#行全为None的时候删除
df2=df.dropna(how='all',axis=1)#列全为None时删除
df3=df.dropna(how='any',axis=0)#不是全为None
df4=df.dropna(how='any',axis=1)#不是全为None

#重复值处理
#result=df.duplicated()
#print(result)
来源= '来源'
日期='日期'
标题='标题'
# 删除特定列中的特定字
df[来源] = df[来源].apply(lambda x: x.replace('来源：', '') if pd.notnull(x) else x)
df[日期] = df[日期].apply(lambda x: x.replace('发布时间：', '') if pd.notnull(x) else x)

# 保存修改后的DataFrame到CSV文件
#df.to_csv('结果数据_阿里巴巴（1）.csv', index=False)

##异常值的检测与处理

df['标题']=df['标题'].str.strip()
df['日期']=df['日期'].str.strip()
df['来源']=df['来源'].str.strip()#去除多余空格


##特征提取
df['length'] = df['标题'].str.len()
print(df['length'])
df.to_csv('结果数据_京东（2）.csv', index=False)