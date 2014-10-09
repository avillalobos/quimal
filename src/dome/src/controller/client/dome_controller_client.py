#!/usr/bin/python

import sys
import rospy
from dome.srv import *
from dome.msg import *

class DomeControllerClient:

	def try_open(self, speed):
		rospy.wait_for_service('open_dome')
		try:
			open_dome_srv = rospy.ServiceProxy('open_dome', open_dome)
			roof_msg = open_dome_srv(speed)
			return roof_msg
		except rospy.ServiceException, e:
			print "Service call failed: %s"%e
	
	def try_close(self, speed):
		rospy.wait_for_service('close_dome')
		try:
			close_dome_srv = rospy.ServiceProxy('close_dome', close_dome)
			roof_msg = close_dome_srv(speed)
			return roof_msg
		except rospy.ServiceException, e:
			print "Service call failed: %s", e
