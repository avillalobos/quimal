#!/usr/bin/python

# -*- coding: utf-8 -*-

from dome.srv import *
from dome.msg import *
from threading import Thread
from sensor_table_model import SensorTableModel
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt, QTimer
from sensor_msgs.msg import CompressedImage

import datetime
import cv2
import numpy as np
import dome_controller_UI 
import sys, os
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
		rospy.Subscriber("/camera/image/compressed", CompressedImage, self.image_callback,  queue_size = 1)
	
		self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
		self.dateEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())

		self.timer = QTimer(self)
		self.timer.timeout.connect(self._get_new_image)
		self.timer.start(1000)

		self.clock_timer = QTimer(self)
		self.clock_timer.timeout.connect(self.update_lcd_time)
		self.clock_timer.start(1000)

	def create_tableview(self):
		self.sensor_display = SensorTableModel(5,3,self.centralwidget)
		self.sensor_display.setDragDropOverwriteMode(False)
		self.sensor_display.setGeometry(QtCore.QRect(460, 120, 431, 361))
		self.sensor_display.setObjectName(_fromUtf8("sensor_display"))


	def update_lcd_time(self):
		#time = QtCore.QTime.currentTime()
		#text = time.toString('hh:mm:ss')
		utc_time = datetime.datetime.utcnow()
		text = utc_time.strftime("%H:%M:%S")
		self.lcd_local_time.display(text)
		self.lcd_sideral_time.display(text)

	def updateSensorStatus(self, data):
		self.sensor_display.updateSensorData("Sensor 1", "Warning", data.ubication)
		self.sensor_display.updateSensorData("Sensor 2", "Critical", data.state)
		self.sensor_display.updateSensorData("Sensor 3", "Ok", data.sensor1)
		
	def threaded_open_dome(self, empty):
		print "opening"
		roof_msg = controller.open_dome(speed=1)
		if self.StartStop == True:
			self.LogMonitor.appendPlainText("==================================")
			self.LogMonitor.appendPlainText(str(roof_msg))
			self.LogMonitor.moveCursor(QtGui.QTextCursor.End)


	def open_dome(self):
		thread = Thread(target = self.threaded_open_dome , args = (self,))
		thread.start()

	def threaded_close_dome(self, empty):
		roof_msg = controller.close_dome(speed=1)
		if self.StartStop == True:
			self.LogMonitor.appendPlainText("==================================")
			self.LogMonitor.appendPlainText(str(roof_msg))
			self.LogMonitor.moveCursor(QtGui.QTextCursor.End)

	def close_dome(self):
		thread = Thread(target = self.threaded_close_dome , args = (self,))
		thread.start()

	def threaded_emergency_stop(self, empty):
		roof_msg = controller.emergency_stop()
		if self.StartStop == True:
			self.LogMonitor.appendPlainText("==================================")
			self.LogMonitor.appendPlainText(str(roof_msg))
			self.LogMonitor.moveCursor(QtGui.QTextCursor.End)

	def emergency_stop(self):
		thread = Thread(target = self.threaded_emergency_stop , args = (self,))
		thread.start()
	
	def log_function(self):
		self.StartStop = not self.StartStop
		if self.StartStop == True:
			self.Start_Stop.setText(_translate("TCS_Main_Panel", "Start!", None))
		else:
			self.Start_Stop.setText(_translate("TCS_Main_Panel", "Stop!", None))

	def _get_new_image(self):
		if self.image_data != None:
			myPixmap = QtGui.QPixmap(QtGui.QImage.fromData(self.image_data))
			myScaledPixmap = myPixmap.scaled(self.camera_view.size(), QtCore.Qt.KeepAspectRatio)
			self.camera_view.setPixmap(myScaledPixmap)

	def image_callback(self, ros_data):
		#### direct conversion to CV2 ####
		np_arr = np.fromstring(ros_data.data, np.uint8)
		image_np = cv2.imdecode(np_arr, cv2.CV_LOAD_IMAGE_COLOR)
		self.image_data = np_arr

	def generate_log(self):
		print self.sensor_display.getSelectedItems()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = GUI_TCS_Main_Panel()
	myapp.show()
	sys.exit(app.exec_())
