# -*- coding:utf-8 -*-

'''
���Կ�������Զ�����

��������
����ѡ��"����",����������:shell:Startupȷ��,
���뵽C:\Users\Scarlett\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup�ļ����¡�
��һ����ֻҪ����ִ�е��ļ��Ž������Ϳ��Կ��������ˡ�

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
		
#��������Ӧ��
exeFile=os.getcwd()+'/exe.txt'

def doExes(exes):
	for exe in exes:
		print('open'+exe)
		os.startfile(exe)
		
		
doExes(readexeFile(exeFile))



'''
#�����ʱ�򲥷�����
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