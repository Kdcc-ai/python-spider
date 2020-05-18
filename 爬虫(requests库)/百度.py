# 搜索引擎关键字

# 向百度提交个关键词并获得搜索结果
# 百度其实有搜索关键词的接口
# 百度：http://www.baidu.com/s?wd=keyword
import  requests
kv={'wd':'Python'}
try:
   r=requests.get("http://www.baidu.com/s",params=kv)
   r.raise_for_status()
   print(r.status_code)
   print(len(r.text))
except:
    print("爬取失败")