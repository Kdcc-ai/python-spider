# 北京理工大学

import requests
# 一.
# 故requests库提供的7个常用方法 除了一个基本方法外 其他的六方法就是调用request方法来实现的
# 其实只用了一个request方法

# 三个参数url 拟抓取页面的url链接
# params：url中的额外参数 字典或字节流格式 可选
# **kwargs：12个访问控制的参数
# 查文档get方法实际上使用了request方法来封装
r=requests.get("http://www.baidu.com")
# 检查请求状态码
print(r.status_code)
print(type(r))
# 返回这个类 类名是Reponse
print(r.headers)
# 得到get请求获得页面的头部信息


print(r.text)
print(r.encoding)
# 从HTTP Header中(charest字段)猜测的编码方式
# 如果服务器(对于资源编码的一种要求)字段中没有charest字段 则默认为ISO-8859-1编码
print(r.apparent_encoding)
# 从HTTP的内容部分分析文本中的内容编码方式 根据网页内容分析出的编码方法
r.encoding='utf-8'
print(r.text)


# 二. Http协议：已了解

# 三.requests库的方法:
# requests.request(method,url,**kwargs)
# method对应ruquests那七种方法
# url URL链接
# **kwargs是访问控制参数有13个 了解这13个 再记住request库另外6个方法和request方法的联系
# 可选参数！！基础重要啊
# params：字典或字节序列 作为参数增加到URL中 GET使用
kv={'key1':'value1','key2':'value2'}
r=requests.request('GET','http://python123.io/ws',params=kv)
print(r.url)

# data:字典字节序列或文件对象字符串也可 作为Request的内容 POST使用
# 不放在URL链接里面 而是请求向服务器提交资源时使用
kv2={'key1':'value1','key2':'value2'}
r=requests.request('POST','http://python123.io/ws',data=kv2)


# json数据 JSON格式的数据 作为Request的内容 POST使用
# 同样和上面一样可以用字典作为json语句的参数 那么这个字典就赋值到服务器的json语句上


# headers：字典,HTTP定制头 浏览器再想服务器发送请求时服务器看到的user-agent字段就是Chrome/10
# 模拟任何版本的浏览器发送请求
hd={'user-agent','Chrome/10'}
r=requests.request('POST','http://python123.io/ws',headers=hd)


# cookies:字典或Cookie
# Request中的cookie
# auth:元组 支持HTTP认证功能


# file：字典类型 传输文件
fs={'file':open('',"rb")}
r=requests.request('POST','http://python123.io/ws',files=fs)
# 对特定的链接提交文件


# timeout:设定超时时间 秒为单位
r=requests.request('GET','http://www.baidu.com',timeout=10)


# proxies:字典类型 设定访问代理服务器(代理网络用户去取得网络信息 网络信息的中转站) 可以增加登陆认证
pxs={'http':'http://user:pass@10.10.10.1:1234',
      'https':'https://10.10.10.1:4321'}
r=requests.request('GET','http://www.baidu.com',proxies=pxs)
# 可以隐藏原用户的IP地址


# 另外几个字段已将拍 高级功能 用到的时候再说



# requeset入门总结 基本用get()和head()方法








# ...网络爬虫的盗亦有道
# 网络爬虫的尺寸 小规模数据量小爬取速度不敏感 使用Requests库
#               中规模 爬取速度敏感 爬取系列网站
#               大规模,搜索引擎 爬取速度关键 用于定制开发 爬取全网

# 网络爬虫的限制 发布公告 告知所有爬虫网站的爬取策略
# Robots协议做到 网站告诉网络爬虫那些页面能访问 存储在网站根目录下的Robots.txt文件中
# 我们可以查看里面内容 已经讲过了
# 以后做网站的时候是不是可以对自己的网站做一个相关的规范 使得爬虫能访问哪里
# 网络爬虫可以遵循robots协议也可以不遵循






