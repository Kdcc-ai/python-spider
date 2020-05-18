import requests
url="http://m.ip138.com/ip.asp?ip="
path=url+"202.204.80.112"
try:
      p=requests.get(path)
      p.raise_for_status()
      p.encoding=p.apparent_encoding
      print(p.text[-500:])
except:
    print("爬取失败")
    #收获:一些查询界面的网站 比如有文本框的 需要点击按钮的
    #在正式向后台提交时候 通常以链接形式提交
    # 只要我们知道提交时链接的地址 就可以挖掘一下 这个网站后台的API是什么