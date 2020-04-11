# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Statistics_Menu_Windows.ui'
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

class Ui_StatisticsWindow(object):
    def setupUi(self, StatisticsWindow):
        StatisticsWindow.setObjectName(_fromUtf8("StatisticsWindow"))
        StatisticsWindow.resize(567, 368)
        self.centralwidget = QtGui.QWidget(StatisticsWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ButtonSpecificStatistics = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonSpecificStatistics.sizePolicy().hasHeightForWidth())
        self.ButtonSpecificStatistics.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ButtonSpecificStatistics.setFont(font)
        self.ButtonSpecificStatistics.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ButtonSpecificStatistics.setObjectName(_fromUtf8("ButtonSpecificStatistics"))
        self.horizontalLayout.addWidget(self.ButtonSpecificStatistics)
        self.ButtonGeneralStatistics = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonGeneralStatistics.sizePolicy().hasHeightForWidth())
        self.ButtonGeneralStatistics.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ButtonGeneralStatistics.setFont(font)
        self.ButtonGeneralStatistics.setMouseTracking(False)
        self.ButtonGeneralStatistics.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ButtonGeneralStatistics.setAutoFillBackground(False)
        self.ButtonGeneralStatistics.setObjectName(_fromUtf8("ButtonGeneralStatistics"))
        self.horizontalLayout.addWidget(self.ButtonGeneralStatistics)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        StatisticsWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(StatisticsWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        StatisticsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StatisticsWindow)
        QtCore.QMetaObject.connectSlotsByName(StatisticsWindow)

    def retranslateUi(self, StatisticsWindow):
        StatisticsWindow.setWindowTitle(_translate("StatisticsWindow", "Statistics Window", None))
        self.ButtonSpecificStatistics.setText(_translate("StatisticsWindow", "Specific Statistics", None))
        self.ButtonGeneralStatistics.setText(_translate("StatisticsWindow", "General Statistics", None))

