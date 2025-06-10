# _*_ coding: utf-8 _*_
import requests
import re
import csv
from datetime import datetime

csv_file_path = '结果数据.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['企业', '标题', '日期', '来源', '链接'])

def cctv(company, page):
    num = page

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
    url = 'https://search.cctv.com/search.php?qtext=' + company + '&sort=date&type=web&vtime=&page=' + str(num)
    print('正在获取----------------》》》', url)
    res = requests.get(url, headers=headers, timeout=10).text

    p_href = '<span lanmu1=".*?"'
    p_title = 'target="_blank">.*?</a>'
    p_source = '<div class="src-tim">.*?<span class="src">(.*?)</span>'
    p_date = '<div class="src-tim">.*?<span class="tim">(.*?)</span>'
    href = re.findall(p_href, res, re.S)
    title = re.findall(p_title, res, re.S)
    for i in range(20):
        title.remove('target="_blank"></a>')
    source = re.findall(p_source, res, re.S)
    date = re.findall(p_date, res, re.S)

    for i in range(len(title)):
        title[i] = title[i].strip().replace('target="_blank">', '')
        title[i] = title[i].strip().replace('</a>', '')
        href[i] = href[i].strip().replace('<span lanmu1="', '')
        href[i] = href[i].strip().replace('"', '')
        source[i] = source[i].strip()
        date[i] = date[i].strip()

    with open(csv_file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for i in range(len(title)):
            writer.writerow([company, title[i], date[i], source[i], href[i]])

    print(company + '第' + str(num) + '页信息爬取成功并写入CSV文件!')

companys = ['阿里巴巴', '京东', '万科集团', '腾讯', '小米', '新东方']
for company in companys:
    for i in range(10):
        try:
            cctv(company, i + 1)
        except Exception as e:
            print(company + '第' + str(i + 1) + '页信息爬取失败!', e)
