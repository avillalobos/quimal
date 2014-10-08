#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tcs_gui.ui'
#
# Created: Sun Oct  5 21:42:55 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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
    
    def setupUi(self, TCS_Main_Panel):
        TCS_Main_Panel.setObjectName(_fromUtf8("TCS_Main_Panel"))
        TCS_Main_Panel.resize(800, 600)
        self.centralwidget = QtGui.QWidget(TCS_Main_Panel)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Start_Stop = QtGui.QPushButton(self.centralwidget)
        self.Start_Stop.setGeometry(QtCore.QRect(700, 530, 94, 24))
        self.Start_Stop.setObjectName(_fromUtf8("Start_Stop"))
        self.LogMonitor = QtGui.QPlainTextEdit(self.centralwidget)
        self.LogMonitor.setGeometry(QtCore.QRect(0, 480, 701, 76))
        self.LogMonitor.setObjectName(_fromUtf8("LogMonitor"))
        TCS_Main_Panel.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(TCS_Main_Panel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        TCS_Main_Panel.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(TCS_Main_Panel)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        TCS_Main_Panel.setStatusBar(self.statusbar)
        
        self.retranslateUi(TCS_Main_Panel)
        QtCore.QObject.connect(self.Start_Stop, QtCore.SIGNAL(_fromUtf8("clicked()")), self.LogMonitor.repaint)
        QtCore.QMetaObject.connectSlotsByName(TCS_Main_Panel)

    def retranslateUi(self, TCS_Main_Panel):
        TCS_Main_Panel.setWindowTitle(_translate("TCS_Main_Panel", "MainWindow", None))
        self.Start_Stop.setText(_translate("TCS_Main_Panel", "Start!", None))
        self.Start_Stop.clicked.connect(self.printStuff)
        
    def printStuff(self):
        self.LogMonitor.appendPlainText("Hola")
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
