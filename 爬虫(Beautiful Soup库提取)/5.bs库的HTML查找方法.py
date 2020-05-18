# 只详细讲了find_all方法 还有其他七种方法
# 使用中理解好find_all方法 其他七种方法很好使用了

from bs4 import BeautifulSoup
import requests
import re
# find_all函数参数 name attrs(对标签属性值的检索字符串) recurisive(是否对从该soup开始所有节点信息进行搜索 默认True False的话就搜儿子节点)
#                  string(对标签中字符串域进行检索) **kwargs
r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
# 返回一个列表类型 返回这个标签的列表
print(soup.find_all('a'))

# 我们要查找a标签和b标签呢？？以一个列表形式给入
print(soup.find_all(['a','b']))

for i in soup.find_all(re.compile('b')):
    print(i)


print(soup.find_all('p','course'))
# 对属性做相关的约定 查找属性域id属性-link1作为查找标签
print(soup.find_all(id='link1'))
print(soup.find_all(id='link'))
print(soup.find_all(re.compile('link')))
# 使用正则表达式作为搜索词的一部分

print(soup.find_all(string='Basic Python'))
print(soup.find_all(re.compile('python')))

