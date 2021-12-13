import requests
import re
import bs4
import pandas as pd
import numpy as np
import string
import jieba
from PIL import Image


def get_data(cid):
    """分析网页，并获取网页文件"""
    url = 'https://comment.bilibili.com/457833738.xml'.format(cid)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }  # 注意格式为字典，不能有空格
    response = requests.get(url, headers=headers).content.decode('utf-8')  # 必须进行解码
    return response


def parse_html(response):
    """解读网页文件，提取关键信息"""
    # 法一：美丽汤
    soup = bs4.BeautifulSoup(response)
    lst = soup.findAll(name='d')
    danmuku = [i.text for i in soup.findAll(name='d')]  # 返回弹幕列表
    # 法二：正则表达式
    # pattern = re.compile('<d p=".*?">(.*?)</d>')
    # danmuku = re.findall(pattern, response)
    return danmuku


def save_data(danmuku):
    """将数据存储为CSV文件"""
    Dict = {
        'danmuku': danmuku
    }
    pd_data = pd.DataFrame(Dict)
    pd_data.to_csv('弹幕文件.csv', index=False, header=False, mode='w', encoding='utf-8-sig')
