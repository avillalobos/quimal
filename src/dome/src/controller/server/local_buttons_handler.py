#!/usr/bin/python
# The main objective of this file is handle the events received from the Arduino and Local Buttons
# using the GPIO library available for python

import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import String

GPIO.setmode(GPIO.BOARD) # using the numbers of the pin like is being used on the board

# We will use the ping #18 of the board of the RPi for communication with the physical environment. So buttons
# will inform to pin 18 or the RPi when they are as local (HIGH) or remote (LOW)
local_remote_channel = 18
GPIO.setup(local_remote_channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
pub = rospy.Publisher('dome/mode', String, queue_size=100)
rospy.init_node('LocalRemoteHandler')

rospy.loginfo("Starting LocalRemote handler")

def publish_set_to_local():
	rospy.logwarn("Control has been transferred to LOCAL CONTROL ONLY!")
	pub.publish("LOCAL")

def publish_set_to_remote():
	rospy.logwarn("Control has been transferred to REMOTE CONTROL")
	pub.publish("REMOTE")

GPIO.add_event_detect(local_remote_channel, GPIO.RISING, callback=publish_set_to_local, bouncetime=200)
GPIO.add_event_detect(local_remote_channel, GPIO.FALLING, callback=publish_set_to_remote, bouncetime=200)