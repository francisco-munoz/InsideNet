# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ControlPanel.ui'
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

class Ui_ControlPanel(object):
    def setupUi(self, ControlPanel):
        ControlPanel.setObjectName(_fromUtf8("ControlPanel"))
        ControlPanel.resize(530, 176)
        ControlPanel.setMinimumSize(QtCore.QSize(530, 176))
        ControlPanel.setMaximumSize(QtCore.QSize(530, 176))
        self.centralwidget = QtGui.QWidget(ControlPanel)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.NextTestButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.NextTestButton.setGeometry(QtCore.QRect(420, 130, 91, 41))
        self.NextTestButton.setObjectName(_fromUtf8("NextTestButton"))
        self.LayerComboBox = QtGui.QFontComboBox(self.centralwidget)
        self.LayerComboBox.setGeometry(QtCore.QRect(100, 20, 257, 27))
        self.LayerComboBox.setObjectName(_fromUtf8("LayerComboBox"))
        self.LayerLabel = QtGui.QLabel(self.centralwidget)
        self.LayerLabel.setGeometry(QtCore.QRect(10, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.LayerLabel.setFont(font)
        self.LayerLabel.setObjectName(_fromUtf8("LayerLabel"))
        self.FmapLabel = QtGui.QLabel(self.centralwidget)
        self.FmapLabel.setGeometry(QtCore.QRect(10, 90, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.FmapLabel.setFont(font)
        self.FmapLabel.setObjectName(_fromUtf8("FmapLabel"))
        self.FmapComboBox = QtGui.QFontComboBox(self.centralwidget)
        self.FmapComboBox.setGeometry(QtCore.QRect(100, 90, 257, 27))
        self.FmapComboBox.setObjectName(_fromUtf8("FmapComboBox"))
        self.ShowSpinBox = QtGui.QCheckBox(self.centralwidget)
        self.ShowSpinBox.setGeometry(QtCore.QRect(100, 140, 151, 22))
        self.ShowSpinBox.setObjectName(_fromUtf8("ShowSpinBox"))
        self.AccuracySpinBox = QtGui.QSpinBox(self.centralwidget)
        self.AccuracySpinBox.setGeometry(QtCore.QRect(450, 30, 61, 27))
        self.AccuracySpinBox.setMaximum(255)
        self.AccuracySpinBox.setProperty("value", 1)
        self.AccuracySpinBox.setObjectName(_fromUtf8("AccuracySpinBox"))
        self.AccuracyLabel = QtGui.QLabel(self.centralwidget)
        self.AccuracyLabel.setGeometry(QtCore.QRect(450, 10, 68, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AccuracyLabel.setFont(font)
        self.AccuracyLabel.setObjectName(_fromUtf8("AccuracyLabel"))
        ControlPanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(ControlPanel)
        QtCore.QMetaObject.connectSlotsByName(ControlPanel)

    def retranslateUi(self, ControlPanel):
        ControlPanel.setWindowTitle(_translate("ControlPanel", "ControlPanel", None))
        self.NextTestButton.setText(_translate("ControlPanel", "Next Test", None))
        self.LayerLabel.setText(_translate("ControlPanel", "Layer", None))
        self.FmapLabel.setText(_translate("ControlPanel", "Fmap", None))
        self.ShowSpinBox.setText(_translate("ControlPanel", "Show Everything", None))
        self.AccuracyLabel.setText(_translate("ControlPanel", "Accuracy", None))

