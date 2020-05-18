import requests
url='https://item.jd.com/34301693617.html'
# 京东某物品内容
try:
    r=requests.get(url)
    # 返回的代码不是200 才会产生异常
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print('爬取失败')