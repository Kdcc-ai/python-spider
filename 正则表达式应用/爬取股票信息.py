# 已经爬不出来了  但是思路比较重要

# 获取HTML页面
import requests
from bs4 import BeautifulSoup
import re
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    # 找到所有的a标签
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
            print(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue


# def getStockInfo(lst, stockURL, fpath):
#     for stock in lst:
#         url = stockURL + stock + ".html"
#         html = getHTMLText(url)
#         try:
#             if html == "":
#                 continue
#             infoDict = {}
#             soup = BeautifulSoup(html, 'html.parser')
#             stockInfo = soup.find('div', attrs={'class': 'stock-bets'})
#             # 股票所存在的大标签信息
#             name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
#             infoDict.update({'股票名称': name.text.split()[0]})
#
#             keyList = stockInfo.find_all('dt')
#             valueList = stockInfo.find_all('dd')
#             for i in range(len(keyList)):
#                 key = keyList[i].text
#                 val = valueList[i].text
#                 infoDict[key] = val
#
#             with open(fpath, 'a', encoding='utf-8') as f:
#                 f.write(str(infoDict) + '\n')
#         except:
#             traceback.print_exc()
#             continue


def main():
    # 获取股票列表
    stock_list_url = 'https://quote.eastmoney.com/stocklist.html'
    slist = []
    getStockList(slist, stock_list_url)
    # for i in slist:
    #     print(i)
    # stock_info_url = 'https://gupiao.baidu.com/stock/'
    # output_file = 'D:/BaiduStockInfo.txt'
    # //获得股票编号列表
    # getStockInfo(slist, stock_info_url, output_file)
main()

