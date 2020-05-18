# 记住字符转义符号 'ABC\\-001'代表'ABC\-001'
# 因此我们可以用r前缀 不考虑转义问题 s=r'ABC\-001'

# 功能一：匹配
import re
# match方法判断是否匹配 如果匹配成功返回一个Match对象 否则返回None
# 采用raw string类型表示正咋表达式 表示为 r''
# 原生字符串是不包含转义符的字符串
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
test='用户输入的字符串'
if re.match(r'正则表达式',test):
    print('OK')
else:
    print('failed')


# 功能二:split方法按正则表达式匹配结果进行分割 返回列表类型
# 正常的话可以用split方法 但有缺陷 比如说我们用单空格切分时 就无法识别多空格
# 正则表达式切割比他厉害
# split函数多了一个参数 maxspilt(最大分割数 剩余部分作为一个整体输出)
print(re.split(r'\s+','a b  c'))
print(re.split(r'[\s\,]+','a,b, c  d'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
# !!用户输入了一组标签 下次记得用正则表达式来把不规范的输入转化成正确的数组
print(re.split(r'[1-9]\d{5}','BIT10081 TSU10084',maxsplit=1))

# 功能三:分组match方法匹配的字符串中提取子串,使用()表示分组进行提取 通过group方法打印
print(re.match(r'^(\d{3})-(\d{3,8})$', '010-12345'))
m=re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# 匹配器对象
print(m.group(0))
print(m.group(1))
print(m.group(2))
# 如果正则表达式定义了组 就可以在Match对象上用group方法提取出子串
# group(0)永远是子串 group(1) group(1)....
# 凶残例子 用正则识别合法的时间。
t='19:05:30'
m=re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m)


# 功能四:贪婪匹配 默认是贪婪匹配 就是匹配尽可能多的字符.
# 比如
print(re.match(r'^(\d+)(0*)$','102300').groups())
# \d+ 贪婪匹配 直接把后面0全都匹配了 所以0*只能匹配空字符串了
#用？阻止非贪婪匹配 也就是尽可能少匹配 才能把后面的0匹配出来
print(re.match(r'^(\d+?)(0*)$', '102300').groups())
match=re.search(r'[1-9]\d{5}','BIT 100081')
print(match)
# 例二：
print(re.search(r'PY.*N','PYANBNCNDN').group(0))
#得到最小匹配 进行改进
print(re.search(r'PY.*?N','PYANBNCNDN').group(0))
# 最小匹配操作符  *? 前一个字符0次或无限次扩展，最小匹配
#                +1前一个字符1次或无限次扩展，最小匹配
#                ??前一个字符0次或一次匹配，最小匹配

# 原理: 当我们Python使用正则表达式时 re模块内部会干两件事:
#    1.编译正则表达式 如果正则表达式字符串本身不合法 会报错
#    2.用编译后的正则表达式去匹配字符串

# 如果一个正则表达式重复使用几千次 出于效率的考虑我们可以预编译该正则表达式
# 编译 将符合正则表达式语法的字符串转换成正则表达式对象
re_telephone=re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())


# 爬虫正则表达式学习补充
# 表达文本类型的特征(病毒 入侵等)
# .代表任意单个字符 [] [抑或符]  *表示*之前一个字符出现0或多次  +前一个字符1或多次  ？前一个字符0或一次
# ()分组标记 内部只能使用|
#  匹配中文字符 [\u4e00-\u9fa5]

# search函数 在一个字符串中搜索匹配正则表达式的第一个位置 返回match对象
# search(pattern,string,flags=0)
# 已拍 例子
import re
match=re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0))


# findall函数 搜索字符串,以列表类型返回全部能匹配的子串
# 参数与search同

# findliter函数 获得match对象的迭代类型 可迭代处理


# sub函数
print(re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 TSU10084'))