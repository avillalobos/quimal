#!/usr/bin/python

from dome.srv import *
from dome.msg import roof
import rospy, time, serial, os.path
from subprocess import call

class LateralDoorController:
	def __init__(self):
		rospy.init_node('LateralDoor_Controller')
		super(LateralDoorController,self).__init__()
		self.pub = rospy.Publisher('dome/lateral_door/status', roof, queue_size=100)
		# useful only on Raspberry PI
		self.status_pin = 18
		self.STATES={"PREPARING":"PREPARING","STARTING":"STARTING","OPENING":"OPENING","OPEN":"OPEN", "CLOSING":"CLOSING", "PARKING":"PARKING", "PARKED":"PARKED", "CLOSED":"CLOSED", "FINISH":"FINISH", "ABORTED":"ABORTED", "STOPPING":"STOPPING", "STOP":"STOP", "EMERGENCY_STOP":"EMERGENCY_STOP"}
		roof_initial_msg = self.getInitialState()
		self.roof_status = None
		self.last_roof_status = None
		rospy.Subscriber("dome/roof/status", roof, self.callback)
		while self.roof_status == None:
			rospy.loginfo("waiting to store first message of roof status")
			self.pub.publish(roof_initial_msg)
			time.sleep(1)
		# TODO fix this part to match with the corresponding arduino and fixing the timeout
		self.rate = rospy.Rate(10)
		
	def action_open_lateral_door(self):
		roof_msg = roof()
		msg = self.arduino.write("openLateralDoor")
		msg = self.readLineFromArduino()
		while msg != "FINISH":
			if self.roof_status.state != self.STATES["EMERGENCY_STOP"]:
				roof_msg = self.createRoofMSG("openLateralDoor",msg,True,False,True,1)
				self.pub.publish(roof_msg)
				rospy.loginfo(msg)
				# This frequency should be modified once the hardware is connected

				self.rate.sleep()
			else:
				rospy.logwarn("Due an Emergency stop message, the opening of the lateral door has been stopped!")
				break;
			msg = self.readLineFromArduino()
		
		rospy.loginfo("Lateral door status: " + msg)
		# getting the last message
		msg = self.readLineFromArduino()	
		rospy.loginfo("Lateral door final state: " + msg)
		return roof_msg

	def action_close_lateral_door(self):
		roof_msg = roof()
		msg = self.arduino.write("closeLateralDoor")
		msg = self.readLineFromArduino()
		while msg != "FINISH":
			if self.roof_status.state != self.STATES["EMERGENCY_STOP"]:
				roof_msg = self.createRoofMSG("closeLateralDoor",msg,True,False,True,1)
				self.pub.publish(roof_msg)
				rospy.loginfo(msg)
				# This frequency should be modified once the hardware is connected
				r = rospy.Rate(0.5)
				r.sleep()
			else:
				rospy.logwarn("Due an Emergency stop message, the opening of the lateral door has been stopped!")
				break;
			msg = self.readLineFromArduino()
		
		rospy.loginfo("Lateral door status: " + msg)
		# getting the last message
		msg = self.readLineFromArduino()	
		rospy.loginfo("Lateral door final state: " + msg)
		return roof_msg
