# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DICOMDIRGui.ui'
#
# Created: Sun Mar 15 11:19:12 2015
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

try:
  from PyQt4 import QtGui, QtCore
except:
  from PyQt5 import QtGui, QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DICOMDIRGui(object):
    def setupUi(self, DICOMDIRGui):
        DICOMDIRGui.setObjectName(_fromUtf8("DICOMDIRGui"))
        DICOMDIRGui.setWindowModality(QtCore.Qt.WindowModal)
        DICOMDIRGui.resize(685, 583)
        self.buttonBox = QtGui.QDialogButtonBox(DICOMDIRGui)
        self.buttonBox.setGeometry(QtCore.QRect(105, 545, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(DICOMDIRGui)
        self.layoutWidget.setGeometry(QtCore.QRect(5, 10, 676, 531))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblDICOMDIR = QtGui.QLabel(self.layoutWidget)
        self.lblDICOMDIR.setAutoFillBackground(True)
        self.lblDICOMDIR.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblDICOMDIR.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblDICOMDIR.setText(_fromUtf8(""))
        self.lblDICOMDIR.setWordWrap(True)
        self.lblDICOMDIR.setObjectName(_fromUtf8("lblDICOMDIR"))
        self.verticalLayout.addWidget(self.lblDICOMDIR)
        self.listDICOMDIR = QtGui.QListWidget(self.layoutWidget)
        self.listDICOMDIR.setStyleSheet(_fromUtf8("selection-background-color: rgb(255, 255, 127);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.listDICOMDIR.setAlternatingRowColors(True)
        self.listDICOMDIR.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listDICOMDIR.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.listDICOMDIR.setResizeMode(QtGui.QListView.Adjust)
        self.listDICOMDIR.setObjectName(_fromUtf8("listDICOMDIR"))
        self.verticalLayout.addWidget(self.listDICOMDIR)

        self.retranslateUi(DICOMDIRGui)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DICOMDIRGui.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DICOMDIRGui.reject)
        QtCore.QMetaObject.connectSlotsByName(DICOMDIRGui)

    def retranslateUi(self, DICOMDIRGui):
        DICOMDIRGui.setWindowTitle(QtGui.QApplication.translate("DICOMDIRGui", "DICOMDIR", None, QtGui.QApplication.UnicodeUTF8))

