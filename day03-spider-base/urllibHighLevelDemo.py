#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
urllib模块的高级用法,主要是cookies,登陆验证,代理设置等等
@author:huldar
@file: urllibHighLevelDemo.py
@time: 2018/12/21
"""
# handler的继承结构
import http.cookiejar
import urllib
from urllib.error import URLError
from urllib.parse import urlparse, urlunparse, urlsplit

from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener, ProxyHandler

'''
/--BaseHandler
    |
    |---HTTPDefaultErrorHandler:处理HTTP响应错误,错误都会抛出HTTPError类型的异常
    |
    |---HTTPRedirectHandler:处理重定向
    |
    |---HTTPCookieProcessor:用于处理cookie
    |
    |---ProxyHandler:用于处理代理,默认代理为空
    |
    |---HTTPPasswordMgr:用于管理密码,它维护了用户名和密码表
    |
    |---HTTPBasicAuthorHandler:用于管理认证,如果一个连接打开时需要认证,那么可以用他来解决认证问题
还有其他的Handler,参见官网
'''
# 示例登陆验证

# 验证
userName = 'root'
password = 'root'

url = 'http://localhost:5000/'

realm = HTTPPasswordMgrWithDefaultRealm()
realm.add_password(None, url, userName, password)

auth_handler = HTTPBasicAuthHandler(realm)
auth_opener = build_opener(auth_handler)

try:
    result = auth_opener.open(url)
    result_html = result.read().decode('utf-8')
    print(result_html)
except URLError as e:
    print(e.reason)

# 代理

proxy_handler = ProxyHandler({'http': 'http://127.0.0.1:9743', 'https': 'https://127.0.0.1:9743'})

opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

cookie = http.cookiejar.CookieJar()
http_cookie_processor = urllib.request.HTTPCookieProcessor(cookiejar=cookie)
request_build_opener = urllib.request.build_opener(http_cookie_processor)
response = request_build_opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + '=' + item.value)
# 生成cookie的文件

fileName = 'cookies_LWP.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename=fileName)
cookie = http.cookiejar.LWPCookieJar(filename=fileName)
cookie_handler = urllib.request.HTTPCookieProcessor(cookiejar=cookie)
opener = urllib.request.build_opener(cookie_handler)
cookieFileResponse = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
# Opener
'''
openerDirector类
'''
# 从文件中读取cookie(以LWP格式的为例)
lwp_cookie = http.cookiejar.LWPCookieJar()
lwp_cookie.load(filename=fileName, ignore_expires=True, ignore_discard=True)

load_cookie_handler = urllib.request.HTTPCookieProcessor(lwp_cookie)

load_cookie_opener = urllib.request.build_opener(load_cookie_handler)
load_cookie_response = load_cookie_opener.open('http://www.baidu.com')
print(load_cookie_response.read().decode('utf-8'))
# -------------------华丽的分割线(异常处理)---------------------------
"""
urllib的error模块定义了由request模块产生的异常
|--OSError
     |
     |---URLError:由request模块产生的异常都能使用该异常捕捉
            |
            |--HTTPError:处理HTTP请求错误,比如认证请求失败错误(属性code,reason,headers)
"""
# 解析链接
url_parse = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(url_parse), url_parse)
# http://www.baidu.com/index.html;user?id=5#comment
# ----   ------------- ---------- --- - -----------
# shceme       netloc      path    params  query#frament
# urlparse('url',scheme,allow_fragments)
'''
url:必填
scheme:默认'',并且档url中不包含scheme时候,scheme=''才会生效
allow_fragments:是否忽略fragment
'''
# urlunparse()
url_data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
urlunparse_result = urlunparse(url_data)
print(urlunparse_result)  # http://www.baidu.com/index.html;user?a=6#comment

# urlsplit()
urlsplit_result = urlsplit('http://www.baidu.com/index.html;user?a=6#comment')
print(urlsplit_result)
# SplitResult(scheme='http', netloc='www.baidu.com', path='/index.html;user', query='a=6', fragment='comment')

# urlunsplit 和urlsplit想法

# urljoin
"""
base_url中提供了三项内容 scheme netloc path,
    如果这个3项在新的链接中不存在,就予以补充;
    如果存在则使用新的链接的部分
"""
# urlecode 构建请求的参数 特别是在GET请求中特别常用
# parse_qs()方法 是反序列化,将GET请求中的参数转回字典
# parse_qsl()转回元组


# url编码 url解码
"""
quote() 将内容转化为URL编码的格式 处理URL中的中文乱码问题
unquote() 将URL编码的信息进行解码
"""

# rebotparse解析robot.txt 获取哪些路径可以爬取
