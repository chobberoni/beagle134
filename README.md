BEAGLEBONE BLACK (COREY HOBBS, UC DAVIS, EEC134B SENIOR DESIGN)
----------------------------------------------------------------

![Alt Text](https://github.com/chobberoni/beagle134/blob/master/images/bbblack.jpg)


Introduction
------------
	"First, a bit of vocab: the Beaglebone Black is a single-board computer, 
	like the Raspberry Pi. A single-board computer is pretty much what it 
	sounds like—all the hardware you would expect to find in a desktop or 
	laptop computer, shrunken down and soldered to a single circuit board. 
	A processor, memory, and graphics acceleration are all present as chips 
	on the board.

    To contrast, Arduino boards also have a processor and memory on board,
     but are orders of magnitude less powerful, and lack the specialized
      I/O hardware you need to connect the board to a monitor. In more
       concrete terms, you can hook a Beagleboard Black up to a display,
        speakers, a keyboard and mouse and an Ethernet network, and boot
         into a Linux-based operating system. From there, you can do 
         anything you could do with a (low-powered) Linux computer. 
         You can’t do that with Arduino." - ALEX CASTLE of TESTED.COM

*In this course, I am attempting to implement the BBB as a function*
*generator and digital signal processor hybrid unit.*
*In hopes to create a close feeback loop with an external RF*
*Attenae system that will attached to the output/input of the*
*Beagle Bone Black's usb audio jacks.*

Setting up BBB for this Project
--------------------------------

	Since I started with BBB rev 6a, and I wanted it to run 
	Ubuntu based linux environment, I had to flash it.

####Things Needed to flash BBB:

1. [5V, 2A BBB Power Supply](http://www.amazon.com/Power-Adapter-10W-BeagleBone-Black/dp/B00FA7DLE0/ref=sr_1_1?s=electronics&ie=UTF8&qid=1425883117&sr=1-1&keywords=beaglebone+black+power+supply)
2. [Micro SD Card](http://www.amazon.com/Sandisk-MicroSDHC-Memory-Card-Adapter/dp/B000WH6H1M)
3. [Micro HDMI-HDMI CABLE](http://www.amazon.com/HDMI-Male-Cable-1-3V-33AWG/dp/B0040ZTH2I/ref=sr_1_3?s=wireless&rps=1&ie=UTF8&qid=1425882768&sr=1-3&keywords=micro+hdmi+to+hdmi)
4. [External Monitor](github.com/chobberoni/beagle134/blob/master/images/February%2026%2C%202015%20at%201049PM(1).jpg)
5. [USB Keyboard](http://www.amazon.com/V7-Standard-USB-Keyboard-KC0A1-4N6P/dp/B005Y0G9ME)
6. [USB Mouse](http://www.amazon.com/dp/B002ZIN9DU/ref=cm_sw_r_tw_dp_v9t.ub0GPNG43)
7. [USB Port Extender](http://www.amazon.com/AmazonBasics-4-Port-USB-2-0-Ultra-Mini/dp/B003M0NURK/ref=pd_sim_pc_1?ie=UTF8&refRID=0D15C9R5PZ4RYNTD1BYC)

####[Instructions to flash](http://elinux.org/Beagleboard:Booting_Ubuntu_on_BeagleBoard_Black)
**click link ^^**
	The steps described here are steps you must take before installing any version of Ubuntu described in this Wiki.

	You must first decide which version you want to run.
	This page has the image files for 3 options for installing Ubuntu/Debian on a micro SD card to boot from
	Your 3 options are
	Ubuntu Precise 12.04.2 LTS
	Ubuntu Raring 13.04
	Debian Wheezy 7.0.0
	You have two current options to flash the eMMC
	Your 2 options are (click the name for download location)
	[Ubuntu]
	[Debian]
	After you have downloaded the .img.xz file you want, use a program such as 7zip to extract the image file 
	Insert the micro SD card into your computer 
	Using a micro SD to SD or micro SD to USB adapter is fine 
	Use Win32 Disk Imager to write the image onto your micro SD 
	Run Win32 Disk Imager 
	Make sure the drive letter corresponding to your micro SD card is selected
	Select the unpacked image file 
	Press 'Write' and wait for Win32 Disk Imager to finish - this should take a few minutes 
	After Win32 Disk Imager has finished remove the micro SD card from your computer 
	You are now ready to follow directions below that correspond to the version of Ubuntu/Debian you downloaded.


	Put the micro SD card into the powered-off BeagleBoard Black 
	Make sure your BeagleBoard Black is connected to a powered-on display via HDMI
	While holding down the 'boot' button (button closest to the micro SD card slot), apply power to the BeagleBoard Black
	You must use an external 5V power supply, USB power will not work 
	Continue to hold down the 'boot' button until the 4 LED lights begin to flicker 
	If more than 15 seconds have passed without the lights beginning to flicker, remove the power and try again 
	The Linux penguin should flash in the upper left-hand corner of your display 
	After approximately 2-3 minutes you should be prompted for a username and password
	Username is: ubuntu
	Password is: ubuntu
	Note: echo is turned off for typing in password
	You should now be in the command terminal for Ubuntu
	Anytime you want to boot from micro SD to Ubuntu from now on start at step 6 
	If you wish to load LXDE you can refer to Loading LXDE section.
