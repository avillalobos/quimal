#!/usr/bin/python

from dome.srv import *
from dome.msg import roof
import rospy, time, serial, os.path, sys
from super_controller import SuperController
from subprocess import call, check_output
from std_msgs.msg import String

class DomeController(SuperController):
	
	def __init__(self):
		self.roof_status = None
		rospy.init_node('RaspberryPI_ROOF_Controller')
		super(DomeController,self).__init__(None)
		self.pub = rospy.Publisher('dome/roof/status', roof, queue_size=100)
		rospy.Subscriber("dome/roof/status", roof, self.callback)
		self.mode = "REMOTE"
		rospy.Subscriber("dome/mode", String, self.updateMode)
		# useful only on Raspberry PI connected to Arduino
		self.status_pin = 18
		self.open_pin = 19
		self.close_pin = 20
		self.opening_sensor_pin = 21
		self.closing_sensor_pin = 22
		self.safety_sensor = 23
		self.PIN_LIST={"open_button":self.open_pin, # 1
					"close_button":self.close_pin, # 2
					"opening_sensor":self.opening_sensor_pin, # 4
					"closing_sensor":self.closing_sensor_pin, # 8
					"safety_sensor":self.safety_sensor} # 16
		roof_initial_msg = self.getInitialState()
		self.last_roof_status = None
		self.status = ""
		while self.roof_status == None:
			rospy.loginfo("waiting to store first message of roof status")
			self.pub.publish(roof_initial_msg)
			time.sleep(1)
	
#=================================================================================================
# UTILS
#=================================================================================================

	def createRoofMSG(self,msgs_list):
		roof_msg = roof()
		roof_msg.open_button = True if self.readPinValue(self.open_pin) == 1 else False
		roof_msg.close_button = True if self.readPinValue(self.close_pin) == 1 else False
		roof_msg.opening_sensor = True if self.readPinValue(self.opening_sensor_pin) else False
		roof_msg.closing_sensor = True if self.readPinValue(self.closing_sensor_pin) else False
		roof_msg.safety_sensor = True if self.mode == "LOCAL" else False
		roof_msg.meteorologic_sensor = True # TODO: Must be implemented or deleted
		roof_msg.state = msgs_list["status"]
		roof_msg.action = msgs_list["action"]
		return roof_msg

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

	# this function must check all the pins being used in the Raspberry PI to control the dome
	def getInitialState(self):
		msg = self.readRasperryStatus()
		roof_initial_msg = self.createRoofMSG(msg)
		return roof_initial_msg
		# check pin open_button
		# check pin close_button
		# check pin opening sensor
		# check pin closing sensor
		# check safety sensor
		# check meteorologic sensor
		# determine state 
		# determine action being performed

	def highPin(self, pin_number):
		if os.path.exists("/sys/class/gpio"):
			cmd = "echo 1 > /sys/class/gpio/gpio"+str(pin_number)+"/value"
			call( [cmd], shell=True  )
			rospy.loginfo("Activated pin: " + str(pin_number)+ " on Raspberry PI")
		else:
			rospy.loginfo("There is no GPIO directory, so probably this is not a Raspberry PI, so that activate a pin is not available")

	def lowPin(self, pin_number):
		if os.path.exists("/sys/class/gpio"):
			cmd = "echo 0 > /sys/class/gpio/gpio"+str(pin_number)+"/value"
			call( [cmd], shell=True  )
			rospy.loginfo("Activated pin: " + str(pin_number)+ " on Raspberry PI")
		else:
			rospy.loginfo("There is no GPIO directory, so probably this is not a Raspberry PI, so that activate a pin is not available")
				
	def readPinValue(self,pin_number):
		if os.path.exists("/sys/class/gpio"):
			result = check_output(["cat","/sys/class/gpio/gpio"+str(pin_number)+"/value"])
			return int(result)
		else:
			rospy.loginfo("There is no GPIO directory, so probably this is not a Raspberry PI, so that activate a pin is not available")
			return -1
	
	def readRasperryStatus(self):
		msgs_list = dict()
		# This will iterate ober all the pins and will retrieve the value of each one
		state_value = 0
		shifter = 0
		for k,v in self.PIN_LIST.iteritems():
			value = self.readPinValue(v)
			msgs_list[k] = value
			state_value = state_value | value << shifter
			shifter += 1
		
		if state_value == 0:
			msgs_list["status"] = self.STATES["STOP"]
		elif state_value == 5:
			msgs_list["status"] = self.STATES["OPEN"]
		elif state_value == 1:
			# cuando se activa el sensor de final de carrera de la apertura
			# entonces se ha terminado de abrir, si solo esta activado el pin
			# de apertura, entonces aun esta solo abriendo.
			msgs_list["status"] = self.STATES["OPENING"]
		elif state_value == 10:
			msgs_list["status"] = self.STATES["CLOSE"]
			# cuando se activa el sensor de final de carrera de la apertura
			# entonces se ha terminado de abrir, si solo esta activado el pin
			# de apertura, entonces aun esta solo abriendo.			
		elif state_value == 2:
			msgs_list["status"] = self.STATES["CLOSING"]
		else:
			msgs_list["status"] = "UNKNOWN"
		
		msgs_list["meteorologic_sensor"] = False;
		msgs_list["action"] = "FIXED"
		
		return msgs_list

#=================================================================================================
# CORE
#=================================================================================================

	# perform the actions to open the dome
	def action_open(self):
		roof_msg = roof()
		# STARTING
		# OPENING
		self.highPin(self.open_pin)
		msg = self.readRasperryStatus()
		while msg["status"] != "OPEN" and msg["status"] != "ABORTED":
			if self.roof_status.state != self.STATES["EMERGENCY_STOP"]:
				roof_msg = self.createRoofMSG(msg)
				self.pub.publish(roof_msg)
				self.rate.sleep()
			else:
				rospy.logwarn("Due an Emergency stop message, the opening of the dome has been stopped!")
				emergency_stop = True
				break;
			msg = self.readRasperryStatus()

		rospy.loginfo("Roof status: " + msg["status"])
		if emergency_stop == False:
		# getting the last message
			msg = msg = self.readRasperryStatus()
			rospy.loginfo("Roof final state = [action performed: OPENING | status:" + msg["status"] +" ]")
		else:
			rospy.logwarn("Executing emergency stop")
		return roof_msg
	
	# perform the actions to close the dome
	def action_close_dome(self):
		roof_msg = roof()
		# STARTING
		# OPENING
		self.highPin(self.open_pin)
		msg = self.readRasperryStatus()
		while msg["status"] != "CLOSE" and msg["status"] != "ABORTED":
			if self.roof_status.state != self.STATES["EMERGENCY_STOP"]:
				roof_msg = self.createRoofMSG(msg)
				self.pub.publish(roof_msg)
				self.rate.sleep()
			else:
				rospy.logwarn("Due an Emergency stop message, the close of the dome has been stopped!")
				emergency_stop = True
				break;
			msg = self.readRasperryStatus()
			
		rospy.loginfo("Roof status: " + msg["status"])
		if emergency_stop == False:
		# getting the last message
			msg = msg = self.readRasperryStatus()
			rospy.loginfo("Roof final state = [action performed: OPENING | status:" + msg["status"] +" ]")
		else:
			rospy.logwarn("Executing emergency stop")
		return roof_msg
	
	# perform the actions to open the dome
	def handle_refresh_dome_status(self,req):
		rospy.loginfo("A new request of refresh have been received" + str(req))
		msg = msg = self.readRasperryStatus()
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