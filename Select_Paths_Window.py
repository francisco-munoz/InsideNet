# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Select_Paths.ui'
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

class Ui_SelectPaths(object):
    def setupUi(self, SelectPaths):
        SelectPaths.setObjectName(_fromUtf8("SelectPaths"))
        SelectPaths.setWindowModality(QtCore.Qt.ApplicationModal)
        SelectPaths.resize(735, 328)
        SelectPaths.setMinimumSize(QtCore.QSize(735, 328))
        SelectPaths.setMaximumSize(QtCore.QSize(735, 328))
        SelectPaths.setBaseSize(QtCore.QSize(735, 328))
        self.centralwidget = QtGui.QWidget(SelectPaths)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.NetworkFileLabel = QtGui.QLabel(self.centralwidget)
        self.NetworkFileLabel.setGeometry(QtCore.QRect(20, 80, 271, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.NetworkFileLabel.setFont(font)
        self.NetworkFileLabel.setObjectName(_fromUtf8("NetworkFileLabel"))
        self.NetworkFileButton = QtGui.QToolButton(self.centralwidget)
        self.NetworkFileButton.setGeometry(QtCore.QRect(300, 70, 24, 25))
        self.NetworkFileButton.setObjectName(_fromUtf8("NetworkFileButton"))
        self.NetworkFileLineEditor = QtGui.QLineEdit(self.centralwidget)
        self.NetworkFileLineEditor.setGeometry(QtCore.QRect(340, 70, 391, 27))
        self.NetworkFileLineEditor.setObjectName(_fromUtf8("NetworkFileLineEditor"))
        self.WeightsLabel = QtGui.QLabel(self.centralwidget)
        self.WeightsLabel.setGeometry(QtCore.QRect(120, 160, 271, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.WeightsLabel.setFont(font)
        self.WeightsLabel.setObjectName(_fromUtf8("WeightsLabel"))
        self.WeightsButton = QtGui.QToolButton(self.centralwidget)
        self.WeightsButton.setGeometry(QtCore.QRect(300, 150, 24, 25))
        self.WeightsButton.setObjectName(_fromUtf8("WeightsButton"))
        self.WeightsLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.WeightsLineEdit.setGeometry(QtCore.QRect(340, 150, 391, 27))
        self.WeightsLineEdit.setObjectName(_fromUtf8("WeightsLineEdit"))
        self.ImagePathLabel = QtGui.QLabel(self.centralwidget)
        self.ImagePathLabel.setGeometry(QtCore.QRect(130, 240, 271, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ImagePathLabel.setFont(font)
        self.ImagePathLabel.setObjectName(_fromUtf8("ImagePathLabel"))
        self.ImagePathLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.ImagePathLineEdit.setGeometry(QtCore.QRect(340, 230, 391, 27))
        self.ImagePathLineEdit.setObjectName(_fromUtf8("ImagePathLineEdit"))
        self.ImagePathButton = QtGui.QToolButton(self.centralwidget)
        self.ImagePathButton.setGeometry(QtCore.QRect(300, 230, 24, 25))
        self.ImagePathButton.setObjectName(_fromUtf8("ImagePathButton"))
        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(550, 290, 176, 27))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        SelectPaths.setCentralWidget(self.centralwidget)

        self.retranslateUi(SelectPaths)
        QtCore.QMetaObject.connectSlotsByName(SelectPaths)

    def retranslateUi(self, SelectPaths):
        SelectPaths.setWindowTitle(_translate("SelectPaths", "Select Your Paths", None))
        self.NetworkFileLabel.setText(_translate("SelectPaths", "Select Network Definition File", None))
        self.NetworkFileButton.setText(_translate("SelectPaths", "...", None))
        self.WeightsLabel.setText(_translate("SelectPaths", "Select Weights File", None))
        self.WeightsButton.setText(_translate("SelectPaths", "...", None))
        self.ImagePathLabel.setText(_translate("SelectPaths", "Select Image Path", None))
        self.ImagePathButton.setText(_translate("SelectPaths", "...", None))

