# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatisticPanel.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_StatisticsPanel(object):
    def setupUi(self, StatisticsPanel):
        StatisticsPanel.setObjectName(_fromUtf8("StatisticsPanel"))
        StatisticsPanel.resize(429, 276)
        StatisticsPanel.setMinimumSize(QtCore.QSize(429, 276))
        StatisticsPanel.setMaximumSize(QtCore.QSize(429, 276))
        StatisticsPanel.setBaseSize(QtCore.QSize(429, 276))
        self.centralwidget = QtGui.QWidget(StatisticsPanel)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.PixelsPerClass = QtGui.QPushButton(self.centralwidget)
        self.PixelsPerClass.setGeometry(QtCore.QRect(10, 10, 121, 81))
        self.PixelsPerClass.setObjectName(_fromUtf8("PixelsPerClass"))
        self.PercentPixelPerClass = QtGui.QPushButton(self.centralwidget)
        self.PercentPixelPerClass.setGeometry(QtCore.QRect(140, 10, 121, 81))
        self.PercentPixelPerClass.setObjectName(_fromUtf8("PercentPixelPerClass"))
        self.MinValues = QtGui.QPushButton(self.centralwidget)
        self.MinValues.setGeometry(QtCore.QRect(270, 10, 121, 81))
        self.MinValues.setObjectName(_fromUtf8("MinValues"))
        self.MaxValues = QtGui.QPushButton(self.centralwidget)
        self.MaxValues.setGeometry(QtCore.QRect(10, 100, 121, 81))
        self.MaxValues.setObjectName(_fromUtf8("MaxValues"))
        self.AverageValues = QtGui.QPushButton(self.centralwidget)
        self.AverageValues.setGeometry(QtCore.QRect(140, 100, 121, 81))
        self.AverageValues.setObjectName(_fromUtf8("AverageValues"))
        self.StdValues = QtGui.QPushButton(self.centralwidget)
        self.StdValues.setGeometry(QtCore.QRect(270, 100, 121, 81))
        self.StdValues.setObjectName(_fromUtf8("StdValues"))
        self.ScanFmaps = QtGui.QPushButton(self.centralwidget)
        self.ScanFmaps.setGeometry(QtCore.QRect(10, 190, 121, 81))
        self.ScanFmaps.setObjectName(_fromUtf8("EmptyButton_2"))
        self.Comprehensive = QtGui.QPushButton(self.centralwidget)
        self.Comprehensive.setGeometry(QtCore.QRect(140, 190, 121, 81))
        self.Comprehensive.setObjectName(_fromUtf8("EmptyButton_3"))
        self.EmptyButton_4 = QtGui.QPushButton(self.centralwidget)
        self.EmptyButton_4.setGeometry(QtCore.QRect(270, 190, 121, 81))
        self.EmptyButton_4.setText(_fromUtf8(""))
        self.EmptyButton_4.setObjectName(_fromUtf8("EmptyButton_4"))
        StatisticsPanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(StatisticsPanel)
        QtCore.QMetaObject.connectSlotsByName(StatisticsPanel)

    def retranslateUi(self, StatisticsPanel):
        StatisticsPanel.setWindowTitle(_translate("StatisticsPanel", "StatisticPanel", None))
        self.PixelsPerClass.setText(_translate("StatisticsPanel", "Pixels per cluster", None))
        self.PercentPixelPerClass.setText(_translate("StatisticsPanel", "P Pixels per cluster", None))
        self.MinValues.setText(_translate("StatisticsPanel", "Min. Values", None))
        self.MaxValues.setText(_translate("StatisticsPanel", "Max. Values", None))
        self.AverageValues.setText(_translate("StatisticsPanel", "Average Values", None))
	self.StdValues.setText(_translate("StatisticsPanel", "Std Values", None))
	self.ScanFmaps.setText(_translate("StatisticsPanel", "Scan Fmaps", None))
	self.Comprehensive.setText(_translate("StatisticsPanel", "Comprehensive", None))
