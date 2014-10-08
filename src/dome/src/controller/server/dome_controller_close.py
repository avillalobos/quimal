#!/usr/bin/python

from dome.srv import *
from dome.msg import roof
import rospy

def handle_close(req):
	rospy.loginfo("TCS is requesting to close roof at speed: " + str(req.speed))
	#print "TCS is requesting to close roof at speed: ", req.speed
	roof_msg = roof()
	roof_msg.ubication = 0.1
	roof_msg.sensor1 = True
	roof_msg.sensor2 = False
	roof_msg.sensor3 = True
	return roof_msg

def close():
	rospy.init_node('close_server')
	s = rospy.Service('close_dome', close_dome, handle_close)
	rospy.loginfo("ready to close.")
	#print "ready to close."
	rospy.spin()

if __name__ == "__main__":
	close()
