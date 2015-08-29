# This is an abstract class to gather all the recurrent functionalities
import rospy, time, serial, os.path
from subprocess import call
from std_msgs.msg import String
from dome.msg import roof

class SuperController(object):
	# Just to make it easy, due the change on the motors, I will put a condition regarding the arduino name
	# if arduino_name is empty, then we will assume a raspberry pi based controller.
	def __init__(self, arduino_name):
		if arduino_name == "" or arduino_name == None:
			self.arduino = None
		else:
			self.arduino = serial.Serial("/dev/"+str(arduino_name), timeout=30,baudrate=115200)
		# useful only on Raspberry PI
		self.status_pin = 4 # means ping 7 of the board
		self.STATES={"PREPARING":"PREPARING","STARTING":"STARTING","OPENING":"OPENING","OPEN":"OPEN", "CLOSING":"CLOSING", "PARKING":"PARKING", "PARKED":"PARKED", "CLOSED":"CLOSED", "FINISH":"FINISH", "ABORTED":"ABORTED", "STOPPING":"STOPPING", "STOP":"STOP", "EMERGENCY_STOP":"EMERGENCY_STOP"}
		self.rate = rospy.Rate(10)
		self.data_from_arduino = ["open_button", "close_button", "opening_sensor", "closing_sensor", "safety_sensor", "meteorologic_sensor","action", "status"]
		self.mode = ""

#=================================================================================================
# UTILS
#=================================================================================================

	def readLineFromArduino(self):
		if self.arduino == None:
			rospy.logwarn("Trying to use an Arduino function on a Raspberry PI based controller")
			return None
		else:
			msg = ""
			b = self.arduino.read()
			while b != "#":
				msg = msg + b
				b = self.arduino.read()
			return msg

	def parseArduinoLecture(self,msg):
		if self.arduino == None:
			rospy.logwarn("Trying to use an Arduino function on a Raspberry PI based controller")
			return None
		else:
			msgs_list = msg.split("|")
			msg_dict = dict()
			index = 0
			for raw_data in msgs_list:
				try:
					msg_dict[self.data_from_arduino[index]] = raw_data
				except KeyError, e:
					rospy.loginfo("Key: " + str(self.data_from_arduino[index]) + "Not found")
				index+=1
			return msg_dict

	def blinkGPIO(self):
		if self.arduino == None:
			rospy.logwarn("Trying to use an Arduino function on a Raspberry PI based controller")
			return None
		else:
			if os.path.exists("/sys/class/gpio"):
				# Agregar verificaciones de seguridad
				cmd = "echo 1 > /sys/class/gpio/gpio"+str(self.status_pin)+"/value"
				call( [cmd], shell=True  )
				time.sleep(2)
				cmd = "echo 0 > /sys/class/gpio/gpio"+str(self.status_pin)+"/value"
				call( [cmd], shell=True  )
			else:
				rospy.loginfo("There is no GPIO directory, so probably this is not a Raspberry PI, so that, BlinkGPIO is unavailable, instead it will be sent a serial command to the arduino")
				self.arduino.write("status")

	def getInitialState(self):
		rospy.loginfo("Unimplemented function on the children class")

#=================================================================================================
# CORE
#=================================================================================================

	# Handler registered when the open service is requested
	def handle_open(self,req):
		rospy.loginfo("TCS is requesting to open roof at speed: " + str(req.speed))
		if self.mode == "LOCAL":
			rospy.loginfo("System is local only, so is not possible to operate it remotely")
			roof_msg = roof()
			roof_msg.state = "System is local only, so is not possible to operate it remotely"
			rospy.logwarn(roof_msg.state)
			return roof_msg
		# it is only possible to open if the status of the TCS is PARKED, CLOSED, ABORTED or STOP. If an emergency stop was pressed is because there is something or someone in danger and need to be phisically disabled.
		if self.roof_status.state == self.STATES["PARKED"] or self.roof_status.state == self.STATES["CLOSED"] or self.roof_status.state == self.STATES["ABORTED"] or self.roof_status.state == self.STATES["STOP"]:
			if self.roof_status.state == self.STATES["EMERGENCY_STOP"]: self.roof_status = self.last_roof_status
			# wait until action is completed
			roof_msg = self.action_open()
			return roof_msg
		else:
			roof_msg = roof()
			roof_msg.state = "Not possible to open due roof is in another state: " + self.roof_status.state
			rospy.logwarn(roof_msg.state)
			return roof_msg
	
	# perform the actions to open some structure
	def action_open(self):
		rospy.loginfo("Unable to control opening because this function is not implemented on the children class")

	# Handler registered when the close service is requested
	def handle_close(self,req):
		rospy.loginfo("TCS is requesting to close roof at speed: " + str(req.speed))
		if self.mode == "LOCAL":
			rospy.loginfo("System is local only, so is not possible to operate it remotely")
			roof_msg = roof()
			roof_msg.state = "System is local only, so is not possible to operate it remotely"
			rospy.logwarn(roof_msg.state)
			return roof_msg
		#print "TCS is requesting to close roof at speed: ", req.speed
		if self.roof_status.state == self.STATES["PARKED"] or self.roof_status.state == self.STATES["OPEN"] or self.roof_status.state == self.STATES["ABORTED"] or self.roof_status.state == self.STATES["STOP"]:
			#if self.roof_status.state == self.STATES[8]: self.roof_status = self.last_roof_status
			#lateral_door_msg = self.action_close_lateral_door()
			#rospy.loginfo(lateral_door_msg)
			roof_msg = self.action_close_dome()
			return roof_msg
		else:
			roof_msg = roof()
			roof_msg.state = "Not possible to close due roof is in another state: " + self.roof_status.state
			rospy.logwarn(roof_msg.state)
			return roof_msg

	# perform the actions to close the dome
	def action_close(self):
		rospy.loginfo("Unable to control closing because this function is not implemented on the children class")

	# Start the server to answer the different services handled	
	def server(self):
		rospy.loginfo("Unimplemented function on the child class")
