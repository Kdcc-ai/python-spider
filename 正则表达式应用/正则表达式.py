# 介绍match对象
# 正则表达式中的search match函数等返回的都是个match对象
import re
match=re.search(r'[1-9]\d{5}','BIT 100081')
# 注意match对象返回的只是第一次匹配的结果
# 那么如果我们希望得到每一次匹配的返回对象 用finditer(可能写错了)来实现
print(type(match))
# .group(0) 获得匹配后的字符串
# .start()匹配字符串在原始字符串的开始位置
# .end().......................最后位置
print(match.string)
print(match.re)