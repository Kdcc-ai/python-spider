# 使用prettify()方法
from bs4 import BeautifulSoup
import requests
# ！！！！！重要！！！！！！
r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup2=BeautifulSoup(demo,"html.parser")
print(soup2.prettify())
# 按HTML格式输出
print(soup2.a.prettify())