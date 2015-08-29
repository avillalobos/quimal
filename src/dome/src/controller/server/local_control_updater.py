#/usr/bin/python

import RPi.GPIO as GPIO
import rospy


class LocalRemotePublisher(SuperController):
	def __init__(self):
		super(SuperController,self).__init__("arduino")
		self.LOCAL_REMOTE_PIN=23
		GPIO.setmode(GPIO.BMC)
		GPIO.setup(LOCAL_REMOTE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		rospy.init_node('ROOF_LocalControl_publisher')
		self.pub = rospy.Publisher('dome/mode', String, queue_size=100)
		GPIO.add_event_detect(self.LOCAL_REMOTE_PIN, GPIO.RISING, callback=self.local_mode_activated, bouncetime=300)
		GPIO.add_event_detect(self.LOCAL_REMOTE_PIN, GPIO.FALLING, callback=self.remote_mode_activated, bouncetime=300)

	def createRoofMSG(self,action,status, sensor1, sensor2, sensor3, ubication):
		roof_msg = roof()
		roof_msg.ubication = ubication
		roof_msg.sensor1 = True
 		roof_msg.sensor2 = False
		roof_msg.sensor3 = True
		roof_msg.state = status
		roof_msg.action = action
		return roof_msg

	def local_mode_activated(self,channel):
		rospy.loginfo("Control has been changed to LOCAL MODE ONLY, please acknoledge locally to come back to remote.")
		self.pub.publish("LOCAL")
	
	def remote_mode_activated(self,channel):
		rospy.loginfo("Control has been changed to REMOTE MODE")
		self.pub.publish("REMOTE")
