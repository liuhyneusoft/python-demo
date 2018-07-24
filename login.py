# -*- coding: utf-8 -*-
import itchat

itchat.login()

# 发送消息,filehelper 就是微信上的文件传输助手
itchat.send(u'你好', 'filehelper')

# 获取好友列表
friends = itchat.get_friends(update=True)[0:]

# 初始化计数器，有男有女，当然，有些人是不填的
male = female = other = 0

# 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
# 1表示男性，2女性
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

# 总数
total = len(friends[1:])

print(u"man：%.2f%%" % (float(male) / total * 100))
print(u"woman：%.2f%%" % (float(female) / total * 100))
print(u"other：%.2f%%" % (float(other) / total * 100))

