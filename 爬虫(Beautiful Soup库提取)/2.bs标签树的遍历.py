from bs4 import BeautifulSoup
import  requests
# 下行遍历 contents
soup=BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>",'html.parser')
print(soup.b)
# 获得b标签的儿子节点 放到一个列表中 可以进行迭代
print(soup.b.contents)

# 对于一个标签的儿子节点包括:标签节点 字符串节点比如说\n
# 返回儿子节点的个数
# 通过已知个数可以进行for循环遍历
print(len(soup.b.contents))



# # 上行遍历 parent(1个父亲节点) parents(循环遍历父亲节点)
r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup2=BeautifulSoup(demo,"html.parser")
print(soup2.title.parent)
# 父亲节点是head标签
# 这块一定要记住HTML界面的树形形状
print(soup2.html.parent)
# html是HTML界面最高级标签 打印本身
print(soup2.parent)
# soup标签的父亲是空的
print(soup2)
# 进行某一标签的父亲全部遍历
for parent in soup2.a.parents:
    # 会遍历到soup标签树本身 而soup标签是没名字的
    # 所以打印自己
    if parent is None:
        print(parent)
    else:
        print(parent.name)


# 平行遍历:记住！！平行遍历一定时发生在同一个父节点下的同节点
soup3=BeautifulSoup(demo,"html.parser")
# 而且记住平行标签可能有NavigableString类型 也就是string类型的也会放到树上
print(soup3.a.next_sibling)
print(soup3.a.next_sibling.next_sibling)
print(soup3.a.previous_sibling)
