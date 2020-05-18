# import requests
# path="D:/abc.JPG"
# r=requests.get("http://placekitten.com/g/500/600")
# print(r.status_code)
# with open(path,'wb') as f:
#     f.write(r.content)
# #     图片上是二进制
# f.close()
import requests
import os
root="D:/picture/"
url="http://placekitten.com/g/500/600"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
    # 收获:文件存储