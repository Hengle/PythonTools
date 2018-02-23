# -*- coding:utf-8 -*-

import time
from time import sleep
from PIL import ImageGrab

m=int(input("请输入抓屏时间s: "))
#m=m*60
sleepTime=0.01
n=1

while n<m:
	sleep(sleepTime)
	im =ImageGrab.grab()
	dt = list(time.localtime())
	imageName=str(dt[0])+"-"+str(dt[1])+"-"+str(dt[2])+"-"+str(dt[3])+"-"+str(dt[4])+"-"+str(dt[5])+"-"+str(n)+".jpg"
	print(imageName)
	im.save(imageName,'jpeg')
	n=n+1