# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tcs_gui.ui'
#
# Created: Wed Nov  5 17:00:01 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_TCS_Main_Panel(object):
    def setupUi(self, TCS_Main_Panel):
        TCS_Main_Panel.setObjectName(_fromUtf8("TCS_Main_Panel"))
        TCS_Main_Panel.resize(901, 628)
        self.centralwidget = QtGui.QWidget(TCS_Main_Panel)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Start_Stop = QtGui.QPushButton(self.centralwidget)
        self.Start_Stop.setGeometry(QtCore.QRect(800, 520, 94, 24))
        self.Start_Stop.setObjectName(_fromUtf8("Start_Stop"))
        self.LogMonitor = QtGui.QPlainTextEdit(self.centralwidget)
        self.LogMonitor.setGeometry(QtCore.QRect(0, 490, 801, 101))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LogMonitor.sizePolicy().hasHeightForWidth())
        self.LogMonitor.setSizePolicy(sizePolicy)
        self.LogMonitor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LogMonitor.setReadOnly(True)
        self.LogMonitor.setObjectName(_fromUtf8("LogMonitor"))
        self.open_dome_btn = QtGui.QPushButton(self.centralwidget)
        self.open_dome_btn.setGeometry(QtCore.QRect(800, 10, 94, 24))
        self.open_dome_btn.setObjectName(_fromUtf8("open_dome_btn"))
        self.close_dome_btn = QtGui.QPushButton(self.centralwidget)
        self.close_dome_btn.setGeometry(QtCore.QRect(800, 40, 94, 24))
        self.close_dome_btn.setObjectName(_fromUtf8("close_dome_btn"))
        self.emergency_stop_btn = QtGui.QPushButton(self.centralwidget)
        self.emergency_stop_btn.setGeometry(QtCore.QRect(783, 70, 111, 51))
        self.emergency_stop_btn.setObjectName(_fromUtf8("emergency_stop_btn"))
        self.sensor_display = QtGui.QTableView(self.centralwidget)
        self.sensor_display.setGeometry(QtCore.QRect(460, 120, 431, 361))
        self.sensor_display.setDragDropOverwriteMode(False)
        self.sensor_display.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.sensor_display.setObjectName(_fromUtf8("sensor_display"))
        self.camera_view = QtGui.QLabel(self.centralwidget)
        self.camera_view.setGeometry(QtCore.QRect(30, 40, 400, 400))
        self.camera_view.setObjectName(_fromUtf8("camera_view"))
        TCS_Main_Panel.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(TCS_Main_Panel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 901, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        TCS_Main_Panel.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(TCS_Main_Panel)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        TCS_Main_Panel.setStatusBar(self.statusbar)

        self.retranslateUi(TCS_Main_Panel)
        QtCore.QObject.connect(self.open_dome_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), TCS_Main_Panel.open_dome)
        QtCore.QObject.connect(self.close_dome_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), TCS_Main_Panel.close_dome)
        QtCore.QObject.connect(self.emergency_stop_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), TCS_Main_Panel.emergency_stop)
        QtCore.QMetaObject.connectSlotsByName(TCS_Main_Panel)

    def retranslateUi(self, TCS_Main_Panel):
        TCS_Main_Panel.setWindowTitle(_translate("TCS_Main_Panel", "MainWindow", None))
        self.Start_Stop.setText(_translate("TCS_Main_Panel", "PushButton", None))
        self.open_dome_btn.setText(_translate("TCS_Main_Panel", "Open Dome", None))
        self.close_dome_btn.setText(_translate("TCS_Main_Panel", "Close Dome", None))
        self.emergency_stop_btn.setText(_translate("TCS_Main_Panel", "Emergency Stop!", None))
        self.camera_view.setText(_translate("TCS_Main_Panel", "TextLabel", None))

