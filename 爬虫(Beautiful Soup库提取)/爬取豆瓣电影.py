import requests
from bs4 import BeautifulSoup
import json
class DouBan(object):
    def __init__(self):
        self.baseurl='https://movie.douban.com/top250?start='
        self.headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
        self.result_list=[]
    # 爬取页面
    def start_request(self,url):
        try:
            p = requests.get(url,headers=self.headers)
            p.raise_for_status()
            p.encoding = p.apparent_encoding
            return p.text
        except:
            print("爬取失败")
    # 页面解析
    def parse(self,text):
        soup=BeautifulSoup(text,'html.parser')
        result_list=soup.find_all('div',attrs={'class':'item'})
        for movie in result_list:
            mydict={}
            mydict['title']=movie.find('span',attrs={'class':'title'}).text
            mydict['score']=movie.find('span',attrs={'class','rating_num'}).text
            quote=movie.find('span',attrs={'class','inq'})
            mydict['quote']=quote.text if quote else None
            star=movie.find('div',attrs={'class','star'})
            mydict['comment_num']=star.find_all('span')[-1].text
            self.result_list.append(mydict)
    def write_json(self,result):
         s=json.dumps(result,indent=4,ensure_ascii=False)
         with open('movies.json','w',encoding='utf-8') as f:
             f.write(s)
    # 开始爬取函数
    def start(self):
        for n in range(0,250,25):
          text=self.start_request(self.baseurl+str(n)+'&filter=')
          self.parse(text)
        self.write_json(self.result_list)
Spider=DouBan()
Spider.start()