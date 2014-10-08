#!/usr/bin/python

from dome.srv import *
from dome.msg import roof
import rospy

def handle_open(req):
	#print "TCS is requesting to open roof at speed: ", req.speed
	rospy.loginfo("TCS is requesting to open roof at speed: " + str(req.speed))
	roof_msg = roof()
	roof_msg.ubication = 0.1
	roof_msg.sensor1 = True
	roof_msg.sensor2 = False
	roof_msg.sensor3 = True
	return roof_msg

def open():
	rospy.init_node('open_server')
	s = rospy.Service('open_dome', open_dome, handle_open)
	#print "ready to open."
	rospy.loginfo("ready to open.")
	rospy.spin()

if __name__ == "__main__":
	open()
