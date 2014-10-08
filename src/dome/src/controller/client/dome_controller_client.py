#!/usr/bin/python

import sys
import rospy
from dome.srv import *
from dome.msg import *

def try_open(speed):
	rospy.wait_for_service('open_dome')
	try:
		open_dome_srv = rospy.ServiceProxy('open_dome', open_dome)
		roof_msg = open_dome_srv(speed)
		return roof_msg
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e

def try_close(speed):
	rospy.wait_for_service('close_dome')
	try:
		close_dome_srv = rospy.ServiceProxy('close_dome', close_dome)
		roof_msg = close_dome_srv(speed)
		return roof_msg
	except rospy.ServiceException, e:
		print "Service call failed: %s", e

if __name__ == "__main__":

	if sys.argv[1] == "open":
		print "Requesting to open at speed: ", sys.argv[2]
	    	speed = int(sys.argv[2])
		print "Server response status of dome:"
		roof_msg = try_open(speed)
		print roof_msg
	elif sys.argv[1] == "close":
                print "Requesting to open at speed: ", sys.argv[2]
                speed = int(sys.argv[2])
                print "Server response status of dome:"
                roof_msg = try_close(speed)
                print roof_msg
	else:
		print "Wrong option!, please try [open|close] options followed by the speed"
