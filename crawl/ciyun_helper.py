# coding:utf8

import jieba  # jeiba分词
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS  # 词云库
import matplotlib.pyplot as plt  # 显示图像使用
import numpy as np
# from scipy.misc import imread  # 读取图像,PIL,CV,可替代
from imageio import  imread

text = open("shugou.txt", "r", encoding="utf-8").read()
seg_list = jieba.cut(text, cut_all=True)  # 全模式
text_deal = "/".join(seg_list)
bg_mask = imread("test.jpg")  # 幕布
wc = WordCloud(
    background_color="white",  # 背景白色
    mask=bg_mask,  # 幕布形状
    font_path="simhei.ttf",  # 字体一定要换,不然乱码
    max_font_size=80,  # 最大字体size
    max_words=2000,  # 多少字
    scale=2
).generate(text_deal)
plt.imshow(wc)
wc.to_file('output.png')

# from pathlib import Path
# from wordcloud import WordCloud
#
# # 读取文本内容
# current_directory = Path.cwd()
# text = Path.open(current_directory/"shugou.txt", "r", encoding="utf-8").read()
# bg_mask = imread(current_directory/"微信图片_20181219093910.jpg")
# # 创建词云实例对象
# wordcloud = WordCloud(
#     background_color="white",  # 背景白色
#     mask=bg_mask,  # 幕布形状
#     font_path="simhei.ttf",  # 字体一定要换,不然乱码
#     max_font_size=80,  # 最大字体size
#     max_words=2000,  # 多少字
#     scale=2
# )
#
# # 加载文本内容到词云对象中。
# wordcloud.generate(text)
#
# # 将图像以定义的图像文件名输出。
# wordcloud.to_file('output.png')
