# -*- coding:utf-8 -*-

from PIL import Image


def processGif(file):
	try:
		gif=Image.open(file)
	except IOError:
		print("cant load",file)
	
	i=0
	mypalette=gif.getpalette()
	
	try:
		while 1:
			gif.putpalette(mypalette)
			new_im=Image.new("RGBA",gif.size)
			new_im.paste(gif)
			new_im.save('image_'+str(i)+'.png')
			i=i+1
			gif.seek(gif.tell()+1)
	except EOFError:
		pass
	#finally gif.close()
	
processGif('1.gif')