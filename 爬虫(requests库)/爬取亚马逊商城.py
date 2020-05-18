# import requests
# r=requests.get("https://www.amazon.cn/dp/B00C8FVZZY")
# print(r.status_code)
# # 没访问到
# r.encoding=r.apparent_encoding
# print(r.request.headers)
#
# newuser={'user-agent':'Mozilla/5.0'}
# r=requests.get("https://www.amazon.cn/dp/B00C8FVZZY",headers=newuser)
# print(r.status_code)
# # 改变headers字段

#整个代码
import requests
url="https://www.amazon.cn/dp/B00C8FVZZY"
try:
    kv={"user-agent":"Mozilla/5.0"}
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")
# 收获:对来源进行了审查  所以我们利用requests库来改变uset-agent