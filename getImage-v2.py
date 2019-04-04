# -*- coding: utf-8 -*-
import requests
import urllib2
import os
from bs4 import BeautifulSoup
import time
 
url  = 'http://soso.nipic.com/q_%E8%A2%81%E7%AB%8B_g_0.html'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)  # 使用headers避免访问受限
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.find_all('a')
folder_path = './photo/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)  # 创建文件夹
 
for index,item in enumerate(items):
    #print (item.get('href'))
    #print ('-----------------------')
    if item and item.get('class') == [u'search-works-thumb', u'relative']:        
        picPageLink = item.get('href')   # get函数获取图片链接地址，requests发送访问请求
        print (picPageLink)
        f = urllib2.urlopen(urllib2.Request(picPageLink)).read()
        
        soup = BeautifulSoup(f, 'html.parser')
        items = soup.find_all('img')

        for j,item in enumerate(items):
            if item and item.get('class') == [u'works-img']:
                img = requests.get(item.get('src'))   # get函数获取图片链接地址，requests发送访问请求
                img_name = folder_path + str(index + 1) +'.jpg'
                with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
                    file.write(img.content)
                    file.flush()
                file.close()  # 关闭文件
                print('第%d张图片下载完成' %(index+1))
                time.sleep(1)  # 自定义延时
                break

