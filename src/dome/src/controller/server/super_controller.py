# This is an abstract class to gather all the recurrent functionalities
import rospy, time, serial, os.path
from subprocess import call

class SuperController(object):
	def __init__(self, arduino_name):
		self.arduino = serial.Serial("/dev/"+str(arduino_name), timeout=30,baudrate=115200)
		# useful only on Raspberry PI
		self.status_pin = 18
		self.STATES={"PREPARING":"PREPARING","STARTING":"STARTING","OPENING":"OPENING","OPEN":"OPEN", "CLOSING":"CLOSING", "PARKING":"PARKING", "PARKED":"PARKED", "CLOSED":"CLOSED", "FINISH":"FINISH", "ABORTED":"ABORTED", "STOPPING":"STOPPING", "STOP":"STOP", "EMERGENCY_STOP":"EMERGENCY_STOP"}
		self.rate = rospy.Rate(10)
		self.data_from_arduino = ["open_button", "close_button", "opening_sensor", "closing_sensor", "safety_sensor", "meteorologic_sensor","action", "status"]

#=================================================================================================
# UTILS
#=================================================================================================

	def readLineFromArduino(self):
		msg = ""
		b = self.arduino.read()
		while b != "#":
			msg = msg + b
			b = self.arduino.read()
		return msg

	def parseArduinoLecture(self,msg):
		msgs_list = msg.split("|")
		msg_dict = dict()
		index = 0
		for raw_data in msgs_list:
			msg_dict[self.data_from_arduino[index]] = raw_data
			index+=1
		return msg_dict

	def blinkGPIO(self):
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
		rospy.loginfo("Unable to handle open because this function is not implemented on the children class")
	
	# perform the actions to open some structure
	def action_open(self):
		rospy.loginfo("Unable to control opening because this function is not implemented on the children class")

	# Handler registered when the close service is requested
	def handle_close(self,req):
		rospy.loginfo("Unable to handle close because this function is not implemented on the children class")

	# perform the actions to close the dome
	def action_close(self):
		rospy.loginfo("Unable to control closing because this function is not implemented on the children class")

	# Start the server to answer the different services handled	
	def server(self):
		rospy.loginfo("Unimplemented function on the child class")
