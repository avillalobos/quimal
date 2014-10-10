#!/usr/bin/python

import sys
import rospy
from dome.srv import *
from dome.msg import *

class DomeControllerClient:

	def __init__(self):
		# It is not possible to init node from this archive, so the init node has been executed on the GUI application
		#rospy.init_node("dome_controller_client", disable_signals=True)
		self.pub = rospy.Publisher('dome/roof/status', roof, queue_size=100)

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

	def emergency_stop(self):
		# Added some fake information, just to send the Emergency Stop command
		roof_emergency_msg = roof()
		roof_emergency_msg.ubication = 0
		roof_emergency_msg.sensor1 = False
		roof_emergency_msg.sensor2 = False
		roof_emergency_msg.sensor3 = False
		roof_emergency_msg.state = "EMERGENCY_STOP"
		self.pub.publish(roof_emergency_msg)
