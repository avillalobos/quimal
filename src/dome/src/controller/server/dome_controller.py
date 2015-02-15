#!/usr/bin/python

from dome.srv import *
from dome.msg import roof
import rospy, time, serial, os.path
from super_controller import SuperController
from subprocess import call

class DomeController(SuperController):

#=================================================================================================

	def __init__(self):
		rospy.init_node('ROOF_Controller')
		super(DomeController,self).__init__("ttyACM0")
		self.pub = rospy.Publisher('dome/roof/status', roof, queue_size=100)
		rospy.Subscriber("dome/roof/status", roof, self.callback)
		# useful only on Raspberry PI
		self.status_pin = 18
		roof_initial_msg = self.getInitialState()
		self.roof_status = None
		self.last_roof_status = None
		while self.roof_status == None:
			rospy.loginfo("waiting to store first message of roof status")
			self.pub.publish(roof_initial_msg)
			time.sleep(1)

#=================================================================================================
# UTILS
#=================================================================================================

	def createRoofMSG(self,action,status, sensor1, sensor2, sensor3, ubication):
		roof_msg = roof()
		roof_msg.ubication = ubication
		roof_msg.sensor1 = True
		roof_msg.sensor2 = False
 		roof_msg.sensor3 = True
 		roof_msg.state = status
		roof_msg.action = action
		return roof_msg

	# this code must be programated with the electronics and mechanical team.
	def getInitialState(self):
		roof_initial_msg = roof()
		roof_initial_msg.ubication = 0
		roof_initial_msg.sensor1 = False
		roof_initial_msg.sensor2 = False
		roof_initial_msg.sensor3 = False
		# This make a change on the pin status so that the interruption will be triggered and a message will be sent by Serial port
		self.blinkGPIO()
		state = self.readLineFromArduino()
		roof_initial_msg.state = state
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

#=================================================================================================
# CORE
#=================================================================================================

	# Handler registered when the open service is requested
	def handle_open(self,req):
		rospy.loginfo("TCS is requesting to open roof at speed: " + str(req.speed))
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

	# perform the actions to open the dome
	def action_open(self):
		roof_msg = roof()
		msg = self.arduino.write("openDome")
		msg = self.readLineFromArduino()
		emergency_stop = False
		while msg != "FINISH" and msg != "ABORTED":
			if self.roof_status.state != self.STATES["EMERGENCY_STOP"]:
				roof_msg = self.createRoofMSG("openDome",msg,True,False,True,1)
				self.pub.publish(roof_msg)
				self.rate.sleep()
			else:
				rospy.logwarn("Due an Emergency stop message, the opening of the dome has been stopped!")
				emergency_stop = True
				break;
			msg = self.readLineFromArduino()	
		rospy.loginfo("Roof status: " + msg)
		if emergency_stop == False:
		# getting the last message
			msg = self.readLineFromArduino().split(":")
			rospy.loginfo("Roof final state = [action performed:" + msg[0] + " | status:" + msg[1] +" | next action:" + msg[2] + "]")
		else:
			rospy.logwarn("Executing emergency stop")
		return roof_msg

	# Handler registered when the close service is requested
	def handle_close(self,req):
		rospy.loginfo("TCS is requesting to close roof at speed: " + str(req.speed))
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
	def action_close_dome(self):
		msg = self.arduino.write("closeDome")
		msg = self.readLineFromArduino()
		emergency_stop = False
		while msg != "FINISH" and msg != "ABORTED":
			if self.roof_status.state != self.STATES["EMERGENCY_STOP"]:
				roof_msg = self.createRoofMSG("closeDome",msg,False,True,False,1)
				self.pub.publish(roof_msg)
				self.rate.sleep()
			else:
				rospy.logwarn("Due an Emergency stop message, the close of the dome has been stopped!")
				emergency_stop = True
				break;
			msg = self.readLineFromArduino()
		rospy.loginfo("Roof status: " + msg)
		if emergency_stop == False:
		# getting the last message
			msg = self.readLineFromArduino().split(":")
			rospy.loginfo("Roof final state = [action performed:" + msg[0] + " | status:" + msg[1] +" | next action:" + msg[2] + "]")
		else:
			rospy.logwarn("Executing emergency stop")
		return roof_msg

	# Start the server to answer the different services handled	
	def server(self):
		s1 = rospy.Service('open_dome', open_dome, self.handle_open)
		s2 = rospy.Service('close_dome', close_dome, self.handle_close)
		rospy.loginfo("ready to go!.")
		rospy.spin()

#=================================================================================================
# MAIN
#=================================================================================================

if __name__ == "__main__":
	dome_controller = DomeController()
	dome_controller.server()
