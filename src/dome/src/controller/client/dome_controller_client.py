#!/usr/bin/python

import sys
import rospy
#for sidereal values
import datetime as dt
import pytz
import sidereal
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

	def try_refresh_dome_status(self):
		rospy.wait_for_service('refresh_dome_status')
		try:
			refresh_dome_status_srv = rospy.ServiceProxy('refresh_dome_status', update_status)
			roof_msg = refresh_dome_status_srv()
			return roof_msg
		except rospy.ServiceException, e:
			print "Service call failed: %s", e

	#TODO implement the emergency stop function
	def emergency_stop(self):
		# Added some fake information, just to send the Emergency Stop command
		roof_emergency_msg = roof()
		roof_emergency_msg.ubication = 0
		roof_emergency_msg.sensor1 = False
		roof_emergency_msg.sensor2 = False
		roof_emergency_msg.sensor3 = False
		roof_emergency_msg.state = "EMERGENCY_STOP"
		self.pub.publish(roof_emergency_msg)

	def getSiderealTime(self,eLong):
		t = dt.datetime.now(pytz.UTC)
		gst = sidereal.SiderealTime.fromDatetime(t)
		lst_str = str(gst.lst(eLong)).translate(None, '[]hms').split(' ')
		sidereal_time = dt.datetime(t.year, t.month, t.day, int(lst_str[0]), int(lst_str[1]), int(float(lst_str[2])))
		#return lst_str[0]+":"+lst_str[1]+":"+lst_str[2]
		return sidereal_time.strftime("%H:%M:%S")
