#!/usr/bin/python

import sys
import rospy
from telescope.srv import *
from telescope.msg import *

class TelescopeControllerClient:

	def __init__(self):
		print "Starting"

	def getinfo(self):
        	rospy.wait_for_service('getInfo')
	        try:
	                getInfo_srv = rospy.ServiceProxy('getInfo', getInfo)
	                info = getInfo_srv()
	                rospy.loginfo("Telescope status: \n" + str(info))
			return info
	        except rospy.ServiceException, e:
	                rospy.logfatal("Service call failed: %s" + e)
			return None

	def setdec(self,DEC):
	        rospy.wait_for_service('setDEC')
	        try:
	                setdec_srv = rospy.ServiceProxy('setDEC', setDEC)
	                status = setdec_srv(DEC)
	                rospy.loginfo("Telescope status:\n" + str(status))
			return status
	        except rospy.ServiceException, e:
	                rospy.logfatal("Service call failed: %s" + e)
			return None

	def setra(self,RA):
	        rospy.wait_for_service('setRA')
	        try:
	                setra_srv = rospy.ServiceProxy('setRA', setRA)
	                status = setra_srv(RA)
	                rospy.loginfo("Telescope status:\n" + str(status))
			return status
	        except rospy.ServiceException, e:
	                rospy.logfatal("Service call failed: %s" + e)
			return None

	
	def setslewrate(self,slew):
	        rospy.wait_for_service('setSlewRate')
	        try:
	                setslewrate_srv = rospy.ServiceProxy('setSlewRate', setSlewRate)
	                status = setslewrate_srv(slew)
	                rospy.loginfo("Telescope status:\n" + str(status))
			return status
	        except rospy.ServiceException, e:
	                rospy.logfatal("Service call failed: %s" + e)
			return None

	
	def settarget(self,RA, DEC):
	        rospy.wait_for_service('setTarget')
	        try:
	                settarget_srv = rospy.ServiceProxy('setTarget', setTarget)
	                status = settarget_srv(RA,DEC)
	                rospy.loginfo("Telescope status:\n" + str(status))
			return status
	        except rospy.ServiceException, e:
	                rospy.logfatal("Service call failed: %s" + e)
			return None

	def park(self):
                rospy.wait_for_service('Park')
                try:
                        park_srv = rospy.ServiceProxy('Park', Park)
                        status = park_srv()
                        rospy.loginfo("Telescope status:\n" + str(status))
                        return status
                except rospy.ServiceException, e:
                        rospy.logfatal("Service call failed: %s" + e)
                        return None
	
	def stopSlewing(self):
                rospy.wait_for_service('StopSlewing')
                try:
                        park_srv = rospy.ServiceProxy('StopSlewing', StopSlewing)
                        status = park_srv()
                        rospy.loginfo("Telescope status:\n" + str(status))
                        return status
                except rospy.ServiceException, e:
                        rospy.logfatal("Service call failed: %s" + e)
                        return None
