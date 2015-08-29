#!/usr/bin/python

from arduino.dome_controller import DomeController
from raspberry.dome_controller import DomeController
import sys, rospy

if __name__ == "__main__":
	if len(sys.argv) <= 1 :
		print "You should indicate if you want a Raspberry PI based controller (raspberry) or an Arduino based controller (arduino)"
	elif sys.argv[1] == "arduino":
		if len(sys.argv) == 2:
			dome_controller = DomeController(sys.argv[1])
			dome_controller.server()
		else:
			print "You should indicate also the device name as a parameter"
	elif sys.argv[1] == "raspberry":
		dome_controller = DomeController()
		dome_controller.server()
	else:
		print "You should indicate either raspberry or arduino base controller"