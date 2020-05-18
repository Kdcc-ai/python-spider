# 参考
# https://blog.csdn.net/zwq912318834/article/details/79571110
# 1.
import requests
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
headers = {
    "Referer":"https://passport.mafengwo.cn/",
    "User-Agent":userAgent,
    # "cookie":"mfw_uuid=5e881e29-54c4-8d42-b414-07aa9ab977fc; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222020-04-04+13%3A42%3A01%22%3B%7D; __mfwc=direct; uva=s%3A92%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1585978923%3Bs%3A10%3A%22last_refer%22%3Bs%3A24%3A%22https%3A%2F%2Fwww.mafengwo.cn%2F%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1585978923%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=5e881e29-54c4-8d42-b414-07aa9ab977fc; UM_distinctid=17143b5d81f2a4-0d61702000e7b7-4313f6a-e1000-17143b5d82044a; __omc_chl=; __omc_r=; c=JkUIZlRl-1585980693485-27510d1b5d69f37189993; __jsluid_s=8697b42d27391335981213eb72822a12; login=mafengwo; __mfwlv=1585986319; __mfwvn=2; __mfwa=1585978921954.54873.3.1585986319280.1585989285049; PHPSESSID=70n49n6tvgmd65ivv5n3bjs7n3; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1585981458,1585982186,1585989285,1585989387; uol_throttle=58911470; mfw_uid=58911470; mfw_passport_redirect=https%3A%2F%2Fwww.mafengwo.cn%2F; __mfwb=f6f5d4db2153.9.direct; __mfwlt=1585989596; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1585989596; _xid=3PkPsk8MaFrgIWSgNG1E%2BclwTvD%2Fz5vCfGbDOvAY5z7xih4vf%2BOKrxp1Y3EeEz35OxunRUELGwvfocGFHRVIhA%3D%3D; _fmdata=rp1psoJQiczuefZk%2Bmf%2Bv6WBbZcQiYI1BpFYWhQJxcl4c7ac9u26dGjrs7AmQaDfMBaydXIc6m7hfRTEwZD7ytt%2BYN9cKs0dkhgOHHi72YE%3D"
    # "cookie":"__jsluid_s=56d9e6cc7ac46e25f4dbb0285ce5cef8; mfw_uuid=5e881e29-54c4-8d42-b414-07aa9ab977fc; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222020-04-04+13%3A42%3A01%22%3B%7D; __mfwc=direct; uva=s%3A92%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1585978923%3Bs%3A10%3A%22last_refer%22%3Bs%3A24%3A%22https%3A%2F%2Fwww.mafengwo.cn%2F%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1585978923%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=5e881e29-54c4-8d42-b414-07aa9ab977fc; UM_distinctid=17143b5d81f2a4-0d61702000e7b7-4313f6a-e1000-17143b5d82044a; __omc_chl=; __omc_r=; __jsluid_h=636a8d26371110468a1915d28ee16bef; bottom_ad_status=0; c=JkUIZlRl-1585980693485-27510d1b5d69f37189993; login=mafengwo; __mfwlv=1585986319; __mfwvn=2; __jsl_clearance=1585986957.923|0|p07JmA8Bj9n238PvQDDTnl7U8fM%3D; __mfwa=1585978921954.54873.3.1585986319280.1585989285049; CNZZDATA30065558=cnzz_eid%3D614989939-1585976396-https%253A%252F%252Fwww.mafengwo.cn%252F%26ntime%3D1585987196; _fmdata=rp1psoJQiczuefZk%2Bmf%2Bv6WBbZcQiYI1BpFYWhQJxcl4c7ac9u26dGjrs7AmQaDfMBaydXIc6m7hfRTEwZD7yn34hhEGX%2BpeL1KMn6w2TsY%3D; _xid=uq1Ga%2FtSC4zOPfhVu%2BfwxU%2BI0%2B4lA2fiJRbZyrCfS0BngkUmv6AOFcEovHdqi3QOzFFHmL%2FBlcrYs30ZcozIpg%3D%3D; PHPSESSID=70n49n6tvgmd65ivv5n3bjs7n3; __mfwb=f6f5d4db2153.4.direct; __mfwlt=1585989386; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1585981458,1585982186,1585989285,1585989387; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1585989387"
}

def Login(account,password):
    print("开始模拟登录马蜂窝...")
    postUrl = "https://passport.mafengwo.cn/login/"
    postData = {
        "passport":account,
        "password":password,
    }
    reponseRes = requests.post(postUrl,data=postData,headers=headers)
    print(f"statusCode = {reponseRes.status_code}")
    print(f"text ={reponseRes.text}")

if __name__ == "__main__":
    Login("13180188351",'lyd340688')



# 2.得到cookie 下次访问的时候就直接带上cookie就可以了
import requests
import http.cookiejar as cookielib
import execjs
import re
# session代表某一次连接
mafengwoSession = requests.session()
# 通过此方法实例化的cookie对象可以直接调用save方法
mafengwoSession.cookies = cookielib.LWPCookieJar(filename='D:\Python爬虫\mafengwoCookies.txt')
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
headers = {
    "Referer":"https://passport.mafengwo.cn/",
    "User-Agent":userAgent,
}
# def executejs(first_html):
#     # 提取其中的JS加密函数
#     js_string = ''.join(re.findall(r'(function .*?)</script>', first_html))
#     # 提取其中执行JS函数的参数
#     js_arg = ''.join(re.findall(r'setTimeout\(\"\D+\((\d+)\)\"', first_html))
#     js_name = re.findall(r'function (\w+)', js_string)[0]
#     # 修改JS函数，使其返回Cookie内容
#     js_string = js_string.replace('eval("qo=eval;qo(po);")', 'return po')
#     func = execjs.compile(js_string)
#     return func.call(js_name, js_arg)
# def parse_cookie(string):
#     string = string.replace("document.cookie='", "")
#     clearance = string.split(';')[0]
#     return {clearance.split('=')[0]: clearance.split('=')[1]}
def Login(account,password):
    print("开始模拟登录马蜂窝...")
    postUrl = "https://passport.mafengwo.cn/login/"
    postData = {
        "passport":account,
        "password":password,
    }
    reponseRes = requests.post(postUrl,data=postData,headers=headers)
    # cookie_str = executejs(reponseRes.content.decode('utf-8'))
    # cookie = parse_cookie(cookie_str)
    print(f"statusCode = {reponseRes.status_code}")
    print(f"text ={reponseRes.content.decode('utf-8')}")
    mafengwoSession.cookies.save()
if __name__ == "__main__":
    Login("13180188351",'lyd340688')


# 3.~~通过访问一个只有在登录界面才能访问的界面判断是否登陆成功~~
# 所以最终形成的登录模式：
# 首先尝试cookie登录 其次如果cookie无法登录成功 就用用户名密码登录 将新的cookie保存下来
import requests
import  http.cookiejar as cookielib
# 代表一次登录
mafengwoSession = requests.session()
mafengwoSession.cookies = cookielib.LWPCookieJar(filename='D:\Python爬虫\mafengwoCookies.txt')
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
headers = {
    "Referer":"https://passport.mafengwo.cn/",
    "User-Agent":userAgent,
}
def Login(account,password):
    print("开始模拟登录马蜂窝...")
    postUrl = "https://passport.mafengwo.cn/login/"
    postData = {
        "passport":account,
        "password":password,
    }
    reponseRes = requests.post(postUrl,data=postData,headers=headers)
    print(f"statusCode = {reponseRes.status_code}")
    print(f"text ={reponseRes.text}")
    mafengwoSession.cookies.save()

def isLoginStatus():
    routeUrl = "http://www.mafengwo.cn/plan/route.php"
    # 设置headers  设置不允许重定向
    reponseRes = mafengwoSession.get(routeUrl,headers=headers,allow_redirects=False)
    print(f"isLoginStatus={reponseRes.status_code}")
    if reponseRes.status_code!=200:
        return False
    else:
        return True
if __name__=='__main__':
    # 先尝试使用已有的cookie登录
    mafengwoSession.cookies.load()
    isLogin = isLoginStatus()
    print(f"is login mafengwo = {isLogin}")

    if isLogin== False:
        print(f"cookie失效 用户重新登录...")
        Login("13180188351","lyd340688")

    routeUrl = "http://www.mafengwo.cn/plan/route.php"
    resp = mafengwoSession.get(routeUrl,headers=headers,allow_redirects=False)
    print(f"resp.status={resp.status_code}")




