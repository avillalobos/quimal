#!/usr/bin/python

from dome.srv import *
from dome.msg import roof
import rospy, time, serial

class DomeController:

	def __init__(self):
		self.pub = rospy.Publisher('dome/roof/status', roof, queue_size=100)
		rospy.init_node('ROOF_Controller')
		self.STATES=["PREPARING","STARTING","OPENING","OPEN", "CLOSING", "PARKING", "PARKED", "CLOSED","FINISH", "EMERGENCY_STOP"]
		roof_initial_msg = self.getInitialState()
		self.roof_status = None
		self.last_roof_status = None
		rospy.Subscriber("dome/roof/status", roof, self.callback)
		while self.roof_status == None:
			rospy.loginfo("waiting to store first message of roof status")
			self.pub.publish(roof_initial_msg)
			time.sleep(1)
		# TODO fix this part to match with the corresponding arduino and fixing the timeout
		self.arduino = serial.Serial("/dev/ttyACM0", timeout=30)

	# this code must be programated with the electronics and mechanical team.
	def getInitialState(self):
		roof_initial_msg = roof()
		roof_initial_msg.ubication = 0
		roof_initial_msg.sensor1 = False
		roof_initial_msg.sensor2 = False
		roof_initial_msg.sensor3 = False
		roof_initial_msg.state = self.STATES[7]
		self.pub.publish(roof_initial_msg)
		return roof_initial_msg
	
	def readLineFromArduino(self):
		msg = ""
		b = self.arduino.read()
		while b != "#":
			msg = msg + b
			b = self.arduino.read()
		return msg

	def createRoofMSG(self,action,status, sensor1, sensor2, sensor3, ubication):
		roof_msg = roof()
		roof_msg.ubication = ubication
		roof_msg.sensor1 = True
		roof_msg.sensor2 = False
 		roof_msg.sensor3 = True
 		roof_msg.state = status
		roof_msg.action = action
		return roof_msg

	# Callback to receive the status of the Dome at any time
	def callback(self, data):
		if data.state == self.STATES[9]:
			rospy.logwarn("RECEIVED AN EMERGENCY STOP!, DOME WILL STOP AS SOON AS POSSIBLE!")
		else:
			rospy.loginfo("received new status: " + str(data.state))
		self.last_roof_status = self.roof_status
		self.roof_status = data

	# Handler registered when the open service is requested
	def handle_open(self,req):
		#print "TCS is requesting to open roof at speed: ", req.speed
		rospy.loginfo("TCS is requesting to open roof at speed: " + str(req.speed))
		if self.roof_status.state == self.STATES[7] or self.roof_status.state == self.STATES[8]:
			if self.roof_status.state == self.STATES[8]: self.roof_status = self.last_roof_status
			# wait until action is completed
			lateral_door_msg = self.action_open_lateral_door()
			rospy.loginfo(lateral_door_msg)
			roof_msg = self.action_open_dome()
			return roof_msg
		else:
			roof_msg = roof()
			roof_msg.state = "Not possible to open due roof is in another state: " + self.roof_status.state
			rospy.logwarn(roof_msg.state)
			return roof_msg

	# perform the actions to open the dome
	def action_open_dome(self):
		roof_msg = roof()
		msg = self.arduino.write("openDome")
		msg = self.readLineFromArduino()
		while msg != "FINISH":
			if self.roof_status.state != self.STATES[9]:
				roof_msg = self.createRoofMSG("openDome",msg,True,False,True,1)
				self.pub.publish(roof_msg)
				rospy.loginfo(msg)
				# This frequency should be modified once the hardware is connected
				r = rospy.Rate(0.5)
				r.sleep()
			else:
				rospy.logwarn("Due an Emergency stop message, the opening of the dome has been stopped!")
				break;
			msg = self.readLineFromArduino()
		
		rospy.loginfo("Roof status: " + msg)
		# getting the last message
		msg = self.readLineFromArduino()	
		rospy.loginfo("Roof final state: " + msg)
		return roof_msg

	def action_open_lateral_door(self):
		roof_msg = roof()
		msg = self.arduino.write("openLateralDoor")
		msg = self.readLineFromArduino()
		while msg != "FINISH":
			if self.roof_status.state != self.STATES[9]:
				roof_msg = self.createRoofMSG("openLateralDoor",msg,True,False,True,1)
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

	# Handler registered when the close service is requested
	def handle_close(self,req):
		rospy.loginfo("TCS is requesting to close roof at speed: " + str(req.speed))
		#print "TCS is requesting to close roof at speed: ", req.speed
		if self.roof_status.state == self.STATES[3] or self.roof_status.state == self.STATES[8]:
			if self.roof_status.state == self.STATES[8]: self.roof_status = self.last_roof_status
			lateral_door_msg = self.action_close_lateral_door()
			rospy.loginfo(lateral_door_msg)
			roof_msg = self.action_close_dome()
			return roof_msg
		else:
			roof_msg = roof()
			roof_msg.state = "Not possible to close due roof is in another state: " + self.roof_status.state
			rospy.logwarn(roof_msg.state)
			return roof_msg


	# perform the actions to close the dome
	def action_close_dome(self):
		msg = self.arduino.write("closeDome")
		msg = self.readLineFromArduino()
		while msg != "FINISH":
			if self.roof_status.state != self.STATES[8]:
				roof_msg = self.createRoofMSG("closeDome",msg,False,True,False,1)
				self.pub.publish(roof_msg)
				r = rospy.Rate(0.5) # 10hz
				r.sleep()
			else:
				rospy.logwarn("Due an Emergency stop message, the close of the dome has been stopped!")
				break;
			msg = self.readLineFromArduino()

		rospy.loginfo("Roof status: " + msg)
		# getting the last message
		msg = self.readLineFromArduino()	
		rospy.loginfo("Roof final state: " + msg)
		return roof_msg

	def action_close_lateral_door(self):
		roof_msg = roof()
		msg = self.arduino.write("closeLateralDoor")
		msg = self.readLineFromArduino()
		while msg != "FINISH":
			if self.roof_status.state != self.STATES[9]:
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

	# Starte the server to answer the different services handled	
	def server(self):
		s1 = rospy.Service('open_dome', open_dome, self.handle_open)
		s2 = rospy.Service('close_dome', close_dome, self.handle_close)
		rospy.loginfo("ready to go!.")
		rospy.spin()

if __name__ == "__main__":
	dome_controller = DomeController()
	dome_controller.server()
