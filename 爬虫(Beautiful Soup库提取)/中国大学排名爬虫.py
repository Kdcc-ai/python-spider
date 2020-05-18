import requests
import  bs4
# 学会分析好HTML标签
# BeautifulSoup库的方法

# 首先获取HTML信息
# 熬成一锅汤
# 把每一行大学信息存入一个列表中
# 输出
def getHTMLText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return " "

def fillUnivList(unifo,html):
    soup= bs4.BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            # 获得td标签的string内容 排名 名称 总分
            unifo.append([tds[0].string,tds[1].string,tds[3].string])

def printUnivList(unifo,num):
    print("{0:{3}^10}\t{1:{3}^10}\t{2:^10}".format("排名","学校名称","总分",chr(12288)))
    for i in range(20):
        u=unifo[i]
        print("{0:{3}^10}\t{1:{3}^10}\t{2:^10}".format(u[0],u[1],u[2],chr(12288)))

def main():
    unifo=[]
    url="http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    # 分析HTML文件信息
    fillUnivList(unifo, html)
    printUnivList(unifo,20)
main()
# 格式化输出 format方法
