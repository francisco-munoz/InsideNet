# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Load_File_Path_Window.ui'
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
        SelectPaths.resize(740, 91)
        SelectPaths.setMinimumSize(QtCore.QSize(740, 91))
        SelectPaths.setMaximumSize(QtCore.QSize(735, 328))
        SelectPaths.setBaseSize(QtCore.QSize(735, 328))
        self.centralwidget = QtGui.QWidget(SelectPaths)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.LoadFileLabel = QtGui.QLabel(self.centralwidget)
        self.LoadFileLabel.setGeometry(QtCore.QRect(10, 20, 271, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.LoadFileLabel.setFont(font)
        self.LoadFileLabel.setObjectName(_fromUtf8("LoadFileLabel"))
        self.FileLoadButton = QtGui.QToolButton(self.centralwidget)
        self.FileLoadButton.setGeometry(QtCore.QRect(230, 10, 24, 25))
        self.FileLoadButton.setObjectName(_fromUtf8("FileLoadButton"))
        self.FileLoadLineEditor = QtGui.QLineEdit(self.centralwidget)
        self.FileLoadLineEditor.setGeometry(QtCore.QRect(260, 10, 451, 27))
        self.FileLoadLineEditor.setObjectName(_fromUtf8("FileLoadLineEditor"))
        self.acceptLoadFileButton = QtGui.QDialogButtonBox(self.centralwidget)
        self.acceptLoadFileButton.setGeometry(QtCore.QRect(540, 60, 176, 27))
        self.acceptLoadFileButton.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.acceptLoadFileButton.setObjectName(_fromUtf8("acceptLoadFileButton"))
        SelectPaths.setCentralWidget(self.centralwidget)

        self.retranslateUi(SelectPaths)
        QtCore.QMetaObject.connectSlotsByName(SelectPaths)

    def retranslateUi(self, SelectPaths):
        SelectPaths.setWindowTitle(_translate("SelectPaths", "Select Your Paths", None))
        self.LoadFileLabel.setText(_translate("SelectPaths", "Select File to Load Data", None))
        self.FileLoadButton.setText(_translate("SelectPaths", "...", None))

