#!/usr/bin/env python 

import sys, os
import rospy
from telescope.srv import *

sys.path.append(os.path.abspath((os.path.dirname(__file__) + "/../../controller/")))
import controller as controller

#from controller import controller

def getinfo():
	controller.getinfo()

def setdec():
	dec = str(raw_input("Enter DEC: "))
	info = controller.setdec(dec)

def setra():
	ra = str(raw_input("Enter RA: "))
	status = controller.setra(ra)

def setslewrate():
	slew = str(raw_input("Enter Slew rate"))
	status = controller.setslewrate(slew)

def settarget():
	option = str(raw_input("Equatorial (eq) or AltAz mount (altaz): "))
	if option == "eq":
		ra = str(raw_input("Enter RA: "))
		dec = str(raw_input("Enter DEC: "))
		status = controller.seteqtarget(ra,dec)
	elif option == "altaz":
		alt = str(raw_input("Enter ALT: "))
		az = str(raw_input("Enter AZ: "))
		status = controller.setaltaztarget(alt,az)
		

def park():
	controller.park()

def stopSlewing():
	controller.stopSlewing()

if __name__ == "__main__":
	rospy.init_node('telescope_control_client', anonymous=True)
	flag = True
	while flag:
		option = str(raw_input("Enter an option or blank to quit "))
		if option == '':
			break
		else:
			if option == "info":
				getinfo()
			elif option == "dec":
				setdec()
			elif option == "ra":
				setra()
			elif option == "slew":
				setslewrate()
			elif option == "target":
				settarget()
			elif option == "park":
				park()
			elif option == "stop":
				stopSlewing()
			else:
				flag = False
