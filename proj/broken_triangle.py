#/usr/bin/python
import os


#start system

print os.system("clear"),chr(13),"  ",chr(13),


def signals():
	global triangle

	triangle=chr(0)+chr(7)+chr(15)+chr(29)+chr(63)+chr(29)+chr(15)+chr(7)

	waveform=triangle
	select="GOLCU."
	count=1

	while 1:
		print os.system("clear"),chr(13),"  ",chr(13),
		print

		waveform=triangle
		print os.system("clear"),chr(13),"  ",chr(13),
		print
		
		audio=file('/dev/audio', 'wb')
		
		count=0
		while count<2000:
			audio.write(waveform)
			count=count+1
		audio.close()

signals()
