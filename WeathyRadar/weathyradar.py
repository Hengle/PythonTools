# -*- coding:utf-8 -*-


from pyquery import PyQuery as pq
import urllib,urllib2
from PIL import Image
import os
#import requests

def saveImg(imageURL,fileName):
     u = urllib.urlopen(imageURL)
     data = u.read()
     f = open(fileName, 'wb')
     f.write(data)
     f.close()	

#d = pq('http://products.weather.com.cn/product/radar/index/procode/JC_RADAR_AZ9210_JB')
d = pq('http://products.weather.com.cn/product/radar/index/procode/JC_RADAR_AZ9250_JB')
DomTree = d('#slideform #slide option')


n=0
for item in DomTree.items():
	pic=item.attr('bigpic')
	fileName=pic[81:]
	#print(fileName)
	saveImg(pic,fileName)	
	n=n+1

images=[]
filelist = os.listdir(os.getcwd())
for file in filelist:
	#print file
	if os.path.splitext(file)[1]=='.png':
		print file
		try:
			image=Image.open(file)
			images.append(image)
		except IOError:
			print("read",file,"failed")

print(len(images))
gifimage=Image.new("RGBA",(640,480))
gifimage.save("1.gif",save_all=True,append_images=images,loop=1,duration=10*len(images),comment=b"complete")
