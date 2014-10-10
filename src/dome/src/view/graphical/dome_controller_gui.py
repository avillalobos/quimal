#!/usr/bin/python

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tcs_gui.ui'
#
# Created: Fri Oct 10 00:05:27 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, os
sys.path.append(os.path.abspath((os.path.dirname(__file__) + "/../../controller/")))
import controller as controller

import rospy
from dome.srv import *
from dome.msg import *

from threading import Thread

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

class Ui_TCS_Main_Panel(QtGui.QMainWindow):

	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setupUi(self)
		self.StartStop = True
		rospy.init_node("dome_controller_client")

	def setupUi(self, TCS_Main_Panel):
		TCS_Main_Panel.setObjectName(_fromUtf8("TCS_Main_Panel"))
		TCS_Main_Panel.resize(800, 600)
		self.centralwidget = QtGui.QWidget(TCS_Main_Panel)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.Start_Stop = QtGui.QPushButton(self.centralwidget)
		self.Start_Stop.setGeometry(QtCore.QRect(700, 520, 94, 24))
		self.Start_Stop.setObjectName(_fromUtf8("Start_Stop"))
		self.LogMonitor = QtGui.QPlainTextEdit(self.centralwidget)
		self.LogMonitor.setGeometry(QtCore.QRect(0, 490, 701, 76))
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.LogMonitor.sizePolicy().hasHeightForWidth())
		self.LogMonitor.setSizePolicy(sizePolicy)
		self.LogMonitor.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.LogMonitor.setReadOnly(True)
		self.LogMonitor.setObjectName(_fromUtf8("LogMonitor"))
		self.open_dome_btn = QtGui.QPushButton(self.centralwidget)
		self.open_dome_btn.setGeometry(QtCore.QRect(690, 10, 94, 24))
		self.open_dome_btn.setObjectName(_fromUtf8("open_dome_btn"))
		self.close_dome_btn = QtGui.QPushButton(self.centralwidget)
		self.close_dome_btn.setGeometry(QtCore.QRect(690, 40, 94, 24))
		self.close_dome_btn.setObjectName(_fromUtf8("close_dome_btn"))
		self.emergency_stop_btn = QtGui.QPushButton(self.centralwidget)
		self.emergency_stop_btn.setGeometry(QtCore.QRect(673, 70, 111, 51))
		self.emergency_stop_btn.setObjectName(_fromUtf8("emergency_stop_btn"))
		TCS_Main_Panel.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(TCS_Main_Panel)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		TCS_Main_Panel.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(TCS_Main_Panel)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		TCS_Main_Panel.setStatusBar(self.statusbar)
        
		self.retranslateUi(TCS_Main_Panel)
		QtCore.QObject.connect(self.open_dome_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), TCS_Main_Panel.open_dome)
		QtCore.QObject.connect(self.close_dome_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), TCS_Main_Panel.close_dome)
		QtCore.QObject.connect(self.emergency_stop_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), TCS_Main_Panel.emergency_stop)
		QtCore.QObject.connect(self.Start_Stop, QtCore.SIGNAL(_fromUtf8("clicked()")), TCS_Main_Panel.log_function)
		QtCore.QMetaObject.connectSlotsByName(TCS_Main_Panel)

	def retranslateUi(self, TCS_Main_Panel):
		
		TCS_Main_Panel.setWindowTitle(_translate("TCS_Main_Panel", "MainWindow", None))
		self.Start_Stop.setText(_translate("TCS_Main_Panel", "Stop!", None))
		self.open_dome_btn.setText(_translate("TCS_Main_Panel", "Open Dome", None))
		self.close_dome_btn.setText(_translate("TCS_Main_Panel", "Close Dome", None))
		self.emergency_stop_btn.setText(_translate("TCS_Main_Panel", "Emergency Stop!", None))

	def threaded_open_dome(self, empty):
		roof_msg = controller.open_dome(speed=1)
		if self.StartStop == True:
			self.LogMonitor.appendPlainText("==================================")
			self.LogMonitor.appendPlainText(str(roof_msg))

	def open_dome(self):
		thread = Thread(target = self.threaded_open_dome , args = (self,))
		thread.start()

	def threaded_close_dome(self, empty):
		roof_msg = controller.close_dome(speed=1)
		if self.StartStop == True:
			self.LogMonitor.appendPlainText("==================================")
			self.LogMonitor.appendPlainText(str(roof_msg))

	def close_dome(self):
		thread = Thread(target = self.threaded_close_dome , args = (self,))
		thread.start()

	def threaded_emergency_stop(self, empty):
		roof_msg = controller.emergency_stop()
		if self.StartStop == True:
			self.LogMonitor.appendPlainText("==================================")
			self.LogMonitor.appendPlainText(str(roof_msg))

	def emergency_stop(self):
		thread = Thread(target = self.threaded_emergency_stop , args = (self,))
		thread.start()
	
	def log_function(self):
		self.StartStop = not self.StartStop
		if self.StartStop == True:
			self.Start_Stop.setText(_translate("TCS_Main_Panel", "Start!", None))
		else:
			self.Start_Stop.setText(_translate("TCS_Main_Panel", "Stop!", None))

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = Ui_TCS_Main_Panel()
	myapp.show()
	sys.exit(app.exec_())
