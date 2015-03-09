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

    In this course, I am attempting to implement the BBB as a function
     generator and digital signal processor hybrid unit. 
    In hopes to create a close feeback loop with an external RF 
    Attenae system that will attached to the output/input of the
    Beagle Bone Black's usb audio jacks.

Setting up BBB for this Project
--------------------------------

Since I started with BBB rev 6a, and I wanted it to run Ubuntu based linux environment, I had to flash it.

###Things Needed to flash BBB:

[5V, 2A BBB Power Supply](www.amazon.com/Power-Adapter-10W-BeagleBone-Black/dp/B00FA7DLE0/ref=sr_1_1?s=electronics&ie=UTF8&qid=1425883117&sr=1-1&keywords=beaglebone+black+power+supply)
[Micro SD Card](www.amazon.com/Sandisk-MicroSDHC-Memory-Card-Adapter/dp/B000WH6H1M)
[Micro HDMI-HDMI CABLE](www.amazon.com/HDMI-Male-Cable-1-3V-33AWG/dp/B0040ZTH2I/ref=sr_1_3?s=wireless&rps=1&ie=UTF8&qid=1425882768&sr=1-3&keywords=micro+hdmi+to+hdmi)
[External Monitor](github.com/chobberoni/beagle134/blob/master/images/February%2026%2C%202015%20at%201049PM(1).jpg)
[USB Keyboard](www.amazon.com/V7-Standard-USB-Keyboard-KC0A1-4N6P/dp/B005Y0G9ME)
[USB Mouse](www.amazon.com/dp/B002ZIN9DU/ref=cm_sw_r_tw_dp_v9t.ub0GPNG43)
[USB Port Extender](www.amazon.com/AmazonBasics-4-Port-USB-2-0-Ultra-Mini/dp/B003M0NURK/ref=pd_sim_pc_1?ie=UTF8&refRID=0D15C9R5PZ4RYNTD1BYC)