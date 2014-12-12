# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tcs_gui.ui'
#
# Created: Fri Nov 14 00:42:18 2014
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
        self.open_dome_btn.setGeometry(QtCore.QRect(460, 0, 94, 24))
        self.open_dome_btn.setObjectName(_fromUtf8("open_dome_btn"))
        self.close_dome_btn = QtGui.QPushButton(self.centralwidget)
        self.close_dome_btn.setGeometry(QtCore.QRect(560, 0, 94, 24))
        self.close_dome_btn.setObjectName(_fromUtf8("close_dome_btn"))
        self.emergency_stop_btn = QtGui.QPushButton(self.centralwidget)
        self.emergency_stop_btn.setGeometry(QtCore.QRect(500, 30, 111, 51))
        self.emergency_stop_btn.setObjectName(_fromUtf8("emergency_stop_btn"))
        self.sensor_display = QtGui.QTableView(self.centralwidget)
        self.sensor_display.setGeometry(QtCore.QRect(460, 120, 431, 361))
        self.sensor_display.setDragDropOverwriteMode(False)
        self.sensor_display.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.sensor_display.setObjectName(_fromUtf8("sensor_display"))
        self.camera_view = QtGui.QLabel(self.centralwidget)
        self.camera_view.setGeometry(QtCore.QRect(30, 40, 400, 400))
        self.camera_view.setObjectName(_fromUtf8("camera_view"))
        self.lcd_local_time = QtGui.QLCDNumber(self.centralwidget)
        self.lcd_local_time.setGeometry(QtCore.QRect(760, 40, 131, 41))
        self.lcd_local_time.setDigitCount(8)
        self.lcd_local_time.setProperty("value", 0.0)
        self.lcd_local_time.setProperty("intValue", 0)
        self.lcd_local_time.setObjectName(_fromUtf8("lcd_local_time"))
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(620, 90, 110, 23))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateEdit_2 = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(780, 90, 110, 23))
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.btn_generate_log = QtGui.QPushButton(self.centralwidget)
        self.btn_generate_log.setGeometry(QtCore.QRect(460, 90, 95, 24))
        self.btn_generate_log.setObjectName(_fromUtf8("btn_generate_log"))
        self.start_date_label = QtGui.QLabel(self.centralwidget)
        self.start_date_label.setGeometry(QtCore.QRect(580, 90, 41, 21))
        self.start_date_label.setObjectName(_fromUtf8("start_date_label"))
        self.start_date_label_2 = QtGui.QLabel(self.centralwidget)
        self.start_date_label_2.setGeometry(QtCore.QRect(740, 90, 41, 21))
        self.start_date_label_2.setObjectName(_fromUtf8("start_date_label_2"))
        self.lcd_sideral_time = QtGui.QLCDNumber(self.centralwidget)
        self.lcd_sideral_time.setGeometry(QtCore.QRect(760, 0, 131, 41))
        self.lcd_sideral_time.setDigitCount(8)
        self.lcd_sideral_time.setProperty("value", 0.0)
        self.lcd_sideral_time.setProperty("intValue", 0)
        self.lcd_sideral_time.setObjectName(_fromUtf8("lcd_sideral_time"))
        self.lbl_sideral_time = QtGui.QLabel(self.centralwidget)
        self.lbl_sideral_time.setGeometry(QtCore.QRect(659, 10, 91, 22))
        self.lbl_sideral_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_sideral_time.setObjectName(_fromUtf8("lbl_sideral_time"))
        self.lbl_local_time = QtGui.QLabel(self.centralwidget)
        self.lbl_local_time.setGeometry(QtCore.QRect(670, 50, 80, 22))
        self.lbl_local_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_local_time.setObjectName(_fromUtf8("lbl_local_time"))
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
        QtCore.QObject.connect(self.btn_generate_log, QtCore.SIGNAL(_fromUtf8("clicked()")), TCS_Main_Panel.generate_log)
        QtCore.QMetaObject.connectSlotsByName(TCS_Main_Panel)

    def retranslateUi(self, TCS_Main_Panel):
        TCS_Main_Panel.setWindowTitle(_translate("TCS_Main_Panel", "MainWindow", None))
        self.Start_Stop.setText(_translate("TCS_Main_Panel", "Stop!", None))
        self.open_dome_btn.setText(_translate("TCS_Main_Panel", "Open Dome", None))
        self.close_dome_btn.setText(_translate("TCS_Main_Panel", "Close Dome", None))
        self.emergency_stop_btn.setText(_translate("TCS_Main_Panel", "Emergency Stop!", None))
        self.camera_view.setText(_translate("TCS_Main_Panel", "TextLabel", None))
        self.btn_generate_log.setText(_translate("TCS_Main_Panel", "Generate Log", None))
        self.start_date_label.setText(_translate("TCS_Main_Panel", "Start", None))
        self.start_date_label_2.setText(_translate("TCS_Main_Panel", "End", None))
        self.lbl_sideral_time.setText(_translate("TCS_Main_Panel", "Sidereal Time", None))
        self.lbl_local_time.setText(_translate("TCS_Main_Panel", "UTC Time", None))

