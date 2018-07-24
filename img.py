import itchat
import math
import PIL.Image as Image
import os

itchat.auto_login()
friends = itchat.get_friends(update=True)[0:]
user = friends[0]["UserName"]

num = 0
for i in friends:
    img = itchat.get_head_img(userName=i["UserName"])
    fileImage = open('d:/' + "/" + str(num) + ".jpg",'wb')
    fileImage.write(img)
    fileImage.close()
    num += 1

ls = os.listdir('d:/')
each_size = int(math.sqrt(float(640*640)/len(ls)))
lines = int(640/each_size)
image = Image.new('RGB', (640, 640))

x = 0
y = 0
for i in range(0,len(ls)+1):
    try:
        img = Image.open('d:/' + "/" + str(i) + ".jpg")
    except IOError:
        print("Error")
    else:
        img = img.resize((each_size, each_size), Image.ANTIALIAS)
        image.paste(img, (x * each_size, y * each_size))
        x += 1
        if x == lines:
            x = 0
            y += 1
image.save('d:/' + "all.jpg")
itchat.send_image('d:/' + "all.jpg", 'filehelper')