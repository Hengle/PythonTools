# -*- coding:utf-8 -*-

'''
电脑开机后的自动处理

开机自启
首先选择"运行",输入以下字:shell:Startup确定,
进入到C:\Users\Scarlett\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup文件夹下。
下一步，只要将可执行的文件放进来，就可以开机自启了。

'''

import os
import winsound
import time


def readexeFile(filePath):
	results=[]
	try:
		exe_file=open(filePath)
		for file_line in exe_file.readlines():
			content = file_line.strip('\n')
			results.append(content)
	
	finally:
		exe_file.close()
		
	return results
		
#开机启动应用
exeFile=os.getcwd()+'/exe.txt'

def doExes(exes):
	for exe in exes:
		print('open'+exe)
		os.startfile(exe)
		
		
doExes(readexeFile(exeFile))



'''
#整点的时候播放音乐
soundFile=os.getcwd()+'/sound.wav'
def playSound():
	winsound.PlaySound(soundFile,winsound.SND_FILENAME)
	time.sleep(60)

while(True):
	dt=list(time.localtime())
	hour = dt[3]
	min = dt[4]
	if (hour ==12 and min == 0) or \
		(hour ==6 and min == 0):
		playSound()
'''	