import sys, random
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class SensorTableModel(QTableWidget):
	def __init__(self, *args):
		QTableWidget.__init__(self, *args)
		self.data = {'Sensor Name':['Sensor 1','Sensor 2','Sensor 3'], 'Status':['Warning','Critical','Ok'], 'Value':['7','8','9']}
		self.setmydata()
		#self.resizeColumnsToContents()
		#self.resizeRowsToContents()
		header = self.horizontalHeader()
		header.setStretchLastSection(True)
		#self.clicked.connect(self.update)
		    
	def setmydata(self):

		horHeaders = []
		for n, key in enumerate(sorted(self.data.keys())):
			horHeaders.append(key)
			for m, item in enumerate(self.data[key]):
				newitem = QTableWidgetItem(item)
				newitem.setFlags(Qt.ItemIsEnabled)
				self.setItem(m, n, newitem)
				self.setHorizontalHeaderLabels(horHeaders)
	
	def updateSensorData(self, sensor, status, value):
		row = self.data["Sensor Name"].index(sensor)
		self.setItem(row, 1, QTableWidgetItem(str(status)))
		self.setItem(row, 2, QTableWidgetItem(str(value)))

