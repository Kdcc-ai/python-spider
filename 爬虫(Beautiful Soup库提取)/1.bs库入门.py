# 解析HTML页面 信息标记与信息提取
import requests
r=requests.get("http://python123.io/ws/demo.html")
print(r.text)
demo=r.text
from bs4 import BeautifulSoup
# 一个参数是HTML格式的信息 一个是解释器html.parser
soup=BeautifulSoup(demo,"html.parser")
print(soup.title)
# 页面的title 页面左上方显示的内容

print(soup.a)
# 链接标签
# 有相同标签 只返回第一个
print(soup.a.name)
# 标签的名字
print(soup.a.attrs)
# 返回一个字典 标签名字 属性名字和属性的值之间的对应关系
print(soup.a.attrs["href"])
# 字典查找
print(type(soup.a.attrs))
# 属性是个字典
print(type(soup.a))
# bs库定义的一个标签类
print(soup.a.string)

print(soup.p)
print(soup.p.string)
print(type(soup.p.string))
# bs库定义的一个可以包含其他标签的标签类

soup2=BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>",
                    "html.parser")
# HTML页面中用<!表示注释开始
print(soup2.b.string)
# This is a comment
print(type(soup2.b.string))
# 输出 <class 'bs4.element.Comment'>
# 说明是文本标签
print(soup2.p.string)
print(type(soup2.p.string))
# 输出<class 'bs4.element.NavigableString'>


# print(soup.prettify())
# 返回解析后的HTML


# 收获:理解 其实HTML源代码就是一个标签树
#          这个库其实功能就是解析这些标签的(可以认为bs对象<==>对应的HTML界面)
#          只要是标签类型的文件 都可以解析
#          并且标签树有三种遍历方式 已拍

# 讲解一下标签
# 如何理解BeautifulSoup解析器？已拍

