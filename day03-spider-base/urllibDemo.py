#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
学习使用urllib包,认识爬虫
@author:huldar
@file: urllibDemo.py
@time: 2018/12/21
"""

# urllib是Python内置的HTTP请求库
import socket

"""
urllib有4个模块:
    request:最基本的HTTP请求模块,可以用来模拟发送请求
    error:异常处理模块
    parse:工具模块,提供了许多URL处理方法,比如拆分/解析/合并等
    robotparser:识别网站的robots.txt文件
"""
# 模块练习--request
import urllib.request

# urlopen参数
"""
    url:访问的URL路径
    data=None: 附加数据,如果添加该参数,他需要被转码成bytes类型
    timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
    *
    cafile=None
    capath=None
    cadefault=False
    context=None
"""
response = urllib.request.urlopen("https://www.python.org")
# HTTPResponse是对URL请求结果的封装
"""
@:type HTTPResponse
    主要属性有:
        msg,version,status,reason,debuglevel,closed
    主要的方法有:
        read(),readinto(),getHeader(name),getHeaders(),fileno()
"""
# print(response.read().decode('utf-8')) #即可得到网页HTML数据,然后分析爬取
print(type(response))  # <class 'http.client.HTTPResponse'>
print(response.version)  # http版本
print(response.status)  # 响应状态码
print(response.reason)  # 响应状态词
print(response.debuglevel)
print(response.getheaders())
print(response.getheader('Server'))

# urlopen(url,data=None,[timeout,*],cafile=None,capath=None,cadefault=False,context=None)
"""
data参数示例
"""
import urllib.parse

requestData = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
postResponse = urllib.request.urlopen('http://httpbin.org/post', data=requestData)
print(postResponse.read())
# urllib.parse模块里的urlencode()方法来讲参数字典转化为字符串,第二个参数是指定字符编码

"""
timeout:请求连接超时时间,单位为秒.
"""
import urllib.error

try:
    timeoutResponse = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
"""
context:它必须是ssl.SSLContext,用来指定SSL设置
cafile:指定CA证书
capath:指定CA证书的路径
"""
# Request对象
request = urllib.request.Request('https://python.org')
requestObjectResponse = urllib.request.urlopen(request)
print(requestObjectResponse.read().decode('utf-8'))
# Request构造方法
"""
urllib.request.Request(url,data=None,headers={},origin_req_host=None,unverifiable=False,method=None)
参数解释:
    url:请求的URL,必传参数
    data:如果要传,必传bytes类型,如果是字典,可以先用urllib.parse模块中的urlencode()编码
    headers:请求头
        默认User-Agent是Python-urllib
    origin_req_host:请求方的host名称或者IP地址
    unverifiable:表示这个请求是否是无法验证的,默认是False,意思是说用户没有足够权限来选择接受这个请求的结果.
    method:请求方法
"""
http_bin_post_url = 'http://httpbin.org/post'
headers = {
    'Use-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Host': 'httpbin.org'
}
dataBody = {
    'name': 'huldar'
}

data = bytes(urllib.parse.urlencode(dataBody), encoding='utf8')
http_bin_request = urllib.request.Request(url=http_bin_post_url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(http_bin_request)

print(response.read().decode('utf-8'))

# Request类中有个add_header()方法来添加请求头
