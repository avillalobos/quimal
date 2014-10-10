#!/usr/bin/python

from dome.srv import *
from dome.msg import roof
import rospy, time

class DomeController:

	def __init__(self):
		self.pub = rospy.Publisher('dome/roof/status', roof, queue_size=100)
		rospy.init_node('ROOF_Controller')
		self.STATES=["PREPARING","STARTING","OPENING","OPEN", "CLOSING", "PARKING", "PARKED", "CLOSED", "EMERGENCY_STOP"]
		roof_initial_msg = self.getInitialState()
		self.roof_status = None
		rospy.Subscriber("dome/roof/status", roof, self.callback)
		while self.roof_status == None:
			rospy.loginfo("waiting to store first message of roof status")
			self.pub.publish(roof_initial_msg)
			time.sleep(1)

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
	
	# Callback to receive the status of the Dome at any time
	def callback(self, data):
		if data.state == self.STATES[8]:
			rospy.logwarn("RECEIVED AN EMERGENCY STOP!, DOME WILL STOP AS SOON AS POSSIBLE!")
		else:
			rospy.loginfo("received new status: " + str(data.state))
		self.roof_status = data

	# Handler registered when the open service is requested
	def handle_open(self,req):
		#print "TCS is requesting to open roof at speed: ", req.speed
		rospy.loginfo("TCS is requesting to open roof at speed: " + str(req.speed))
		if self.roof_status.state == self.STATES[7]:
			# wait until action is completed
			roof_msg = self.action_open()
			return roof_msg
		else:
			roof_msg = roof()
			roof.state = "Not possible to open due roof is in another state: " + self.roof_status.state
			rospy.logwarn(roof.state)
			return roof_msg
	
	# perform the actions to open the dome
	def action_open(self):
		roof_msg = roof()
		for i in [0,1,2,3]:
			if self.roof_status.state != self.STATES[8]:
				roof_msg.ubication = i
				roof_msg.sensor1 = True
				roof_msg.sensor2 = False
				roof_msg.sensor3 = True
				roof_msg.state=self.STATES[i]
				self.pub.publish(roof_msg)
				# This frequency should be modified once the hardware is connected
				r = rospy.Rate(1) # 10hz
				r.sleep()
			else:
				rospy.logwarn("Due an Emergency stop message, the opening of the dome has been stopped!")
				break;
		return roof_msg

	# Handler registered when the close service is requested
	def handle_close(self,req):
		rospy.loginfo("TCS is requesting to close roof at speed: " + str(req.speed))
		#print "TCS is requesting to close roof at speed: ", req.speed
		if self.roof_status.state == self.STATES[3]:
			roof_msg = self.action_close()
			return roof_msg
		else:
			roof_msg = roof()
			roof.state = "Not possible to close due roof is in another state: " + self.roof_status.state
			rospy.logwarn(roof.state)
			return roof_msg


	# perform the actions to close the dome
	def action_close(self):
		roof_msg = roof()
		for i in [4,5,6,7]:
			if self.roof_status.state != self.STATES[8]:
				roof_msg.ubication = i
				roof_msg.sensor1 = True
				roof_msg.sensor2 = False
				roof_msg.sensor3 = True
				roof_msg.state=self.STATES[i]
				self.pub.publish(roof_msg)
				r = rospy.Rate(1) # 10hz
				r.sleep()
			else:
				rospy.logwarn("Due an Emergency stop message, the close of the dome has been stopped!")
				break;
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
