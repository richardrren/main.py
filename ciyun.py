import os
import re
import cv2
import jieba
import requests
import moviepy
import pandas as pd
import numpy as np
from PIL import Image
from lxml import etree
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from fake_useragent import UserAgent

# -*- coding:utf-8 -*-
import cv2
cap = cv2.VideoCapture(r"立刻接受学姐对你说的LUV.flv")
num = 1
while 1:
    # 逐帧读取视频  按顺序保存到本地文件夹
    ret,frame = cap.read()
    if ret:
        cv2.imwrite(f".\pictures\img_{num}.jpg",frame)
    else:
        break
cap.release()   # 释放资源


# -*- coding:utf-8 -*-
import cv2
import base64
import numpy as np
import os
from aip import AipBodyAnalysis
import time
import random

APP_ID = '25308577'
API_KEY = 'YzjGGfsHP7gmFMWt4n0V9NsO'
SECRET_KEY = '8VQKlwfUcDCPcAXMANZiuOd1PNlZIuw3'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
# 保存图像分割后的路径
path = './mask_img/'

# os.listdir  列出保存到图片名称
img_files = os.listdir('./pictures')
print(img_files)
for num in range(1, len(img_files) + 1):
    # 按顺序构造出图片路径
    img = f'./pictures/img_{num}.jpg'
    img1 = cv2.imread(img)
    height, width, _ = img1.shape
    # print(height, width)
    # 二进制方式读取图片
    with open(img, 'rb') as fp:
        img_info = fp.read()

    # 设置只返回前景   也就是分割出来的人像
    seg_res = client.bodySeg(img_info)
    labelmap = base64.b64decode(seg_res['labelmap'])
    nparr = np.frombuffer(labelmap, np.uint8)
    labelimg = cv2.imdecode(nparr, 1)
    labelimg = cv2.resize(labelimg, (width, height), interpolation=cv2.INTER_NEAREST)
    new_img = np.where(labelimg == 1, 255, labelimg)
    mask_name = path + 'mask_{}.png'.format(num)
    # 保存分割出来的人像
    cv2.imwrite(mask_name, new_img)
    print(f'======== 第{num}张图像分割完成 ========')


# 绘制词云
import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
for num in range(1,23):
    with open("comment.txt", 'r') as f:
        job_title_1 = f.read()
    contents_cut_job_title = jieba.cut(job_title_1)
    contents_list_job_title = " ".join(contents_cut_job_title)
    img = f'mask_{num}.png'
    mask = 255 - np.array(Image.open(img))  # 相互转化
    wc = WordCloud(stopwords=STOPWORDS.add("一个"), collocations=False,
                   background_color="white",
                   font_path=r"K:\msyh.ttc",
                   width=400, height=300, random_state=42,
                   mask=mask
                   )
    wc.generate(contents_list_job_title)
    wc.to_file(f"ciyun_{num}.png")


# 合成视频

import cv2
video_address = 'tiaowu.mp4'   # 输出视频的保存路径
fps = 20  # 帧率，可以调整
img_size = (1080, 1920)  #  图片的大小
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
videoWriter = cv2.VideoWriter(video_address , fourcc, fps, img_size)
for num in range(1,23):
    img_path = f'ciyun_{num}.png'
    frame = cv2.resize(cv2.imread(img_path), img_size)
    videoWriter.write(frame)      # 合成视频
videoWriter.release()



