# -*- coding:utf-8 -*-

import time
from time import sleep
from PIL import ImageGrab
from PIL import Image

m=int(input("请输入抓屏时间s: "))
#m=m*60
sleepTime=0.01
n=1

images=[]
gifSize=[]

while n<m:
	sleep(sleepTime)
	im =ImageGrab.grab()
	dt = list(time.localtime())
	#imageName=
	imageName=str(dt[0])+"-"+str(dt[1])+"-"+str(dt[2])+"-"+str(dt[3])+"-"+str(dt[4])+"-"+str(dt[5])+"-"+str(n)+".jpg"
	print(imageName)
	im.save(imageName,'jpeg')
	n=n+1
	images.append(im)
	gifSize=im.size
	
	
print(images)
gifImage=Image.new("RGBA",gifSize)
gifImage.save("1.gif",save_all=True,append_images=images,loop=1,duration=10*len(images),comment=b"complete")
	
	
