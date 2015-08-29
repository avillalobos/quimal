#!/usr/bin/python

from dome.srv import *
from dome.msg import roof
import rospy, time, serial, os.path, sys
from super_controller import SuperController
from subprocess import call
from std_msgs.msg import String

class DomeController(SuperController):

#=================================================================================================

	def __init__(self,device_name):
		self.roof_status = None
		rospy.init_node('Arduino_ROOF_Controller')
		super(DomeController,self).__init__(device_name)
		self.pub = rospy.Publisher('dome/roof/status', roof, queue_size=100)
		rospy.Subscriber("dome/roof/status", roof, self.callback)
		self.mode = "LOCAL"
		rospy.Subscriber("dome/mode", String, self.updateMode)
		# useful only on Raspberry PI
		self.status_pin = 18
		roof_initial_msg = self.getInitialState()
		self.last_roof_status = None
		while self.roof_status == None:
			rospy.loginfo("waiting to store first message of roof status")
			self.pub.publish(roof_initial_msg)
			time.sleep(1)

#=================================================================================================
# UTILS
#=================================================================================================

	def str2bool(self,value):
		if value == '1':
			return True
		elif value == '0':
			return False
		else:
			return False

	def createRoofMSG(self,msgs_list):
		roof_msg = roof()
		try:
			roof_msg.open_button = self.str2bool(msgs_list["open_button"])
		except KeyError, e:
			rospy.loginfo("Unable to find key open_button from msg received by Arduino")
			roof_msg.open_button = False
		try:
			roof_msg.close_button = self.str2bool(msgs_list["close_button"])
		except KeyError, e:
			rospy.loginfo("Unable to find key close_button from msg received by Arduino")
			roof_msg.close_button = False
		try:
			roof_msg.opening_sensor = self.str2bool(msgs_list["opening_sensor"])
		except KeyError, e:
			rospy.loginfo("Unable to find key opening_sensor from msg received by Arduino")
			roof_msg.opening_sensor = False
		try:
 			roof_msg.closing_sensor = self.str2bool(msgs_list["closing_sensor"])
 		except KeyError, e:
			rospy.loginfo("Unable to find key closing_sensor from msg received by Arduino")
			roof_msg.closing_sensor = False
		try:
			roof_msg.safety_sensor = self.str2bool(msgs_list["safety_sensor"])
		except KeyError, e:
			rospy.loginfo("Unable to find key safety_sensor from msg received by Arduino")
			roof_msg.safety_sensor = False
		try:
			roof_msg.meteorologic_sensor = self.str2bool(msgs_list["meteorologic_sensor"])
		except KeyError, e:
			rospy.loginfo("Unable to find key meteorologic_sensor from msg received by Arduino")
			roof_msg.meteorologic_sensor = False
		try:
 			roof_msg.state = msgs_list["status"]
 		except KeyError, e:
			rospy.loginfo("Unable to find key status from msg received by Arduino")
			roof_msg.state = "No status recived"
		try:
			roof_msg.action = msgs_list["action"]
		except KeyError, e:
			rospy.loginfo("Unable to find key action from msg received by Arduino")
			roof_msg.action = "No action received"
		return roof_msg

	# this code must be developed with the electronics and mechanical team.
	def getInitialState(self):
		roof_initial_msg = roof()
		# This make a change on the pin status so that the interruption will be triggered and a message will be received by Serial port
		self.blinkGPIO()
		# raw lecture from the arduino
		hardware_info = self.readLineFromArduino()
		roof_initial_msg = self.createRoofMSG(self.parseArduinoLecture(hardware_info))
		self.pub.publish(roof_initial_msg)
		return roof_initial_msg
	
	# Callback to receive the status of the Dome at any time
	def callback(self, data):
		if data.state == self.STATES["EMERGENCY_STOP"]:
			rospy.logwarn("RECEIVED AN EMERGENCY STOP!, DOME WILL STOP AS SOON AS POSSIBLE!")
		else:
			rospy.loginfo("received new status: " + str(data.state))
		self.last_roof_status = self.roof_status
		self.roof_status = data

	def updateMode(self,data):
		rospy.logwarn("Warning, a change of mode have been detected!, mode:  " + data.data)
		self.mode = data.data

#=================================================================================================
# CORE
#=================================================================================================

	# perform the actions to open the dome
	def action_open(self):
		roof_msg = roof()
		msg = self.arduino.write("openDome")
		msg = self.readLineFromArduino()
		msg = self.parseArduinoLecture(msg)
		emergency_stop = False
		while msg["status"] != "FINISH" and msg["status"] != "ABORTED":
			if self.roof_status.state != self.STATES["EMERGENCY_STOP"]:
				roof_msg = self.createRoofMSG(msg)
				self.pub.publish(roof_msg)
				self.rate.sleep()
			else:
				rospy.logwarn("Due an Emergency stop message, the opening of the dome has been stopped!")
				emergency_stop = True
				break;
			msg = self.readLineFromArduino()
			msg = self.parseArduinoLecture(msg)

		rospy.loginfo("Roof status: " + msg["status"])
		if emergency_stop == False:
		# getting the last message
			msg = self.readLineFromArduino().split(":")
			rospy.loginfo("Roof final state = [action performed:" + msg[0] + " | status:" + msg[1] +" | next action:" + msg[2] + "]")
		else:
			rospy.logwarn("Executing emergency stop")
		return roof_msg


	# perform the actions to close the dome
	def action_close_dome(self):
		msg = self.arduino.write("closeDome")
		msg = self.readLineFromArduino()
		msg = self.parseArduinoLecture(msg)
		emergency_stop = False
		while msg["status"] != "FINISH" and msg["status"] != "ABORTED":
			if self.roof_status.state != self.STATES["EMERGENCY_STOP"]:
				roof_msg = self.createRoofMSG(msg)
				self.pub.publish(roof_msg)
				self.rate.sleep()
			else:
				rospy.logwarn("Due an Emergency stop message, the close of the dome has been stopped!")
				emergency_stop = True
				break;
			msg = self.readLineFromArduino()
			msg = self.parseArduinoLecture(msg)
			
		rospy.loginfo("Roof status: " + msg["status"])
		if emergency_stop == False:
		# getting the last message
			msg = self.readLineFromArduino().split(":")
			rospy.loginfo("Roof final state = [action performed:" + msg[0] + " | status:" + msg[1] +" | next action:" + msg[2] + "]")
		else:
			rospy.logwarn("Executing emergency stop")
		return roof_msg

	# perform the actions to open the dome
	def handle_refresh_dome_status(self,req):
		rospy.loginfo("A new request of refresh have been received" + str(req))
		roof_msg = roof()
		# if this is not running under Raspberry PI, will just write by the serial port the command 'status'
		self.blinkGPIO()
		msg = self.readLineFromArduino()
		msg = self.parseArduinoLecture(msg)
		roof_msg = self.createRoofMSG(msg)
		self.pub.publish(roof_msg)
		rospy.loginfo("Roof status: " + roof_msg.state)
		return roof_msg



	# Start the server to answer the different services handled	
	def server(self):
		s1 = rospy.Service('open_dome', open_dome, self.handle_open)
		s2 = rospy.Service('close_dome', close_dome, self.handle_close)
		s3 = rospy.Service('refresh_dome_status', update_status , self.handle_refresh_dome_status)
		rospy.loginfo("ready to go!.")
		rospy.spin()