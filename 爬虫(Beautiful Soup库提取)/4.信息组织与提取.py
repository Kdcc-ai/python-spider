# 信息的标记
# 对信息进行标记来进行识别 用于通信存储和展示
# 有利于程序的理解和运用

# HTML通过预定义的标签形式组织不同类型的信息！！

# 将超文本信息 嵌入！ 到文本中


# 信息标记的种类

# ①XML和HTML接近 通过标签名字来表示信息的信息
# 形式 <name>...</name> <name/> <!-- -->

# ②JSON JS中对于面向对象信息的一种表达形式
#      有类型的键值对 key:value
# 形式 “name”:武汉理工大学
#      “name”：["武汉理工大学",“北京理工大学”]
#      “name”：{
#              "newName": "北京理工大学",
#               "oldname":"延安自然科学院"
#               }键值对的嵌套调用
#编写时候可以用JSON格式直接写

# ③YAML 无类型的键值对
# 利用缩进表示所属关系 用-号表达并列关系(用到时候看就行)
# 世界上所有信息  都可以用这种类型的信息来进行组织和标记
# 发挥更大的作用！


# 例子 已拍
# 小tips 已拍


# 介绍信息提取(！！从信息标记中取出想要的信息内容！！)方法
# 方法一：先完整解析信息的标记形式 再提取关键信息
# 得使用标记解析器 如:bs4库的标签树遍历
# 信息提取准确 但繁琐

# 方法二:无视标记形式 直接搜索关键信息
# 对信息的文本查找函数
# 信息提取块 但可能信息提取不正确

# 真正使用时 融合使用
# 实例:提取HTML中所有URL链接:
# 思路 搜索所有的<a>标签 解析<a>标签格式提取href后的链接内容
from bs4 import BeautifulSoup
import requests
r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup2=BeautifulSoup(demo,"html.parser")
soup=BeautifulSoup(demo,'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))