# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GeneralStatisticControlPanel.ui'
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

class Ui_GeneralStatisticControlPanel(object):
    def setupUi(self, GeneralStatisticControlPanel):
        GeneralStatisticControlPanel.setObjectName(_fromUtf8("GeneralStatisticControlPanel"))
        GeneralStatisticControlPanel.resize(629, 362)
        GeneralStatisticControlPanel.setMinimumSize(QtCore.QSize(629, 362))
        GeneralStatisticControlPanel.setMaximumSize(QtCore.QSize(629, 362))
        GeneralStatisticControlPanel.setBaseSize(QtCore.QSize(629, 362))
        self.centralwidget = QtGui.QWidget(GeneralStatisticControlPanel)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.NumberOfImagesLabel = QtGui.QLabel(self.centralwidget)
        self.NumberOfImagesLabel.setGeometry(QtCore.QRect(20, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.NumberOfImagesLabel.setFont(font)
        self.NumberOfImagesLabel.setObjectName(_fromUtf8("NumberOfImagesLabel"))
        self.NumberOfImagesCB = QtGui.QSpinBox(self.centralwidget)
        self.NumberOfImagesCB.setGeometry(QtCore.QRect(180, 20, 131, 27))
        self.NumberOfImagesCB.setObjectName(_fromUtf8("NumberOfImagesCB"))
#        self.AccuracyCB = QtGui.QSpinBox(self.centralwidget)
        self.AccuracyCB = QtGui.QDoubleSpinBox(self.centralwidget)
        self.AccuracyCB.setGeometry(QtCore.QRect(430, 20, 51, 27))
        self.AccuracyCB.setObjectName(_fromUtf8("AccuracyCB"))
        self.AccuracyLabel = QtGui.QLabel(self.centralwidget)
        self.AccuracyLabel.setGeometry(QtCore.QRect(350, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.AccuracyLabel.setFont(font)
        self.AccuracyLabel.setObjectName(_fromUtf8("AccuracyLabel"))
        self.NumberOfLayersCB = QtGui.QSpinBox(self.centralwidget)
        self.NumberOfLayersCB.setGeometry(QtCore.QRect(180, 170, 51, 27))
        self.NumberOfLayersCB.setObjectName(_fromUtf8("NumberOfLayersCB"))
        self.NumberOfLayersLabel = QtGui.QLabel(self.centralwidget)
        self.NumberOfLayersLabel.setGeometry(QtCore.QRect(20, 170, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.NumberOfLayersLabel.setFont(font)
        self.NumberOfLayersLabel.setObjectName(_fromUtf8("NumberOfLayersLabel"))
        self.FmapsPerLayerLabel = QtGui.QLabel(self.centralwidget)
        self.FmapsPerLayerLabel.setGeometry(QtCore.QRect(20, 230, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.FmapsPerLayerLabel.setFont(font)
        self.FmapsPerLayerLabel.setObjectName(_fromUtf8("FmapsPerLayerLabel"))
        self.FmapsPerLayerCB = QtGui.QSpinBox(self.centralwidget)
        self.FmapsPerLayerCB.setGeometry(QtCore.QRect(180, 230, 51, 27))
        self.FmapsPerLayerCB.setObjectName(_fromUtf8("FmapsPerLayerCB"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 50, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 50, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 200, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(180, 260, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.InformationLabel = QtGui.QLabel(self.centralwidget)
        self.InformationLabel.setGeometry(QtCore.QRect(230, 0, 221, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.InformationLabel.setFont(font)
        self.InformationLabel.setObjectName(_fromUtf8("InformationLabel"))
        self.OnlyOneCheck = QtGui.QCheckBox(self.centralwidget)
        self.OnlyOneCheck.setGeometry(QtCore.QRect(350, 120, 99, 22))
        self.OnlyOneCheck.setObjectName(_fromUtf8("OnlyOneCheck"))
        self.LayerCB = QtGui.QComboBox(self.centralwidget)
        self.LayerCB.setGeometry(QtCore.QRect(410, 160, 201, 27))
        self.LayerCB.setObjectName(_fromUtf8("LayerCB"))
        self.LayerLabel = QtGui.QLabel(self.centralwidget)
        self.LayerLabel.setGeometry(QtCore.QRect(350, 160, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.LayerLabel.setFont(font)
        self.LayerLabel.setObjectName(_fromUtf8("LayerLabel"))
        self.FmapCB = QtGui.QComboBox(self.centralwidget)
        self.FmapCB.setGeometry(QtCore.QRect(410, 200, 201, 27))
        self.FmapCB.setObjectName(_fromUtf8("FmapCB"))
        self.FmapLabel = QtGui.QLabel(self.centralwidget)
        self.FmapLabel.setGeometry(QtCore.QRect(350, 200, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.FmapLabel.setFont(font)
        self.FmapLabel.setObjectName(_fromUtf8("FmapLabel"))
        self.GenerateButton = QtGui.QPushButton(self.centralwidget)
        self.GenerateButton.setGeometry(QtCore.QRect(250, 300, 81, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GenerateButton.setFont(font)
        self.GenerateButton.setObjectName(_fromUtf8("GenerateButton"))
        self.GroupEverything = QtGui.QCheckBox(self.centralwidget)
        self.GroupEverything.setGeometry(QtCore.QRect(10, 290, 171, 22))
        self.GroupEverything.setObjectName(_fromUtf8("GroupEverything"))
        self.GroupByFmap = QtGui.QCheckBox(self.centralwidget)
        self.GroupByFmap.setGeometry(QtCore.QRect(10, 320, 131, 22))
        self.GroupByFmap.setObjectName(_fromUtf8("GroupByFmap"))
        self.MaxValueRangeLabel = QtGui.QLabel(self.centralwidget)
        self.MaxValueRangeLabel.setGeometry(QtCore.QRect(20, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.MaxValueRangeLabel.setFont(font)
        self.MaxValueRangeLabel.setObjectName(_fromUtf8("MaxValueRangeLabel"))
        self.MaxValueRangeCB = QtGui.QSpinBox(self.centralwidget)
        self.MaxValueRangeCB.setGeometry(QtCore.QRect(180, 80, 71, 31))
        self.MaxValueRangeCB.setMaximum(10000)
        self.MaxValueRangeCB.setObjectName(_fromUtf8("MaxValueRangeCB"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(180, 110, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        GeneralStatisticControlPanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(GeneralStatisticControlPanel)
        QtCore.QMetaObject.connectSlotsByName(GeneralStatisticControlPanel)

    def retranslateUi(self, GeneralStatisticControlPanel):
        GeneralStatisticControlPanel.setWindowTitle(_translate("GeneralStatisticControlPanel", "GeneralStatisticControlPanel", None))
        self.NumberOfImagesLabel.setText(_translate("GeneralStatisticControlPanel", "Number of Images", None))
        self.AccuracyLabel.setText(_translate("GeneralStatisticControlPanel", "Accuracy", None))
        self.NumberOfLayersLabel.setText(_translate("GeneralStatisticControlPanel", "Number of Layers", None))
        self.FmapsPerLayerLabel.setText(_translate("GeneralStatisticControlPanel", "Fmaps Per Layer", None))
        self.label_5.setText(_translate("GeneralStatisticControlPanel", "(Default: 10)", None))
        self.label_6.setText(_translate("GeneralStatisticControlPanel", "(Default: 5)", None))
        self.label_7.setText(_translate("GeneralStatisticControlPanel", "(Default: *)", None))
        self.label_8.setText(_translate("GeneralStatisticControlPanel", "(Default: *)", None))
        self.InformationLabel.setText(_translate("GeneralStatisticControlPanel", "[Default value is 0 in all cases]", None))
        self.OnlyOneCheck.setText(_translate("GeneralStatisticControlPanel", "Only one", None))
        self.LayerLabel.setText(_translate("GeneralStatisticControlPanel", "Layer", None))
        self.FmapLabel.setText(_translate("GeneralStatisticControlPanel", "Fmap", None))
        self.GenerateButton.setText(_translate("GeneralStatisticControlPanel", "Generate", None))
        self.GroupEverything.setText(_translate("GeneralStatisticControlPanel", "Group Everything", None))
        self.GroupByFmap.setText(_translate("GeneralStatisticControlPanel", "Group by Fmap", None))
        self.MaxValueRangeLabel.setText(_translate("GeneralStatisticControlPanel", "Max Value Range", None))
        self.label_9.setText(_translate("GeneralStatisticControlPanel", "(Default: *)", None))
