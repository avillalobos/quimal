#!/usr/bin/python

# -*- coding: utf-8 -*-

from dome.srv import *
from dome.msg import *
from threading import Thread
from sensor_table_model import SensorTableModel
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt, QTimer
#from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
from std_msgs.msg import String

import datetime
import cv2
import numpy as np
import dome_controller_UI 
import sys, os
from math import pi as PI
sys.path.append(os.path.abspath((os.path.dirname(__file__) + "/../../controller/")))
import controller as controller
import rospy

try:
        _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
        def _fromUtf8(s):
                return s

try:
        _encoding = QtGui.QApplication.UnicodeUTF8
        def _translate(context, text, disambig):
                return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
        def _translate(context, text, disambig):
                return QtGui.QApplication.translate(context, text, disambig)

image_data = None

class GUI_TCS_Main_Panel(QtGui.QMainWindow, dome_controller_UI.Ui_TCS_Main_Panel):

	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self)
		super(GUI_TCS_Main_Panel, self).__init__(parent)
		self.setupUi(self)
		self.create_tableview()
		self.StartStop = True
		rospy.init_node("dome_controller_client")
		rospy.Subscriber("dome/roof/status", roof, self.updateSensorStatus)
		self.image_data = None
		rospy.Subscriber("camera", Image, self.image_callback,  queue_size = 5)
		rospy.Subscriber("dome/mode", String, self.updateMode)
		
		self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
		self.dateEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())

		self.timer = QTimer(self)
		self.timer.timeout.connect(self._get_new_image)
		self.timer.start(1000)

		self.clock_timer = QTimer(self)
		self.clock_timer.timeout.connect(self.update_lcd_time)
		self.clock_timer.start(1000)
	
		# i'm using as reference UT3 @ Paranal Observatory
		deg = 70
		minutes = 24
		seconds = 9.896
		self.longitude = -(deg + minutes / 60 + seconds / 3600) * (PI/180.0)

	def create_tableview(self):
		self.sensor_display = SensorTableModel(7,3,self.centralwidget)
		self.sensor_display.setDragDropOverwriteMode(False)
		self.sensor_display.setGeometry(QtCore.QRect(460, 120, 431, 361))
		self.sensor_display.setObjectName(_fromUtf8("sensor_display"))


	def update_lcd_time(self):
		#time = QtCore.QTime.currentTime()
		#text = time.toString('hh:mm:ss')
		utc_time = datetime.datetime.utcnow()
		text = utc_time.strftime("%H:%M:%S")
		self.lcd_local_time.display(text)
		
		self.lcd_sideral_time.display(controller.getSiderealTime(self.longitude))

	def updateSensorStatus(self, data):
		#TODO usar los valores para determinar si el estado esta bien o mal
		self.sensor_display.updateSensorData("Ubication", "0", data.ubication)
		
		if data.open_button and data.state != "REMOTE":
			self.sensor_display.updateSensorData("Open Button", "Critical", data.open_button)
		else:
			self.sensor_display.updateSensorData("Open Button", "Ok", data.open_button)
		
		if data.close_button and data.state != "REMOTE":
			self.sensor_display.updateSensorData("Close Button", "Critical", data.close_button)
		else:
			self.sensor_display.updateSensorData("Close Button", "0", data.close_button)
		
		
		self.sensor_display.updateSensorData("Opening Sensor", "Ok", data.opening_sensor)
		self.sensor_display.updateSensorData("Closing Sensor", "Ok", data.closing_sensor)
		self.sensor_display.updateSensorData("Safety Sensor", "Ok", data.safety_sensor)
		self.sensor_display.updateSensorData("Meteorologic Sensor", "Ok", data.meteorologic_sensor)
		self.lbl_status.setText(data.state)
		self.lbl_next_action.setText(data.action)

	def updateMode(self,data):
		self.lbl_mode.setText(data.data)

	def open_dome(self):
		thread = Thread(target = self.threaded_open_dome , args = (self,))
		thread.start()		

	def threaded_open_dome(self, empty):
		print "opening"
		roof_msg = controller.open_dome(speed=1)
		if self.StartStop == True:
			self.LogMonitor.appendPlainText("==================================")
			self.LogMonitor.appendPlainText(str(roof_msg))
			self.LogMonitor.moveCursor(QtGui.QTextCursor.End)

	def close_dome(self):
		thread = Thread(target = self.threaded_close_dome , args = (self,))
		thread.start()

	def threaded_close_dome(self, empty):
		roof_msg = controller.close_dome(speed=1)
		if self.StartStop == True:
			self.LogMonitor.appendPlainText("==================================")
			self.LogMonitor.appendPlainText(str(roof_msg))
			self.LogMonitor.moveCursor(QtGui.QTextCursor.End)

	def emergency_stop(self):
		thread = Thread(target = self.threaded_emergency_stop , args = (self,))
		thread.start()

	def threaded_emergency_stop(self, empty):
		roof_msg = controller.emergency_stop()
		if self.StartStop == True:
			self.LogMonitor.appendPlainText("==================================")
			self.LogMonitor.appendPlainText(str(roof_msg))
			self.LogMonitor.moveCursor(QtGui.QTextCursor.End)

	def refresh_dome_status(self):
		thread = Thread(target = self.threaded_refresh_dome_status , args = (self,))
		thread.start()		

	def threaded_refresh_dome_status(self, empy):
		print "Refreshing dome status"
		roof_msg = controller.refresh_dome_status()
		if self.StartStop == True:
			self.LogMonitor.appendPlainText("==================================")
			self.LogMonitor.appendPlainText(str(roof_msg))
			self.LogMonitor.moveCursor(QtGui.QTextCursor.End)

	def log_function(self):
		self.StartStop = not self.StartStop
		if self.StartStop == True:
			self.Start_Stop.setText(_translate("TCS_Main_Panel", "Start!", None))
		else:
			self.Start_Stop.setText(_translate("TCS_Main_Panel", "Stop!", None))

	def _get_new_image(self):
		if self.image_data != None:
			qimage = QtGui.QImage(self.image_data,640,480, QtGui.QImage.Format_RGB888)
			myPixmap = QtGui.QPixmap(qimage)
			if myPixmap != None and not myPixmap.isNull(): 
				myScaledPixmap = myPixmap.scaled(self.camera_view.size(), QtCore.Qt.KeepAspectRatio)
				print myScaledPixmap
				if myScaledPixmap != None:
					self.camera_view.setPixmap(myScaledPixmap)

	def image_callback(self, ros_data):
		#print "image received", ros_data
		#### direct conversion to CV2 ####
		np_arr = np.fromstring(str(ros_data.data), np.uint8)
		self.image_data = np_arr

	def generate_log(self):
		print self.sensor_display.getSelectedItems()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = GUI_TCS_Main_Panel()
	myapp.show()
	sys.exit(app.exec_())
