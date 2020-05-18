# https://blog.csdn.net/gueter/article/details/1524447
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017804782304672
# 以上两个博客讲的不错 可以参考



# Web 应用 服务器传递网页->浏览器 实际上是把网页的HTML代码发送给浏览器
# HTTP(超文本传输协议)
#  ..HTML是一种用来定义网页的文本 会HTML 就可以编写网页
#  ..HTTP是在网络上传输HTML的协议,用于浏览器和服务器通信

# https://www.liaoxuefeng.com/wiki/1016959663602400/1017804782304672
# 谷歌浏览器 开发者工具 Elements显示网页结构 Network显示浏览器和服务器的通信
# 通过查看谷歌浏览器访问新浪主页 点击view source显示服务器返回的原始数据
# 讲解了HTTP响应相应分为Header和Body两部分(Body)可选
# 紧接着说明了这两部分都代表什么 上面是他的博客地址
# !!浏览器不靠URL来判断响应的内容,通过Content-Type来判断响应的内容
# !!还可以看网页HTML源码(记住记住 是源码)
# 当浏览器读取到新浪首页的HTML源码后,他会解析HTML，显示界面->根据HTML里面的各种链接->发送HTTP请求给新浪服务器
# ->拿到响应的图片、视频、JS脚本、CSS等各种资源->显示出一个完整的界面


# HTTP请求流程:
# 1.浏览器首先向服务器发送HTTP请求包括：GET还是POST GET仅请求资源 POST会附带用户数据
#                                     路径:/full/url/path
#                                     域名:由Host头指定,就比如等新浪主页的那个Host:www.sina.com.cn 以及其他相关的Header
#                                     如果是POST 那么请求还包括一个Body包含用户数据
# 2.服务器向浏览器返回HTTP响应,响应包括: 响应代码 200表示成功 3××表示重定向 4××表示客户端发送的请求有错误 5××表示服务器端的处理发生了错误
#                                      响应类型 Content-Type指定 Content-Type: text/html;charset=utf-8表示响应类型是HTML文本，并且编码是UTF-8，
#                                      Content-Type: image/jpeg表示响应类型是JPEG格式的图片;
#                                      以及其他相关的Header
#                                      通常服务器的HTTP响应会携带内容 也就是有一个Body 包含响应的内容,网页的HTML源码就在Body中
# 3.如果浏览器还需要继续向服务器请求其他资源 比如图片 就在此发出HTTP请求 重复步骤1 2
# 评价:这种HTTP协议采用了非常简单的请求-响应模式 大大简化的开发
# 所以说当我们编写一个页面时,我们只需要在HTTP响应中发送HTML 不需要考虑如何附带图片、视频。
# 浏览器如果请求视频 图片啥的 它会发送另一个HTTP请求。因此一个HTTP请求只处理一个资源


# HTTP协议扩展性极强,就比如刚才我们请求了http://www.sina.com.cn/的首页,但是
# 新浪在HTML中可以链入其他服务器的资源,比如<img src="http://i1.sinaimg.cn/home/2013/1008/U8455P30DT20131008135420.png">
# 从而将请求压力分散到各个服务器上,并且一个站点可以链接到其他站点,无数个站点互相链接起来,就形成了World Wide Web




# HTTP格式:
# HTTP是一种文本协议,所以它的格式也非常简单。HTTP GET请求的格式:
# GET /path HTTP/1.1 请求行
# Header1: Value1  消息报头
# Header2: Value2
# Header3: Value3  每个Header一行一个 换行符是\r\n

# HTTP POST请求的格式:
# POST /path HTTP/1.1 请求行
# Header1: Value1 消息报头
# Header2: Value2
# Header3: Value3
#
# body data goes here... 当遇到两个\r\n时 Header部分结束 后面的数据全是Body 消息正文

# HTTP响应的格式：
# 200 OK 状态头
# Header1: Value1  消息报头
# Header2: Value2
# Header3: Value3
#
# body data goes here... 两个\r\n之后的就是Body 响应正文
# 再次注意Body的数据类型有Content-Type确定 如果是网页Body就是文本 如果是图片Body就是图片的二进制数据
# 当存在Content-Encoding,Body的数据是被压缩的,最常见的压缩方式是gzip.
# 所以,看到Content-Encoding: gzip时 先将Body数据解压缩得到真正的数据
# 压缩的目的在于减少Body大小 加快网络传输

# URL:protocol://hostname:port/resourcename#anchor

# 关于实体报头
