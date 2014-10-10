#!/usr/bin/python

import sys, os
sys.path.append(os.path.abspath((os.path.dirname(__file__) + "/../../controller/")))
#from dome_controller import open_dome, close_dome
import controller as controller

import rospy
from dome.srv import *
from dome.msg import *

def open_dome():
	speed = int(raw_input("Set velocity "))
	roof_msg = controller.open_dome(speed)
	print roof_msg

def close_dome():
	speed = int(raw_input("Set velocity "))
	roof_msg = controller.close_dome(speed)
	print roof_msg

def print_menu():
	print ""
	print "1) Open dome"
	print "2) Close dome"

if __name__ == "__main__":
	rospy.init_node("dome_controller_client")
	flag = True
	while flag:
		print_menu()
		action = int(raw_input("Select action "))
		if action == 1:
			open_dome()
		elif action == 2:
			close_dome()
		else:
			flag = False
