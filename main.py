#!/usr/local/bin/python3.5

from PyQt5 import QtCore, QtGui, QtWidgets, QtQml, QtQuick
from PyQt5.QtCore import Qt, QObject, pyqtSlot, QVariant
from PyQt5.QtQml import QJSValue, QJSEngine

import numpy as np
import pandas as pd
import io
from numpy.random import random
from time import time

tmp = '123'
class PQExchange(QObject):
	@pyqtSlot(QJSValue)
	def log(self, var):
		global tmp
		tmp = var
		print(var)


app = QtGui.QGuiApplication([])
view = QtQuick.QQuickView()
context = view.rootContext()
py = PQExchange()
context.setContextProperty('py', py)
view.setSource(QtCore.QUrl('main.qml'))

engine = context.engine()

rootObj = view.rootObject()

view.show()
app.exec_()