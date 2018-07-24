# coding:utf-8
import itchat
import re
# 先登录
itchat.login()

# 获取好友列表
friends = itchat.get_friends(update=True)[0:]

for i in friends:
    # 获取个性签名
    signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
    # 正则匹配过滤掉emoji表情，例如emoji1f3c3等
    rep = re.compile("1f\d.+")
    signature = rep.sub("", signature)
    if signature != "":
        print(signature)
        print("----------------")