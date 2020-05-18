# 北京理工大学嵩天老师Python网络爬虫
# 获取淘宝搜索页面的信息,提取其中的商品名称和价格

# 淘宝的搜索接口 翻页的处理

# # 提交请求 循环获取页面
# # 循环获取商品信息

import requests
import re
def getHTMLText(url):
    kv = {'cookie':'cookie: t=d61223e23cf95eaf3a7427e46620aa24; cna=KknhFroZHEcCAXgEbDkPkMA5; uc3=id2=VyyY5AHPxrqV%2Fw%3D%3D&vt3=F8dBxd7Ed9v7gopWytk%3D&nk2=F5RDL9RuzK7CKw%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D; lgc=tb63955929; uc4=nk4=0%40FY4I7KuEOrzqo%2FORxKFzLHtXG%2FsW&id4=0%40VXtXDzG6mttLTb9dnw5IY8EDQymW; tracknick=tb63955929; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; enc=LkWXCr2rjtrUCLxXukiml03lT75soVzYczcswxlr3pPb91SbW6nkCHg9kH18ZBufnpJmNA%2BV4hlHn3ZYmwG5wA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=43_1; thw=cn; _samesite_flag_=true; cookie2=7ca742e000f0e87cb18cd16d396d59c7; _tb_token_=fb77408ed1e35; tfstk=cAHPBOXQbLpyCdOD1RyURCxwrZoRZHHnCQELZfX6epLMjPPli9bLmUI-y2z9n7f..; JSESSIONID=F698065DA30CCD2462BC75EEB3EAA4CB; v=0; l=dBaLyT4nQF2x7TpkBOCgCm5f0AQTdIRAgul44rNpi_5dp1T1cDbOour9He96cjWftUTB4o0COBe9-etktBDmndK-g3fPaxDc.; isg=BK-vdiweLUCDhSl8udLLyqTuPsO5VAN2g_ZtwcE8YZ4lEM8SySTgxq3KkgAuaNvu; uc1=cookie14=UoTUOan4slJdzQ%3D%3D',
          'user-agent':'Mozilla/5.0'}

    try:
        r = requests.get(url, headers=kv,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""



def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        # 最小匹配表明只取得最后一个双引号为止的那部分内容 最小匹配！！重要啊
        # plt tlt返回符合要求的字符串列表
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    # https://s.taobao.com/search?q= 是我们提交淘宝页面关键词浏览器返回的链接接口
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        #最终是[[],[],[]...]的列表形式
        except:
            continue
    printGoodsList(infoList)
    #进行输出信息
main()

# 老师还讲到作为爬虫 要确认淘宝是否允许用户在网页爬取相关信息,因此查看淘宝的robots协议
# 发现对所有的爬虫限制了disallow 但如果对淘宝的访问频率不高,那么是可以成功的