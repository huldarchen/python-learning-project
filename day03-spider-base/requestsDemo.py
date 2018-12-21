#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
requests库的使用
@author:huldar
@file: requestsDemo.py
@time: 2018/12/21
"""
import re
import requests

# get(url, params=None, **kwargs):
requests_getBaidu = requests.get('https://www.baidu.com')
print(type(requests_getBaidu))
print(requests_getBaidu.status_code)
print(requests_getBaidu.text)
print(type(requests_getBaidu.text))
print(requests_getBaidu.cookies)

# 抓取网页
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
zhihu_url = 'https://www.zhihu.com/explore'
zhihu_response = requests.get(url=zhihu_url, headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)

titles = re.findall(pattern, zhihu_response.text)
print(titles)

# 抓取二进制数据
gitHub_response = requests.get('https://github.com/favicon.ico')
with open('favicon.ico', 'wb') as f:
    f.write(gitHub_response.content)
#使用get或POST等方法 两次方法相当于调用2次浏览器,不是同一个会话
#要想用同一个会话需要使用session