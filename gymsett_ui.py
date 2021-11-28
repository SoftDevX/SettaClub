# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gymsett.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GymSettings(object):
    def setupUi(self, GymSettings):
        GymSettings.setObjectName("GymSettings")
        GymSettings.resize(747, 413)
        self.centralwidget = QtWidgets.QWidget(GymSettings)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainframe = QtWidgets.QFrame(self.centralwidget)
        self.mainframe.setStyleSheet("\n"
"    background-color: rgb(91, 91, 91);\n"
"\n"
"")
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainframe)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.mainframe)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.assuPriceConfig = QtWidgets.QSpinBox(self.frame)
        self.assuPriceConfig.setGeometry(QtCore.QRect(190, 52, 151, 31))
        self.assuPriceConfig.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.assuPriceConfig.setFont(font)
        self.assuPriceConfig.setStyleSheet("background-color: rgb(154, 154, 154);\n"
"border-radius:5px;")
        self.assuPriceConfig.setMaximum(5000)
        self.assuPriceConfig.setSingleStep(100)
        self.assuPriceConfig.setObjectName("assuPriceConfig")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(22, 52, 144, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(22, 124, 128, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.moiPriceConfig = QtWidgets.QSpinBox(self.frame)
        self.moiPriceConfig.setGeometry(QtCore.QRect(190, 124, 151, 31))
        self.moiPriceConfig.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.moiPriceConfig.setFont(font)
        self.moiPriceConfig.setStyleSheet("background-color: rgb(154, 154, 154);\n"
"border-radius:5px;")
        self.moiPriceConfig.setMaximum(5000)
        self.moiPriceConfig.setSingleStep(100)
        self.moiPriceConfig.setObjectName("moiPriceConfig")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(22, 195, 148, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.troiMoiPriceConfig = QtWidgets.QSpinBox(self.frame)
        self.troiMoiPriceConfig.setGeometry(QtCore.QRect(190, 195, 151, 31))
        self.troiMoiPriceConfig.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.troiMoiPriceConfig.setFont(font)
        self.troiMoiPriceConfig.setStyleSheet("background-color: rgb(154, 154, 154);\n"
"border-radius:5px;")
        self.troiMoiPriceConfig.setMaximum(5000)
        self.troiMoiPriceConfig.setSingleStep(100)
        self.troiMoiPriceConfig.setObjectName("troiMoiPriceConfig")
        self.fermer = QtWidgets.QPushButton(self.frame)
        self.fermer.setGeometry(QtCore.QRect(10, 330, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(18)
        self.fermer.setFont(font)
        self.fermer.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    color: rgb(208, 208, 208);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.422538, y2:0.42, stop:1 rgba(128, 128, 128, 213));\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"\n"
" }\n"
"")
        self.fermer.setObjectName("fermer")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.mainframe)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.conf = QtWidgets.QPushButton(self.frame_2)
        self.conf.setGeometry(QtCore.QRect(210, 330, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(18)
        self.conf.setFont(font)
        self.conf.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    color: rgb(208, 208, 208);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.422538, y2:0.42, stop:1 rgba(128, 128, 128, 213));\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"\n"
" }\n"
"")
        self.conf.setObjectName("conf")
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.mainframe)
        GymSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(GymSettings)
        QtCore.QMetaObject.connectSlotsByName(GymSettings)

    def retranslateUi(self, GymSettings):
        _translate = QtCore.QCoreApplication.translate
        GymSettings.setWindowTitle(_translate("GymSettings", "GymSettings"))
        self.label_6.setText(_translate("GymSettings", "Prix d\'assurance"))
        self.label_12.setText(_translate("GymSettings", "Prix d\'un mois"))
        self.label_13.setText(_translate("GymSettings", "Prix de troi mois"))
        self.fermer.setText(_translate("GymSettings", "Fermer"))
        self.conf.setText(_translate("GymSettings", "Confirmer"))