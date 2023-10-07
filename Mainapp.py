import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QInputDialog, QApplication, QProgressBar, QLabel
from PyQt5.QtGui import QImage, qRgb, QColor, QPixmap, QTransform 
from PyQt5.QtCore import QTimer, Qt
import cv2 
from Aritmath import Ui_Aritmath
from RegionOfInterest import Ui_roi
import numpy as np
import matplotlib.pyplot as plt
import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1045, 740)
        MainWindow.resize(1080, 650)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 10, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pbInput = QtWidgets.QLabel(self.centralwidget)
        self.pbInput.setGeometry(QtCore.QRect(2, 40, 512, 512))
        self.pbInput.setAutoFillBackground(False)
        self.pbInput.setFrameShape(QtWidgets.QFrame.Panel)
        self.pbInput.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pbInput.setLineWidth(1)
        self.pbInput.setText("")
        self.pbInput.setObjectName("pbInput")
        self.pbOutput = QtWidgets.QLabel(self.centralwidget)
        self.pbOutput.setGeometry(QtCore.QRect(530, 40, 512, 512))
        self.pbOutput.setFrameShape(QtWidgets.QFrame.Panel)
        self.pbOutput.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pbOutput.setText("")
        self.pbOutput.setObjectName("pbOutput")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(887, 560, 200, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("loading")
        self.labelInput = QtWidgets.QLabel(self.centralwidget)
        self.labelInput.setGeometry(QtCore.QRect(20, 10, 400, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.labelInput.setFont(font)
        self.labelInput.setText("")
        self.labelInput.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelInput.setObjectName("labelInput")
        self.labelOutput = QtWidgets.QLabel(self.centralwidget)
        self.labelOutput.setGeometry(QtCore.QRect(660, 10, 381, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.labelOutput.setFont(font)
        self.labelOutput.setText("")
        self.labelOutput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelOutput.setObjectName("labelOutput")
        self.labelEfek = QtWidgets.QLabel(self.centralwidget)
        self.labelEfek.setGeometry(QtCore.QRect(10, 560, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelEfek.setFont(font)
        self.labelEfek.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelEfek.setObjectName("labelEfek")
        self.pbPreview = QtWidgets.QLabel(self.centralwidget)
        self.pbPreview.setGeometry(QtCore.QRect(418, 590, 96, 96))
        self.pbPreview.setAutoFillBackground(False)
        self.pbPreview.setFrameShape(QtWidgets.QFrame.Panel)
        self.pbPreview.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pbPreview.setLineWidth(1)
        self.pbPreview.setText("")
        self.pbPreview.setObjectName("pbPreview")
        self.labelInput_6 = QtWidgets.QLabel(self.centralwidget)
        self.labelInput_6.setGeometry(QtCore.QRect(18, 675, 391, 16))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.labelInput_6.setFont(font)
        self.labelInput_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelInput_6.setObjectName("labelInput_6")
        self.labelLoading = QtWidgets.QLabel(self.centralwidget)
        self.labelLoading.setGeometry(QtCore.QRect(530, 560, 381, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.labelLoading.setFont(font)
        self.labelLoading.setText("")
        self.labelLoading.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelLoading.setObjectName("labelLoading")
        self.labelWarning = QtWidgets.QLabel(self.centralwidget)
        self.labelWarning.setGeometry(QtCore.QRect(530, 590, 501, 105))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelWarning.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelWarning.setFont(font)
        self.labelWarning.setText("")
        self.labelWarning.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelWarning.setObjectName("labelWarning")
        self.buttonClear = QtWidgets.QPushButton(self.centralwidget)
        self.buttonClear.setGeometry(QtCore.QRect(10, 558, 120, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonClear.sizePolicy().hasHeightForWidth())
        self.buttonClear.setSizePolicy(sizePolicy)

        self.buttonSetImage = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSetImage.setGeometry(QtCore.QRect(390, 558, 120, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSetImage.sizePolicy().hasHeightForWidth())
        self.buttonSetImage.setSizePolicy(sizePolicy)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.buttonClear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonClear.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonClear.setObjectName("buttonClear")
        self.buttonSetImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonSetImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonSetImage.setObjectName("buttonSetImage")
        self.buttonUndo = QtWidgets.QPushButton(self.centralwidget)
        self.buttonUndo.setGeometry(QtCore.QRect(395, 558, 120, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonUndo.sizePolicy().hasHeightForWidth())
        self.buttonUndo.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.buttonUndo.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        self.buttonUndo.setFont(font)
        self.buttonUndo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonUndo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonUndo.setObjectName("buttonUndo")
        self.buttonEffect1 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEffect1.setGeometry(QtCore.QRect(10, 590, 401, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonEffect1.sizePolicy().hasHeightForWidth())
        self.buttonEffect1.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.buttonEffect1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.buttonEffect1.setFont(font)
        self.buttonEffect1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonEffect1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonEffect1.setStyleSheet("text-align: left;\n"
"")
        self.buttonEffect1.setObjectName("buttonEffect1")
        self.buttonEffect2 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEffect2.setGeometry(QtCore.QRect(10, 620, 401, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonEffect2.sizePolicy().hasHeightForWidth())
        self.buttonEffect2.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.buttonEffect2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.buttonEffect2.setFont(font)
        self.buttonEffect2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonEffect2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonEffect2.setStyleSheet("text-align: left;\n"
"")
        self.buttonEffect2.setObjectName("buttonEffect2")
        self.buttonEffect3 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEffect3.setGeometry(QtCore.QRect(10, 650, 401, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonEffect3.sizePolicy().hasHeightForWidth())
        self.buttonEffect3.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.buttonEffect3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.buttonEffect3.setFont(font)
        self.buttonEffect3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonEffect3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonEffect3.setStyleSheet("text-align: left;\n"
"")
        self.buttonEffect3.setObjectName("buttonEffect3")
        self.buttonSet = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSet.setGeometry(QtCore.QRect(923, 558, 120, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSet.sizePolicy().hasHeightForWidth())
        self.buttonSet.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.buttonSet.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        self.buttonSet.setFont(font)
        self.buttonSet.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonSet.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonSet.setObjectName("buttonSet")
        self.buttonTetapImport = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTetapImport.setGeometry(QtCore.QRect(923, 665, 120, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonTetapImport.sizePolicy().hasHeightForWidth())
        self.buttonTetapImport.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.buttonTetapImport.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        self.buttonTetapImport.setFont(font)
        self.buttonTetapImport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonTetapImport.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonTetapImport.setObjectName("buttonTetapImport")
        self.buttonSimpan = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSimpan.setGeometry(QtCore.QRect(270, 558, 120, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSimpan.sizePolicy().hasHeightForWidth())
        self.buttonSimpan.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.buttonSimpan.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        self.buttonSimpan.setFont(font)
        self.buttonSimpan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonSimpan.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonSimpan.setObjectName("buttonSimpan")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHistogram = QtWidgets.QMenu(self.menuView)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon/icons8-histogram-100 (6).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuHistogram.setIcon(icon)
        self.menuHistogram.setObjectName("menuHistogram")
        self.menuColor = QtWidgets.QMenu(self.menubar)
        self.menuColor.setObjectName("menuColor")
        self.menuRGB = QtWidgets.QMenu(self.menuColor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icon/icons8-rgb-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuRGB.setIcon(icon1)
        self.menuRGB.setObjectName("menuRGB")
        self.menuRGB_to_Grayscale = QtWidgets.QMenu(self.menuColor)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icon/icons8-rgb-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuRGB_to_Grayscale.setIcon(icon2)
        self.menuRGB_to_Grayscale.setObjectName("menuRGB_to_Grayscale")
        self.menuBit_Depth = QtWidgets.QMenu(self.menuColor)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icon/icons8-depth-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBit_Depth.setIcon(icon3)
        self.menuBit_Depth.setObjectName("menuBit_Depth")
        self.menuImage_Processing = QtWidgets.QMenu(self.menubar)
        self.menuImage_Processing.setObjectName("menuImage_Processing")
        self.menuAritmatics_Operation = QtWidgets.QMenu(self.menubar)
        self.menuAritmatics_Operation.setObjectName("menuAritmatics_Operation")
        self.menuFilter = QtWidgets.QMenu(self.menubar)
        self.menuFilter.setObjectName("menuFilter")
        self.menuGaussian_Blur = QtWidgets.QMenu(self.menuFilter)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icon/bluricon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuGaussian_Blur.setIcon(icon4)
        self.menuGaussian_Blur.setObjectName("menuGaussian_Blur")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menubar)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        self.menuMorphology = QtWidgets.QMenu(self.menubar)
        self.menuMorphology.setObjectName("menuMorphology")
        self.menuErosion = QtWidgets.QMenu(self.menuMorphology)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icon/icons8-image-100a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuErosion.setIcon(icon5)
        self.menuErosion.setObjectName("menuErosion")
        self.menuOpening = QtWidgets.QMenu(self.menuMorphology)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icon/icons8-image-100c.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuOpening.setIcon(icon6)
        self.menuOpening.setObjectName("menuOpening")
        self.menuDilation = QtWidgets.QMenu(self.menuMorphology)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Icon/icons8-image-100b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuDilation.setIcon(icon7)
        self.menuDilation.setObjectName("menuDilation")
        self.menuClosing = QtWidgets.QMenu(self.menuMorphology)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Icon/icons8-image-100d.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuClosing.setIcon(icon8)
        self.menuClosing.setObjectName("menuClosing")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuAppearance = QtWidgets.QMenu(self.menuAbout)
        self.menuAppearance.setObjectName("menuAppearance")
        self.menuType_Font = QtWidgets.QMenu(self.menuAppearance)
        self.menuType_Font.setObjectName("menuType_Font")
        self.menuAuto_Fit_Image = QtWidgets.QMenu(self.menuAppearance)
        self.menuAuto_Fit_Image.setObjectName("menuAuto_Fit_Image")
        self.menuInputBorderStyle = QtWidgets.QMenu(self.menuAppearance)
        self.menuInputBorderStyle.setObjectName("menuInputBorderStyle")
        self.menuSize_Font = QtWidgets.QMenu(self.menuAppearance)
        self.menuSize_Font.setObjectName("menuSize_Font")
        self.menuLanguage = QtWidgets.QMenu(self.menuAbout)
        self.menuLanguage.setObjectName("menuLanguage")
        self.menuThird_Apps = QtWidgets.QMenu(self.menuAbout)
        self.menuThird_Apps.setObjectName("menuThird_Apps")
        self.menuAbout_2 = QtWidgets.QMenu(self.menubar)
        self.menuAbout_2.setObjectName("menuAbout_2")
        self.menuGeometry = QtWidgets.QMenu(self.menubar)
        self.menuGeometry.setObjectName("menuGeometry")
        self.menuRotation = QtWidgets.QMenu(self.menuGeometry)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Icon/icons8-rotation-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuRotation.setIcon(icon9)
        self.menuRotation.setObjectName("menuRotation")
        self.menuScaling = QtWidgets.QMenu(self.menuGeometry)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Icon/icons8-fit-to-width-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuScaling.setIcon(icon10)
        self.menuScaling.setObjectName("menuScaling")
        self.menuFeature_Extraction = QtWidgets.QMenu(self.menubar)
        self.menuFeature_Extraction.setObjectName("menuFeature_Extraction")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("Icon/icons8-open-file-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon11)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("Icon/icons8-save-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon12)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("Icon/icons8-exit-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon13)
        self.actionExit.setObjectName("actionExit")
        self.actionInput = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("Icon/icons8-histogram-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInput.setIcon(icon14)
        self.actionInput.setObjectName("actionInput")
        self.actionOutput = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("Icon/icons8-histogram-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOutput.setIcon(icon15)
        self.actionOutput.setObjectName("actionOutput")
        self.actionInput_Output = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("Icon/icons8-histogram-100 (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInput_Output.setIcon(icon16)
        self.actionInput_Output.setObjectName("actionInput_Output")
        self.actionBrightness = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("Icon/icons8-rgb-100 (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBrightness.setIcon(icon17)
        self.actionBrightness.setObjectName("actionBrightness")
        self.actionBrightness_Contrast = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("Icon/icons8-rgb-100 (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBrightness_Contrast.setIcon(icon18)
        self.actionBrightness_Contrast.setObjectName("actionBrightness_Contrast")
        self.actionLog_Brightness = QtWidgets.QAction(MainWindow)
        icon101 = QtGui.QIcon()
        icon101.addPixmap(QtGui.QPixmap("Icon/log_brightness.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLog_Brightness.setIcon(icon101)
        self.actionLog_Brightness.setObjectName("actionLog_Brightness")
        self.actionInvers = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("Icon/icons8-rgb-100 (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInvers.setIcon(icon19)
        self.actionInvers.setObjectName("actionInvers")
        self.actionGamma_Correction = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("Icon/icons8-gamma-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGamma_Correction.setIcon(icon20)
        self.actionGamma_Correction.setObjectName("actionGamma_Correction")
        self.actionHistogram_Equalization_HE = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("Icon/icons8-histogram-100 (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHistogram_Equalization_HE.setIcon(icon21)
        self.actionHistogram_Equalization_HE.setObjectName("actionHistogram_Equalization_HE")
        self.actionFuzzy_HE_RGB = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("Icon/icons8-histogram-100 (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFuzzy_HE_RGB.setIcon(icon22)
        self.actionFuzzy_HE_RGB.setObjectName("actionFuzzy_HE_RGB")
        self.actionFuzzy_to_Grayscale = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("Icon/icons8-histogram-100 (5).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFuzzy_to_Grayscale.setIcon(icon23)
        self.actionFuzzy_to_Grayscale.setObjectName("actionFuzzy_to_Grayscale")
        self.actionOpen_Aritmatics_Panel = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("Icon/icons8-math-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Aritmatics_Panel.setIcon(icon24)
        self.actionOpen_Aritmatics_Panel.setObjectName("actionOpen_Aritmatics_Panel")
        self.actionIdentity = QtWidgets.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("Icon/icons8-full-image-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIdentity.setIcon(icon25)
        self.actionIdentity.setObjectName("actionIdentity")
        self.actionEdge_Detection_1 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_1.setObjectName("actionEdge_Detection_1")
        self.actionEdge_Detection_2 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_2.setObjectName("actionEdge_Detection_2")
        self.actionEdge_Detection_3 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_3.setObjectName("actionEdge_Detection_3")
        self.actionSharpen = QtWidgets.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("Icon/icons8-image-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSharpen.setIcon(icon26)
        self.actionSharpen.setObjectName("actionSharpen")
        self.actionUnsharp_Masking = QtWidgets.QAction(MainWindow)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("Icon/icons8-image-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnsharp_Masking.setIcon(icon27)
        self.actionUnsharp_Masking.setObjectName("actionUnsharp_Masking")
        self.actionAverage_Filter = QtWidgets.QAction(MainWindow)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("Icon/icons8-cmyk-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAverage_Filter.setIcon(icon28)
        self.actionAverage_Filter.setObjectName("actionAverage_Filter")
        self.actionLow_Pass_Filter = QtWidgets.QAction(MainWindow)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("Icon/icons8-cmyk-100 (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLow_Pass_Filter.setIcon(icon29)
        self.actionLow_Pass_Filter.setObjectName("actionLow_Pass_Filter")
        self.actionHigh_Pass_Filter = QtWidgets.QAction(MainWindow)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("Icon/icons8-cmyk-100 (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHigh_Pass_Filter.setIcon(icon30)
        self.actionHigh_Pass_Filter.setObjectName("actionHigh_Pass_Filter")
        self.actionBandstop_Filter = QtWidgets.QAction(MainWindow)
        icon102 = QtGui.QIcon()
        icon102.addPixmap(QtGui.QPixmap("Icon/bandstopfilter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBandstop_Filter.setIcon(icon102)
        self.actionBandstop_Filter.setObjectName("actionBandstop_Filter")
        self.actionPrewitt = QtWidgets.QAction(MainWindow)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("Icon/icons8-full-image-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrewitt.setIcon(icon31)
        self.actionPrewitt.setObjectName("actionPrewitt")
        self.actionSobel = QtWidgets.QAction(MainWindow)
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap("Icon/icons8-full-image-100 (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSobel.setIcon(icon32)
        self.actionSobel.setObjectName("actionSobel")
        self.actionRobert = QtWidgets.QAction(MainWindow)
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap("Icon/icons8-image-100x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRobert.setIcon(icon33)
        self.actionRobert.setObjectName("actionRobert")
        self.actionESquare_3 = QtWidgets.QAction(MainWindow)
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap("Icon/square 3x3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionESquare_3.setIcon(icon34)
        self.actionESquare_3.setObjectName("actionESquare_3")
        self.actionESquare_5 = QtWidgets.QAction(MainWindow)
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap("Icon/square 5x5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionESquare_5.setIcon(icon35)
        self.actionESquare_5.setObjectName("actionESquare_5")
        self.actionECross_3 = QtWidgets.QAction(MainWindow)
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap("Icon/icons8-cross-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionECross_3.setIcon(icon36)
        self.actionECross_3.setObjectName("actionECross_3")
        self.actionDSquare_3 = QtWidgets.QAction(MainWindow)
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap("Icon/square 3x3 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDSquare_3.setIcon(icon37)
        self.actionDSquare_3.setObjectName("actionDSquare_3")
        self.actionDSquare_5 = QtWidgets.QAction(MainWindow)
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap("Icon/square 5x5 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDSquare_5.setIcon(icon38)
        self.actionDSquare_5.setObjectName("actionDSquare_5")
        self.actionDCross_3 = QtWidgets.QAction(MainWindow)
        icon39 = QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap("Icon/icons8-cross-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDCross_3.setIcon(icon39)
        self.actionDCross_3.setObjectName("actionDCross_3")
        self.actionOSquare_9 = QtWidgets.QAction(MainWindow)
        icon40 = QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap("Icon/square 9x9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOSquare_9.setIcon(icon40)
        self.actionOSquare_9.setObjectName("actionOSquare_9")
        self.actionCSquare_9 = QtWidgets.QAction(MainWindow)
        icon41 = QtGui.QIcon()
        icon41.addPixmap(QtGui.QPixmap("Icon/square 9x9 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCSquare_9.setIcon(icon41)
        self.actionCSquare_9.setObjectName("actionCSquare_9")
        self.actionYellow = QtWidgets.QAction(MainWindow)
        icon42 = QtGui.QIcon()
        icon42.addPixmap(QtGui.QPixmap("Icon/yellow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionYellow.setIcon(icon42)
        self.actionYellow.setObjectName("actionYellow")
        self.actionCyan = QtWidgets.QAction(MainWindow)
        icon43 = QtGui.QIcon()
        icon43.addPixmap(QtGui.QPixmap("Icon/cyan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCyan.setIcon(icon43)
        self.actionCyan.setObjectName("actionCyan")
        self.actionPurple = QtWidgets.QAction(MainWindow)
        icon44 = QtGui.QIcon()
        icon44.addPixmap(QtGui.QPixmap("Icon/purple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPurple.setIcon(icon44)
        self.actionPurple.setObjectName("actionPurple")
        self.actionRed = QtWidgets.QAction(MainWindow)
        icon45 = QtGui.QIcon()
        icon45.addPixmap(QtGui.QPixmap("Icon/red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRed.setIcon(icon45)
        self.actionRed.setObjectName("actionRed")
        self.actionGreen = QtWidgets.QAction(MainWindow)
        icon46 = QtGui.QIcon()
        icon46.addPixmap(QtGui.QPixmap("Icon/green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGreen.setIcon(icon46)
        self.actionGreen.setObjectName("actionGreen")
        self.actionBlue = QtWidgets.QAction(MainWindow)
        icon47 = QtGui.QIcon()
        icon47.addPixmap(QtGui.QPixmap("Icon/blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBlue.setIcon(icon47)
        self.actionBlue.setObjectName("actionBlue")
        self.actionOrange = QtWidgets.QAction(MainWindow)
        icon48 = QtGui.QIcon()
        icon48.addPixmap(QtGui.QPixmap("Icon/orange.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOrange.setIcon(icon48)
        self.actionOrange.setObjectName("actionOrange")
        self.actionPink = QtWidgets.QAction(MainWindow)
        icon49 = QtGui.QIcon()
        icon49.addPixmap(QtGui.QPixmap("Icon/pink.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPink.setIcon(icon49)
        self.actionPink.setObjectName("actionPink")
        self.actionGray = QtWidgets.QAction(MainWindow)
        icon50 = QtGui.QIcon()
        icon50.addPixmap(QtGui.QPixmap("Icon/gray.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGray.setIcon(icon50)
        self.actionGray.setObjectName("actionGray")
        self.actionAverage = QtWidgets.QAction(MainWindow)
        icon51 = QtGui.QIcon()
        icon51.addPixmap(QtGui.QPixmap("Icon/icons8-rgba-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAverage.setIcon(icon51)
        self.actionAverage.setObjectName("actionAverage")
        self.actionLightness = QtWidgets.QAction(MainWindow)
        icon52 = QtGui.QIcon()
        icon52.addPixmap(QtGui.QPixmap("Icon/icons8-rgba-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLightness.setIcon(icon52)
        self.actionLightness.setObjectName("actionLightness")
        self.actionLuminance = QtWidgets.QAction(MainWindow)
        icon53 = QtGui.QIcon()
        icon53.addPixmap(QtGui.QPixmap("Icon/icons8-rgba-100 (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLuminance.setIcon(icon53)
        self.actionLuminance.setObjectName("actionLuminance")
        self.action1_Bit = QtWidgets.QAction(MainWindow)
        icon54 = QtGui.QIcon()
        icon54.addPixmap(QtGui.QPixmap("Icon/1bit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action1_Bit.setIcon(icon54)
        self.action1_Bit.setObjectName("action1_Bit")
        self.action2_Bit = QtWidgets.QAction(MainWindow)
        icon55 = QtGui.QIcon()
        icon55.addPixmap(QtGui.QPixmap("Icon/4bit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action2_Bit.setIcon(icon55)
        self.action2_Bit.setObjectName("action2_Bit")
        self.action3_Bit = QtWidgets.QAction(MainWindow)
        icon56 = QtGui.QIcon()
        icon56.addPixmap(QtGui.QPixmap("Icon/8bit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action3_Bit.setIcon(icon56)
        self.action3_Bit.setObjectName("action3_Bit")
        self.action4_Bit = QtWidgets.QAction(MainWindow)
        icon57 = QtGui.QIcon()
        icon57.addPixmap(QtGui.QPixmap("Icon/16bit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action4_Bit.setIcon(icon57)
        self.action4_Bit.setObjectName("action4_Bit")
        self.action5_Bit = QtWidgets.QAction(MainWindow)
        icon58 = QtGui.QIcon()
        icon58.addPixmap(QtGui.QPixmap("Icon/32bit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action5_Bit.setIcon(icon58)
        self.action5_Bit.setObjectName("action5_Bit")
        self.action6_Bit = QtWidgets.QAction(MainWindow)
        icon59 = QtGui.QIcon()
        icon59.addPixmap(QtGui.QPixmap("Icon/64bit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action6_Bit.setIcon(icon59)
        self.action6_Bit.setObjectName("action6_Bit")
        self.action7_Bit = QtWidgets.QAction(MainWindow)
        icon60 = QtGui.QIcon()
        icon60.addPixmap(QtGui.QPixmap("Icon/128bit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action7_Bit.setIcon(icon60)
        self.action7_Bit.setObjectName("action7_Bit")
        self.action8_Bit = QtWidgets.QAction(MainWindow)
        icon61 = QtGui.QIcon()
        icon61.addPixmap(QtGui.QPixmap("Icon/256bit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action8_Bit.setIcon(icon61)
        self.action8_Bit.setObjectName("action8_Bit")
        self.actionGaussian_Blur_3x3 = QtWidgets.QAction(MainWindow)
        icon62 = QtGui.QIcon()
        icon62.addPixmap(QtGui.QPixmap("Icon/icons8-blur-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGaussian_Blur_3x3.setIcon(icon62)
        self.actionGaussian_Blur_3x3.setObjectName("actionGaussian_Blur_3x3")
        self.actionGaussian_Blur_5x5 = QtWidgets.QAction(MainWindow)
        icon63 = QtGui.QIcon()
        icon63.addPixmap(QtGui.QPixmap("Icon/icons8-blur-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGaussian_Blur_5x5.setIcon(icon63)
        self.actionGaussian_Blur_5x5.setObjectName("actionGaussian_Blur_5x5")
        self.actionEnable = QtWidgets.QAction(MainWindow)
        self.actionEnable.setObjectName("actionEnable")
        self.actionDisable = QtWidgets.QAction(MainWindow)
        self.actionDisable.setObjectName("actionDisable")
        self.actionBox = QtWidgets.QAction(MainWindow)
        self.actionBox.setObjectName("actionBox")
        self.actionWindows = QtWidgets.QAction(MainWindow)
        self.actionWindows.setObjectName("actionWindows")
        self.actionNo_Border = QtWidgets.QAction(MainWindow)
        self.actionNo_Border.setObjectName("actionNo_Border")
        self.actionSegoe_UI = QtWidgets.QAction(MainWindow)
        self.actionSegoe_UI.setObjectName("actionSegoe_UI")
        self.action8_pt = QtWidgets.QAction(MainWindow)
        self.action8_pt.setObjectName("action8_pt")
        self.action9_pt = QtWidgets.QAction(MainWindow)
        self.action9_pt.setObjectName("action9_pt")
        self.action10_pt = QtWidgets.QAction(MainWindow)
        self.action10_pt.setObjectName("action10_pt")
        self.action11_pt = QtWidgets.QAction(MainWindow)
        self.action11_pt.setObjectName("action11_pt")
        self.action12_pt = QtWidgets.QAction(MainWindow)
        self.action12_pt.setObjectName("action12_pt")
        self.actionAbout_Apps = QtWidgets.QAction(MainWindow)
        icon64 = QtGui.QIcon()
        icon64.addPixmap(QtGui.QPixmap("Icon/icons8-apps-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_Apps.setIcon(icon64)
        self.actionAbout_Apps.setObjectName("actionAbout_Apps")
        self.actionCheck_For_Updates = QtWidgets.QAction(MainWindow)
        icon65 = QtGui.QIcon()
        icon65.addPixmap(QtGui.QPixmap("Icon/icons8-update-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCheck_For_Updates.setIcon(icon65)
        self.actionCheck_For_Updates.setObjectName("actionCheck_For_Updates")
        self.actionEnglish_US = QtWidgets.QAction(MainWindow)
        self.actionEnglish_US.setObjectName("actionEnglish_US")
        self.actionIndonesia = QtWidgets.QAction(MainWindow)
        self.actionIndonesia.setObjectName("actionIndonesia")
        self.actionRemove_Background = QtWidgets.QAction(MainWindow)
        self.actionRemove_Background.setObjectName("actionRemove_Background")
        self.actionAI_HD_Photo_Upscaling = QtWidgets.QAction(MainWindow)
        self.actionAI_HD_Photo_Upscaling.setObjectName("actionAI_HD_Photo_Upscaling")
        self.actionAI_Image_Generator = QtWidgets.QAction(MainWindow)
        self.actionAI_Image_Generator.setObjectName("actionAI_Image_Generator")
        self.actionLucida_Sans = QtWidgets.QAction(MainWindow)
        self.actionLucida_Sans.setObjectName("actionLucida_Sans")
        self.actionPerpetua = QtWidgets.QAction(MainWindow)
        self.actionPerpetua.setObjectName("actionPerpetua")
        self.actionCanny = QtWidgets.QAction(MainWindow)
        icon66 = QtGui.QIcon()
        icon66.addPixmap(QtGui.QPixmap("Icon/icons8-full-image-100 (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCanny.setIcon(icon66)
        self.actionCanny.setObjectName("actionCanny")
        self.actionKirsh = QtWidgets.QAction(MainWindow)
        iconkirsh = QtGui.QIcon()
        iconkirsh.addPixmap(QtGui.QPixmap("Icon/icons8-full-image-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionKirsh.setIcon(iconkirsh)
        self.actionKirsh.setObjectName("actionKirsh")
        self.actionScharr = QtWidgets.QAction(MainWindow)
        iconScharr = QtGui.QIcon()
        iconScharr.addPixmap(QtGui.QPixmap("Icon/icons8-full-image-100 (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScharr.setIcon(iconScharr)
        self.actionScharr.setObjectName("actionScharr")
        self.actionLaplacian = QtWidgets.QAction(MainWindow)
        iconLaplacian = QtGui.QIcon()
        iconLaplacian.addPixmap(QtGui.QPixmap("Icon/icons8-image-100x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLaplacian.setIcon(iconLaplacian)
        self.actionLaplacian.setObjectName("actionLaplacian")
        self.actionLaplacian_of_Gaussian = QtWidgets.QAction(MainWindow)
        iconLaplacian_of_Gaussian = QtGui.QIcon()
        iconLaplacian_of_Gaussian.addPixmap(QtGui.QPixmap("Icon/icons8-full-image-100 (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLaplacian_of_Gaussian.setIcon(iconLaplacian_of_Gaussian)
        self.actionLaplacian_of_Gaussian.setObjectName("actionLaplacian_of_Gaussian")
        self.actionFlipH = QtWidgets.QAction(MainWindow)
        icon67 = QtGui.QIcon()
        icon67.addPixmap(QtGui.QPixmap("Icon/icons8-flip-horizontal-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFlipH.setIcon(icon67)
        self.actionFlipH.setObjectName("actionFlipH")
        self.actionFlipV = QtWidgets.QAction(MainWindow)
        icon68 = QtGui.QIcon()
        icon68.addPixmap(QtGui.QPixmap("Icon/icons8-flip-vertical-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFlipV.setIcon(icon68)
        self.actionFlipV.setObjectName("actionFlipV")
        self.action90_degree = QtWidgets.QAction(MainWindow)
        icon69 = QtGui.QIcon()
        icon69.addPixmap(QtGui.QPixmap("Icon/andLogo2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action90_degree.setIcon(icon69)
        self.action90_degree.setObjectName("action90_degree")
        self.action180_degree = QtWidgets.QAction(MainWindow)
        icon70 = QtGui.QIcon()
        icon70.addPixmap(QtGui.QPixmap("Icon/andLogo3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action180_degree.setIcon(icon70)
        self.action180_degree.setObjectName("action180_degree")
        self.Set_value = QtWidgets.QAction(MainWindow)
        icon71 = QtGui.QIcon()
        icon71.addPixmap(QtGui.QPixmap("Icon/iconrotation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Set_value.setIcon(icon71)
        self.Set_value.setObjectName("Set_value")
        self.actionTranslation = QtWidgets.QAction(MainWindow)
        icon72 = QtGui.QIcon()
        icon72.addPixmap(QtGui.QPixmap("Icon/icons8-translation-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTranslation.setIcon(icon72)
        self.actionTranslation.setObjectName("actionTranslation")
        self.actionCrop = QtWidgets.QAction(MainWindow)
        icon73 = QtGui.QIcon()
        icon73.addPixmap(QtGui.QPixmap("Icon/icons8-cropping-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCrop.setIcon(icon73)
        self.actionCrop.setObjectName("actionCrop")
        self.actionUniform_Scaling = QtWidgets.QAction(MainWindow)
        icon74 = QtGui.QIcon()
        icon74.addPixmap(QtGui.QPixmap("Icon/icons8-fit-to-width-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUniform_Scaling.setIcon(icon74)
        self.actionUniform_Scaling.setObjectName("actionUniform_Scaling")
        self.actionNon_Uniform_Scaling = QtWidgets.QAction(MainWindow)
        icon75 = QtGui.QIcon()
        icon75.addPixmap(QtGui.QPixmap("Icon/icons8-fit-to-width-100 (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNon_Uniform_Scaling.setIcon(icon75)
        self.actionNon_Uniform_Scaling.setObjectName("actionNon_Uniform_Scaling")
        self.actionThreshold = QtWidgets.QAction(MainWindow)
        self.actionThreshold.setObjectName("actionThreshold")
        self.actionSegmentasi_Citra = QtWidgets.QAction(MainWindow)
        icon76 = QtGui.QIcon()
        icon76.addPixmap(QtGui.QPixmap("Icon/icons8-no-image-gallery-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSegmentasi_Citra.setIcon(icon76)
        self.actionSegmentasi_Citra.setObjectName("actionSegmentasi_Citra")
        self.actionROI = QtWidgets.QAction(MainWindow)
        icon77 = QtGui.QIcon()
        icon77.addPixmap(QtGui.QPixmap("Icon/icons8-full-image-100a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionROI.setIcon(icon77)
        self.actionROI.setObjectName("actionROI")
        self.actionEkstraksi_Warna = QtWidgets.QAction(MainWindow)
        self.actionEkstraksi_Warna.setObjectName("actionEkstraksi_Warna")
        self.actionColor_RGB = QtWidgets.QAction(MainWindow)
        icon78 = QtGui.QIcon()
        icon78.addPixmap(QtGui.QPixmap("Icon/icons8-rgb-100a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColor_RGB.setIcon(icon78)
        self.actionColor_RGB.setObjectName("actionColor_RGB")
        self.actionColor_RGB_to_HSV = QtWidgets.QAction(MainWindow)
        icon79 = QtGui.QIcon()
        icon79.addPixmap(QtGui.QPixmap("Icon/icons8-color-wheel-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColor_RGB_to_HSV.setIcon(icon79)
        self.actionColor_RGB_to_HSV.setObjectName("actionColor_RGB_to_HSV")
        self.actionColor_RGB_to_YCrCb = QtWidgets.QAction(MainWindow)
        icon80 = QtGui.QIcon()
        icon80.addPixmap(QtGui.QPixmap("Icon/icons8-rgb-color-wheel-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColor_RGB_to_YCrCb.setIcon(icon80)
        self.actionColor_RGB_to_YCrCb.setObjectName("actionColor_RGB_to_YCrCb")
        self.actionThreshold_2 = QtWidgets.QAction(MainWindow)
        icon81 = QtGui.QIcon()
        icon81.addPixmap(QtGui.QPixmap("Icon/icons8-electrical-threshold-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionThreshold_2.setIcon(icon81)
        self.actionThreshold_2.setObjectName("actionThreshold_2")
        self.actionColor_RGB_to_CMYK = QtWidgets.QAction(MainWindow)
        icon82 = QtGui.QIcon()
        icon82.addPixmap(QtGui.QPixmap("Icon/icons8-cmyk-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColor_RGB_to_CMYK.setIcon(icon82)
        self.actionColor_RGB_to_CMYK.setObjectName("actionColor_RGB_to_CMYK")
        self.action270_degree = QtWidgets.QAction(MainWindow)
        icon83 = QtGui.QIcon()
        icon83.addPixmap(QtGui.QPixmap("Icon/270degree.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action270_degree.setIcon(icon83)
        self.action270_degree.setObjectName("action270_degree")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menuHistogram.addAction(self.actionInput)
        self.menuHistogram.addAction(self.actionOutput)
        self.menuHistogram.addAction(self.actionInput_Output)
        self.menuView.addAction(self.menuHistogram.menuAction())
        self.menuRGB.addAction(self.actionRed)
        self.menuRGB.addAction(self.actionGreen)
        self.menuRGB.addAction(self.actionBlue)
        self.menuRGB.addSeparator()
        self.menuRGB.addAction(self.actionCyan)
        self.menuRGB.addAction(self.actionGray)
        self.menuRGB.addAction(self.actionOrange)
        self.menuRGB.addAction(self.actionPink)
        self.menuRGB.addAction(self.actionPurple)
        self.menuRGB.addAction(self.actionYellow)
        self.menuRGB_to_Grayscale.addAction(self.actionAverage)
        self.menuRGB_to_Grayscale.addAction(self.actionLightness)
        self.menuRGB_to_Grayscale.addAction(self.actionLuminance)
        self.menuBit_Depth.addAction(self.action1_Bit)
        self.menuBit_Depth.addAction(self.action2_Bit)
        self.menuBit_Depth.addAction(self.action3_Bit)
        self.menuBit_Depth.addAction(self.action4_Bit)
        self.menuBit_Depth.addAction(self.action5_Bit)
        self.menuBit_Depth.addAction(self.action6_Bit)
        self.menuBit_Depth.addAction(self.action7_Bit)
        self.menuBit_Depth.addAction(self.action8_Bit)
        self.menuColor.addAction(self.menuRGB.menuAction())
        self.menuColor.addAction(self.menuRGB_to_Grayscale.menuAction())
        self.menuColor.addSeparator()
        self.menuColor.addAction(self.actionBrightness)
        self.menuColor.addAction(self.actionBrightness_Contrast)
        self.menuColor.addAction(self.actionThreshold_2)
        self.menuColor.addAction(self.actionLog_Brightness)
        self.menuColor.addSeparator()
        self.menuColor.addAction(self.actionInvers)
        self.menuColor.addAction(self.menuBit_Depth.menuAction())
        self.menuColor.addAction(self.actionGamma_Correction)
        self.menuImage_Processing.addAction(self.actionHistogram_Equalization_HE)
        self.menuImage_Processing.addAction(self.actionFuzzy_HE_RGB)
        self.menuImage_Processing.addAction(self.actionFuzzy_to_Grayscale)
        self.menuAritmatics_Operation.addAction(self.actionOpen_Aritmatics_Panel)
        self.menuGaussian_Blur.addAction(self.actionGaussian_Blur_3x3)
        self.menuGaussian_Blur.addAction(self.actionGaussian_Blur_5x5)
        self.menuFilter.addAction(self.actionIdentity)
        self.menuFilter.addAction(self.actionSharpen)
        self.menuFilter.addAction(self.menuGaussian_Blur.menuAction())
        self.menuFilter.addAction(self.actionUnsharp_Masking)
        self.menuFilter.addSeparator()
        self.menuFilter.addAction(self.actionAverage_Filter)
        self.menuFilter.addAction(self.actionLow_Pass_Filter)
        self.menuFilter.addAction(self.actionHigh_Pass_Filter)
        self.menuFilter.addAction(self.actionBandstop_Filter)
        self.menuEdge_Detection.addAction(self.actionPrewitt)
        self.menuEdge_Detection.addAction(self.actionSobel)
        self.menuEdge_Detection.addAction(self.actionRobert)
        self.menuEdge_Detection.addAction(self.actionCanny)
        self.menuEdge_Detection.addSeparator()
        self.menuEdge_Detection.addAction(self.actionKirsh)
        self.menuEdge_Detection.addAction(self.actionScharr)
        self.menuEdge_Detection.addAction(self.actionLaplacian)
        self.menuEdge_Detection.addAction(self.actionLaplacian_of_Gaussian)
        self.menuErosion.addAction(self.actionESquare_3)
        self.menuErosion.addAction(self.actionESquare_5)
        self.menuErosion.addAction(self.actionECross_3)
        self.menuOpening.addAction(self.actionOSquare_9)
        self.menuDilation.addAction(self.actionDSquare_3)
        self.menuDilation.addAction(self.actionDSquare_5)
        self.menuDilation.addAction(self.actionDCross_3)
        self.menuClosing.addAction(self.actionCSquare_9)
        self.menuMorphology.addAction(self.menuErosion.menuAction())
        self.menuMorphology.addAction(self.menuDilation.menuAction())
        self.menuMorphology.addAction(self.menuOpening.menuAction())
        self.menuMorphology.addAction(self.menuClosing.menuAction())
        self.menuType_Font.addAction(self.actionSegoe_UI)
        self.menuType_Font.addAction(self.actionLucida_Sans)
        self.menuType_Font.addAction(self.actionPerpetua)
        self.menuAuto_Fit_Image.addAction(self.actionEnable)
        self.menuAuto_Fit_Image.addAction(self.actionDisable)
        self.menuInputBorderStyle.addAction(self.actionBox)
        self.menuInputBorderStyle.addAction(self.actionWindows)
        self.menuInputBorderStyle.addAction(self.actionNo_Border)
        self.menuSize_Font.addAction(self.action8_pt)
        self.menuSize_Font.addAction(self.action9_pt)
        self.menuSize_Font.addAction(self.action10_pt)
        self.menuSize_Font.addAction(self.action11_pt)
        self.menuSize_Font.addAction(self.action12_pt)
        self.menuAppearance.addAction(self.menuInputBorderStyle.menuAction())
        self.menuAppearance.addAction(self.menuAuto_Fit_Image.menuAction())
        self.menuAppearance.addAction(self.menuType_Font.menuAction())
        self.menuAppearance.addAction(self.menuSize_Font.menuAction())
        self.menuLanguage.addAction(self.actionEnglish_US)
        self.menuLanguage.addAction(self.actionIndonesia)
        self.menuThird_Apps.addAction(self.actionAI_HD_Photo_Upscaling)
        self.menuThird_Apps.addAction(self.actionAI_Image_Generator)
        self.menuAbout.addAction(self.actionSegmentasi_Citra)
        self.menuAbout.addAction(self.actionROI)
        self.menuAbout.addAction(self.actionRemove_Background)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.menuAppearance.menuAction())
        self.menuAbout.addAction(self.menuLanguage.menuAction())
        self.menuAbout.addAction(self.menuThird_Apps.menuAction())
        self.menuAbout_2.addAction(self.actionAbout_Apps)
        self.menuAbout_2.addAction(self.actionCheck_For_Updates)
        self.menuRotation.addAction(self.Set_value)
        self.menuRotation.addAction(self.action90_degree)
        self.menuRotation.addAction(self.action180_degree)
        self.menuRotation.addAction(self.action270_degree)
        self.menuScaling.addAction(self.actionUniform_Scaling)
        self.menuScaling.addAction(self.actionNon_Uniform_Scaling)
        self.menuGeometry.addAction(self.actionFlipH)
        self.menuGeometry.addAction(self.actionFlipV)
        self.menuGeometry.addAction(self.actionCrop)
        self.menuGeometry.addAction(self.actionTranslation)
        self.menuGeometry.addAction(self.menuRotation.menuAction())
        self.menuGeometry.addAction(self.menuScaling.menuAction())
        self.menuFeature_Extraction.addAction(self.actionColor_RGB_to_HSV)
        self.menuFeature_Extraction.addAction(self.actionColor_RGB)
        self.menuFeature_Extraction.addAction(self.actionColor_RGB_to_YCrCb)
        self.menuFeature_Extraction.addAction(self.actionColor_RGB_to_CMYK)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuColor.menuAction())
        self.menubar.addAction(self.menuImage_Processing.menuAction())
        self.menubar.addAction(self.menuAritmatics_Operation.menuAction())
        self.menubar.addAction(self.menuFilter.menuAction())
        self.menubar.addAction(self.menuEdge_Detection.menuAction())
        self.menubar.addAction(self.menuGeometry.menuAction())
        self.menubar.addAction(self.menuMorphology.menuAction())
        self.menubar.addAction(self.menuFeature_Extraction.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuAbout_2.menuAction())

        # self.image = QtGui.QImage()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aplikasi Pengolah Citra"))
        self.label.setText(_translate("MainWindow", "Gambar Masukan"))
        self.label_2.setText(_translate("MainWindow", "Gambar Keluaran"))
        self.labelEfek.setText(_translate("MainWindow", "Efek :"))
        self.labelInput_6.setText(_translate("MainWindow", "*Klik efek untuk menampilkannya pada preview "))
        self.buttonClear.setText(_translate("MainWindow", "Clear Image"))
        self.buttonSetImage.setText(_translate("MainWindow", "Set Image"))
        self.buttonUndo.setText(_translate("MainWindow", "Undo Efek"))
        self.buttonEffect1.setText(_translate("MainWindow", "Tidak ada efek 1"))
        self.buttonEffect2.setText(_translate("MainWindow", "Tidak ada efek 2"))
        self.buttonEffect3.setText(_translate("MainWindow", "Tidak ada efek 3"))
        self.buttonSet.setText(_translate("MainWindow", "Atur ke efek 1"))
        self.buttonTetapImport.setText(_translate("MainWindow", "Tetap Impor"))
        self.buttonSimpan.setText(_translate("MainWindow", "Simpan"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHistogram.setTitle(_translate("MainWindow", "Histogram"))
        self.menuColor.setTitle(_translate("MainWindow", "Color"))
        self.menuRGB.setTitle(_translate("MainWindow", "RGB"))
        self.menuRGB_to_Grayscale.setTitle(_translate("MainWindow", "RGB to Grayscale"))
        self.menuBit_Depth.setTitle(_translate("MainWindow", "Bit Depth"))
        self.menuImage_Processing.setTitle(_translate("MainWindow", "Image Processing"))
        self.menuAritmatics_Operation.setTitle(_translate("MainWindow", "Aritmatics Operations"))
        self.menuFilter.setTitle(_translate("MainWindow", "Filter"))
        self.menuGaussian_Blur.setTitle(_translate("MainWindow", "Gaussian Blur"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuMorphology.setTitle(_translate("MainWindow", "Morphology"))
        self.menuErosion.setTitle(_translate("MainWindow", "Erosion"))
        self.menuOpening.setTitle(_translate("MainWindow", "Opening"))
        self.menuDilation.setTitle(_translate("MainWindow", "Dilation"))
        self.menuClosing.setTitle(_translate("MainWindow", "Closing"))
        self.menuAbout.setTitle(_translate("MainWindow", "Others"))
        self.menuAppearance.setTitle(_translate("MainWindow", "Appearance"))
        self.menuType_Font.setTitle(_translate("MainWindow", "Type Font"))
        self.menuAuto_Fit_Image.setTitle(_translate("MainWindow", "Auto Fit Image"))
        self.menuInputBorderStyle.setTitle(_translate("MainWindow", "InputBorderStyle"))
        self.menuSize_Font.setTitle(_translate("MainWindow", "Size Font"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.menuThird_Apps.setTitle(_translate("MainWindow", "Third Apps"))
        self.menuAbout_2.setTitle(_translate("MainWindow", "About"))
        self.menuGeometry.setTitle(_translate("MainWindow", "Geometry"))
        self.menuRotation.setTitle(_translate("MainWindow", "Rotation"))
        self.menuScaling.setTitle(_translate("MainWindow", "Scaling"))
        self.menuFeature_Extraction.setTitle(_translate("MainWindow", "Feature Extraction"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionInput.setText(_translate("MainWindow", "Input"))
        self.actionOutput.setText(_translate("MainWindow", "Output"))
        self.actionInput_Output.setText(_translate("MainWindow", "Input Output"))
        self.actionBrightness.setText(_translate("MainWindow", "Brightness"))
        self.actionBrightness_Contrast.setText(_translate("MainWindow", "Brightness - Contrast"))
        self.actionLog_Brightness.setText(_translate("MainWindow", "Log Brightness"))
        self.actionInvers.setText(_translate("MainWindow", "Invers"))
        self.actionGamma_Correction.setText(_translate("MainWindow", "Gamma Correction"))
        self.actionHistogram_Equalization_HE.setText(_translate("MainWindow", "Histogram Equalization (HE)"))
        self.actionFuzzy_HE_RGB.setText(_translate("MainWindow", "Fuzzy HE RGB"))
        self.actionFuzzy_to_Grayscale.setText(_translate("MainWindow", "Fuzzy to Grayscale"))
        self.actionOpen_Aritmatics_Panel.setText(_translate("MainWindow", "Open Aritmatics Panel"))
        self.actionIdentity.setText(_translate("MainWindow", "Identity"))
        self.actionEdge_Detection_1.setText(_translate("MainWindow", "Edge Detection 1"))
        self.actionEdge_Detection_2.setText(_translate("MainWindow", "Edge Detection 2"))
        self.actionEdge_Detection_3.setText(_translate("MainWindow", "Edge Detection 3"))
        self.actionSharpen.setText(_translate("MainWindow", "Sharpen"))
        self.actionUnsharp_Masking.setText(_translate("MainWindow", "Unsharp Masking"))
        self.actionAverage_Filter.setText(_translate("MainWindow", "Average Filter"))
        self.actionLow_Pass_Filter.setText(_translate("MainWindow", "Low Pass Filter"))
        self.actionHigh_Pass_Filter.setText(_translate("MainWindow", "High Pass Filter"))
        self.actionBandstop_Filter.setText(_translate("MainWindow", "Bandstop Filter"))
        self.actionPrewitt.setText(_translate("MainWindow", "Prewitt"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionRobert.setText(_translate("MainWindow", "Robert"))
        self.actionESquare_3.setText(_translate("MainWindow", "Square 3"))
        self.actionESquare_5.setText(_translate("MainWindow", "Square 5"))
        self.actionECross_3.setText(_translate("MainWindow", "Cross 3"))
        self.actionDSquare_3.setText(_translate("MainWindow", "Square 3"))
        self.actionDSquare_5.setText(_translate("MainWindow", "Square 5"))
        self.actionDCross_3.setText(_translate("MainWindow", "Cross 3"))
        self.actionOSquare_9.setText(_translate("MainWindow", "Square 9"))
        self.actionCSquare_9.setText(_translate("MainWindow", "Square 9"))
        self.actionYellow.setText(_translate("MainWindow", "Yellow"))
        self.actionCyan.setText(_translate("MainWindow", "Cyan"))
        self.actionPurple.setText(_translate("MainWindow", "Purple"))
        self.actionRed.setText(_translate("MainWindow", "Red"))
        self.actionGreen.setText(_translate("MainWindow", "Green"))
        self.actionBlue.setText(_translate("MainWindow", "Blue"))
        self.actionOrange.setText(_translate("MainWindow", "Orange"))
        self.actionPink.setText(_translate("MainWindow", "Pink"))
        self.actionGray.setText(_translate("MainWindow", "Gray"))
        self.actionAverage.setText(_translate("MainWindow", "Average"))
        self.actionLightness.setText(_translate("MainWindow", "Lightness"))
        self.actionLuminance.setText(_translate("MainWindow", "Luminance"))
        self.action1_Bit.setText(_translate("MainWindow", "1 Bit"))
        self.action2_Bit.setText(_translate("MainWindow", "2 Bit"))
        self.action3_Bit.setText(_translate("MainWindow", "3 Bit"))
        self.action4_Bit.setText(_translate("MainWindow", "4 Bit"))
        self.action5_Bit.setText(_translate("MainWindow", "5 Bit"))
        self.action6_Bit.setText(_translate("MainWindow", "6 Bit"))
        self.action7_Bit.setText(_translate("MainWindow", "7 Bit"))
        self.action8_Bit.setText(_translate("MainWindow", "8 Bit"))
        self.actionGaussian_Blur_3x3.setText(_translate("MainWindow", "Gaussian Blur 3x3"))
        self.actionGaussian_Blur_5x5.setText(_translate("MainWindow", "Gaussian Blur 5x5"))
        self.actionEnable.setText(_translate("MainWindow", "Enable"))
        self.actionDisable.setText(_translate("MainWindow", "Disable"))
        self.actionBox.setText(_translate("MainWindow", "Box"))
        self.actionWindows.setText(_translate("MainWindow", "Windows"))
        self.actionNo_Border.setText(_translate("MainWindow", "No Border"))
        self.actionSegoe_UI.setText(_translate("MainWindow", "Segoe UI"))
        self.action8_pt.setText(_translate("MainWindow", "8 pt"))
        self.action9_pt.setText(_translate("MainWindow", "9 pt"))
        self.action10_pt.setText(_translate("MainWindow", "10 pt"))
        self.action11_pt.setText(_translate("MainWindow", "11 pt"))
        self.action12_pt.setText(_translate("MainWindow", "12 pt"))
        self.actionAbout_Apps.setText(_translate("MainWindow", "About Apps"))
        self.actionCheck_For_Updates.setText(_translate("MainWindow", "Check For Updates"))
        self.actionEnglish_US.setText(_translate("MainWindow", "English (US)"))
        self.actionIndonesia.setText(_translate("MainWindow", "Indonesia"))
        self.actionRemove_Background.setText(_translate("MainWindow", "Remove Background"))
        self.actionAI_HD_Photo_Upscaling.setText(_translate("MainWindow", "AI HD Photo and Upscaling"))
        self.actionAI_Image_Generator.setText(_translate("MainWindow", "AI Image Generator"))
        self.actionLucida_Sans.setText(_translate("MainWindow", "Lucida Sans"))
        self.actionPerpetua.setText(_translate("MainWindow", "Perpetua"))
        self.actionCanny.setText(_translate("MainWindow", "Canny"))
        self.actionKirsh.setText(_translate("MainWindow", "Kirsh"))
        self.actionScharr.setText(_translate("MainWindow", "Scharr"))
        self.actionLaplacian.setText(_translate("MainWindow", "Laplacian"))
        self.actionLaplacian_of_Gaussian.setText(_translate("MainWindow", "Laplacian of Gaussian"))
        self.actionFlipH.setText(_translate("MainWindow", "Flip Horizontal"))
        self.actionFlipV.setText(_translate("MainWindow", "Flip Vertical"))
        self.action90_degree.setText(_translate("MainWindow", "90 degree"))
        self.action180_degree.setText(_translate("MainWindow", "180 degree"))
        self.Set_value.setText(_translate("MainWindow", "Set Value"))
        self.actionTranslation.setText(_translate("MainWindow", "Translation"))
        self.actionCrop.setText(_translate("MainWindow", "Cropping"))
        self.actionUniform_Scaling.setText(_translate("MainWindow", "Uniform Scaling"))
        self.actionNon_Uniform_Scaling.setText(_translate("MainWindow", "Non-Uniform Scaling"))
        self.actionThreshold.setText(_translate("MainWindow", "Threshold"))
        self.actionSegmentasi_Citra.setText(_translate("MainWindow", "Segmentasi Citra"))
        self.actionROI.setText(_translate("MainWindow", "ROI"))
        self.actionEkstraksi_Warna.setText(_translate("MainWindow", "Ekstraksi Warna"))
        self.actionColor_RGB.setText(_translate("MainWindow", "Color RGB to HSL"))
        self.actionColor_RGB_to_HSV.setText(_translate("MainWindow", "Color RGB to HSV"))
        self.actionColor_RGB_to_YCrCb.setText(_translate("MainWindow", "Color RGB to YCrCb"))
        self.actionThreshold_2.setText(_translate("MainWindow", "Threshold"))
        self.actionColor_RGB_to_CMYK.setText(_translate("MainWindow", "Color RGB to CMYK"))
        self.action270_degree.setText(_translate("MainWindow", "270 degree"))


        # ----------------------------------------------------------------------------------------------------------
        # PENDEFINISIAN OBJEK dan PENGATURAN TAMPILAN-----------------------------------------------------------------------------------------
        # mengosongkan data input dan output pixmap serta mengosongkan data String
        self.pixmap1 = None
        self.pixmap2 = None
        self.pixmap3 = None
        self.pixmap4 = None
        self.pixmap5 = None
        self.input_pixmap1 = None
        self.stringefek1 = None
        self.stringefek2 = None
        self.stringefek3 = None
        self.image_path = None
        self.width = None
        self.height = None

        # inisiasi objek timer, mengatur tampilan image preview dan menyembunyikan tombol
        self.timer = QTimer()
        self.timerEfek = QTimer()
        self.timerEfek1 = QTimer()
        self.pbPreview.setVisible(False)
        self.buttonTetapImport.setVisible(False)
        self.action90_degree.setVisible(False)
        self.action180_degree.setVisible(False)
        self.action180_degree.setVisible(False)
        self.action270_degree.setVisible(False)
        self.buttonEffect1.setVisible(False)
        self.buttonEffect2.setVisible(False)
        self.buttonEffect3.setVisible(False)
        self.labelEfek.setVisible(False)
        self.buttonSet.setVisible(False)
        self.buttonUndo.setVisible(False)
        self.labelInput_6.setVisible(False)
        self.buttonSimpan.setVisible(False)
        self.label.setVisible(False)
        self.label_2.setVisible(False)
        self.buttonSetImage.setVisible(False)

        # FUNGSI AKSI PADA MENU -----------------------------------------------------------------------------------------
        
        # File
        self.actionOpen.triggered.connect(self.loadImage) 
        self.actionSave_As.triggered.connect(self.saveImage)
        self.actionExit.triggered.connect(self.exitApplication)
        
        # self.buttonClear.clicked.connect(self.load_data)
        self.actionYellow.triggered.connect(self.applyYellow)
        self.actionRed.triggered.connect(self.applyRed)
        self.actionGreen.triggered.connect(self.applyGreen)
        self.actionOrange.triggered.connect(self.applyOrange)
        self.actionCyan.triggered.connect(self.applyCyan)
        self.actionBlue.triggered.connect(self.applyBlue)
        self.actionPink.triggered.connect(self.applyPink)
        self.actionGray.triggered.connect(self.applyGray)
        self.actionPurple.triggered.connect(self.applyPurple)
        self.actionAverage.triggered.connect(self.convertToGreyscaleAverage)
        # self.actionAverage_Filter.triggered.connect(self.convertToGreyscaleAverage)
        self.actionLightness.triggered.connect(self.convertToGreyscaleLightness) 
        self.actionLuminance.triggered.connect(self.convertToGreyscaleLuminance)
        self.actionBrightness.triggered.connect(self.applyContrastEffect)
        self.actionBrightness_Contrast.triggered.connect(self.showBrightnessContrastDialog)
        self.actionInvers.triggered.connect(self.convertToInvers)
        self.actionThreshold_2.triggered.connect(self.applyThreshold)
        self.actionLog_Brightness.triggered.connect(self.showLogBrightness)
        self.action1_Bit.triggered.connect(self.apply1Bit)
        self.action2_Bit.triggered.connect(self.apply2Bit)
        self.action3_Bit.triggered.connect(self.apply3Bit)
        self.action4_Bit.triggered.connect(self.apply4Bit)
        self.action5_Bit.triggered.connect(self.apply5Bit)
        self.action6_Bit.triggered.connect(self.apply6Bit)
        self.action7_Bit.triggered.connect(self.apply7Bit)
        self.action8_Bit.triggered.connect(self.apply8Bit)
        self.actionHistogram_Equalization_HE.triggered.connect(self.applyHistogramEqualization)
        self.actionFuzzy_HE_RGB.triggered.connect(self.fuzzy_he_rgb)
        self.actionFuzzy_to_Grayscale.triggered.connect(self.fuzzy_greyscale)
        self.actionOpen_Aritmatics_Panel.triggered.connect(self.open_aritmatics_panel)
        self.actionIdentity.triggered.connect(self.applyIdentity)
        self.actionSharpen.triggered.connect(self.applySharpen)
        self.actionGaussian_Blur_3x3.triggered.connect(self.applyGaussianBlur3)
        self.actionGaussian_Blur_5x5.triggered.connect(self.applyGaussianBlur5)
        self.actionUnsharp_Masking.triggered.connect(self.applyUnsharpMasking)
        self.actionAverage_Filter.triggered.connect(self.applyAverageFilter)
        self.actionLow_Pass_Filter.triggered.connect(self.applyLowPassFilter)
        self.actionHigh_Pass_Filter.triggered.connect(self.applyHighPassFilter)
        self.actionBandstop_Filter.triggered.connect(self.applyBandstopFilter)
        self.actionPrewitt.triggered.connect(self.applyPrewitt)
        self.actionSobel.triggered.connect(self.applySobel)
        self.actionRobert.triggered.connect(self.applyRobert)
        self.actionCanny.triggered.connect(self.applyCanny)
        self.actionLaplacian.triggered.connect(self.applyLaplacianFilter)
        self.actionLaplacian_of_Gaussian.triggered.connect(self.applyLaplacianOfGaussianFilter)
        self.actionFlipH.triggered.connect(self.flip_horizontal)
        self.actionFlipV.triggered.connect(self.flip_vertical)
        self.actionCrop.triggered.connect(self.applyCropping)
        self.actionTranslation.triggered.connect(self.applyTranslasi)
        self.Set_value.triggered.connect(self.rotate)
        self.actionUniform_Scaling.triggered.connect(self.applyUniformScaling)
        self.actionNon_Uniform_Scaling.triggered.connect(self.applyNonUniformScaling)
        self.actionESquare_3.triggered.connect(self.applyErotionSquare3)
        self.actionESquare_5.triggered.connect(self.applyErotionSquare5)
        self.actionECross_3.triggered.connect(self.applyErotionCross3)
        self.actionDSquare_3.triggered.connect(self.applyDilationSquare3)
        self.actionDSquare_5.triggered.connect(self.applyDilationSquare5)
        self.actionDCross_3.triggered.connect(self.applyDilationCross3)
        self.actionOSquare_9.triggered.connect(self.applyOpeningSquare9)
        self.actionCSquare_9.triggered.connect(self.applyClosingSquare9)
        self.actionColor_RGB_to_HSV.triggered.connect(self.applyColorRGBtoHSV)
        self.actionColor_RGB.triggered.connect(self.applyColorRGBtoHSL)
        self.actionGamma_Correction.triggered.connect(self.applyGammaCorrection)
        self.actionKirsh.triggered.connect(self.applyKirshFilter)
        self.actionScharr.triggered.connect(self.applyScharrFilter)
        self.actionColor_RGB_to_YCrCb.triggered.connect(self.applyColorRGBtoYCrCb)
        self.actionColor_RGB_to_CMYK.triggered.connect(self.applyColorRGBtoCMYK)
        self.actionInput.triggered.connect(self.show_input_histogram)
        self.actionOutput.triggered.connect(self.show_output_histogram)
        self.actionInput_Output.triggered.connect(self.show_input_histogram)
        self.actionInput_Output.triggered.connect(self.show_output_histogram)
        self.actionSegmentasi_Citra.triggered.connect(self.applyImageSegmentation)
        # self.actionROI.triggered.connect(self.applyROI)
        self.actionROI.triggered.connect(self.open_roi)
        self.actionRemove_Background.triggered.connect(self.removeBackground)
        self.actionEnglish_US.triggered.connect(self.changeLanguageToEnglishUS)
        self.actionIndonesia.triggered.connect(self.changeLanguageToIndonesia)

        # ----------------------------------------------------------------------------------------------------------
        # FUNGSI AKSI PADA TOMBOL -----------------------------------------------------------------------------------------
        # TOMBOL IMPOR
        self.buttonClear.clicked.connect(self.clearImage)
        self.buttonSimpan.clicked.connect(self.saveImage)
        # self.buttonSetImage.clicked.connect(self.aturefek)
        self.buttonUndo.clicked.connect(self.undoEfek)
        self.buttonTetapImport.clicked.connect(self.importImage)
        self.buttonEffect1.clicked.connect(self.showPreviewEffect1)
        self.buttonEffect2.clicked.connect(self.showPreviewEffect2)
        self.buttonEffect3.clicked.connect(self.showPreviewEffect3)




    def loadImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        
        self.image_path, _ = QFileDialog.getOpenFileName(None, "Open Image File", "", 
                                                    "Image Files (*.png *.jpg *.bmp *.gif *.jpeg);;All Files (*)", options=options)
        
        if self.image_path:
            self.pixmap1 = QtGui.QPixmap(self.image_path)
            self.width = self.pixmap1.width()
            self.height = self.pixmap1.height()
            if (self.width > 1000 and self.height > 1000):
                self.labelWarning.setText("Ukuran gambar input terlalu besar!\nAplikasi mungkin akan berjalan lambat ketika melakukan operasi. Tetap lanjutkan?")
                self.buttonTetapImport.setVisible(True)
            else:
                self.importImage()

    def importImage(self):
                self.pbInput.setPixmap(self.pixmap1)
                self.pbInput.setScaledContents(True)
                self.pbOutput.setScaledContents(True)
                self.labelInput.setText(self.image_path)
                self.pixmap2 = None
                self.pixmap3 = None
                self.pixmap4 = None
                self.pixmap5 = None
                self.stringefek1 = None
                self.stringefek2 = None
                self.stringefek3 = None
                self.input_pixmap1 = None
                self.buttonEffect1.setText("Tidak ada efek 1")
                self.buttonEffect2.setText("Tidak ada efek 2")
                self.buttonEffect3.setText("Tidak ada efek 3")
                self.buttonSet.setText("Atur ke efek 1")
                self.labelOutput.setText(None)
                self.labelWarning.setText(None)
                self.buttonTetapImport.setVisible(False)
                self.showImageData()
                # self.clearImage()

    
    def clearImage(self):
        self.pixmap1 = None
        self.labelInput.setText(None)
        self.pixmap2 = None
        self.pixmap3 = None
        self.pixmap4 = None
        self.pixmap5 = None
        self.stringefek1 = None
        self.stringefek2 = None
        self.stringefek3 = None
        self.input_pixmap1 = None
        self.buttonEffect1.setText("Tidak ada efek 1")
        self.buttonEffect2.setText("Tidak ada efek 2")
        self.buttonEffect3.setText("Tidak ada efek 3")
        self.buttonSet.setText("Atur ke efek 1")
        self.labelOutput.setText(None)
        self.labelWarning.setText(None)
        self.pbInput.clear()
        self.pbOutput.clear()

    def setImage1(self):
        if self.image_path:
            # Menyalin gambar dari pbOutput ke pixmap1
            self.pixmap1 = self.pbOutput.pixmap().copy()
            if self.pixmap1:
                self.pixmap1.save(self.image_path)

        







        # 2) FUNGSI SAVE AS
    def saveImage(self):
        if (self.pbOutput.pixmap() is None):
             self.showWarningSave()
        else :
                options = QFileDialog.Options()
                options |= QFileDialog.ReadOnly
                
                self.image_path, _ = QFileDialog.getSaveFileName(None, "Save Image File", "", 
                                                        "PNG Files (*.png);;JPEG Files (*.jpg *.jpeg);;Bitmap Files (*.bmp);;All Files (*)", options=options)
                
                if self.image_path:
                # pixmap = self.pbInput.pixmap()
                        pixmap = self.pbOutput.pixmap()
                        if pixmap:
                                pixmap.save(self.image_path)

        # 3) FUNGSI EXIT
    def exitApplication(self):
        QtWidgets.qApp.quit()


    def changeLanguageToEnglishUS(self):
        self.languageCondition = 0
        _translate = QtCore.QCoreApplication.translate
        # Tampilan UI Aksi
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.buttonEffect1.setText("No Effect 1")
        self.buttonEffect2.setText("No Effect 2")
        self.buttonEffect3.setText("No Effect 3")
        self.buttonSet.setText("Set to effect 1")
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHistogram.setTitle(_translate("MainWindow", "Brightness Histogram"))
        self.menuColor.setTitle(_translate("MainWindow", "Color"))
        self.menuRGB_to_Grayscale.setTitle(_translate("MainWindow", "RGB to Grayscale"))
        self.menuBit_Depth.setTitle(_translate("MainWindow", "Bit Depth"))
        self.menuImage_Processing.setTitle(_translate("MainWindow", "Image Processing"))
        self.menuAritmatics_Operation.setTitle(_translate("MainWindow", "Aritmatics Operations"))
        self.menuFilter.setTitle(_translate("MainWindow", "Filter"))
        self.menuGaussian_Blur.setTitle(_translate("MainWindow", "Gaussian Blur"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuMorphology.setTitle(_translate("MainWindow", "Morphology"))
        self.menuErosion.setTitle(_translate("MainWindow", "Erosion"))
        self.menuOpening.setTitle(_translate("MainWindow", "Opening"))
        self.menuDilation.setTitle(_translate("MainWindow", "Dilation"))
        self.menuClosing.setTitle(_translate("MainWindow", "Closing"))
        self.menuAbout.setTitle(_translate("MainWindow", "Others"))
        self.menuAppearance.setTitle(_translate("MainWindow", "Appearance"))
        self.menuType_Font.setTitle(_translate("MainWindow", "Type Font"))
        self.menuAuto_Fit_Image.setTitle(_translate("MainWindow", "Auto Fit Image"))
        self.menuInputBorderStyle.setTitle(_translate("MainWindow", "InputBorderStyle"))
        self.menuSize_Font.setTitle(_translate("MainWindow", "Size Font"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.menuThird_Apps.setTitle(_translate("MainWindow", "Third Apps"))
        self.menuAbout_2.setTitle(_translate("MainWindow", "About"))
        self.menuGeometry.setTitle(_translate("MainWindow", "Geometry"))
        self.menuRotation.setTitle(_translate("MainWindow", "Rotation"))
        self.menuScaling.setTitle(_translate("MainWindow", "Scaling"))
        self.menuFeature_Extraction.setTitle(_translate("MainWindow", "Feature Extraction"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionInput.setText(_translate("MainWindow", "Input"))
        self.actionOutput.setText(_translate("MainWindow", "Output"))
        self.actionInput_Output.setText(_translate("MainWindow", "Input Output"))
        self.actionBrightness.setText(_translate("MainWindow", "Brightness"))
        self.actionBrightness_Contrast.setText(_translate("MainWindow", "Brightness - Contrast"))
        self.actionLog_Brightness.setText(_translate("MainWindow", "Log Brightness"))
        self.actionInvers.setText(_translate("MainWindow", "Invers"))
        self.actionGamma_Correction.setText(_translate("MainWindow", "Gamma Correction"))
        self.actionHistogram_Equalization_HE.setText(_translate("MainWindow", "Histogram Equalization (HE)"))
        self.actionFuzzy_HE_RGB.setText(_translate("MainWindow", "Fuzzy HE RGB"))
        self.actionFuzzy_to_Grayscale.setText(_translate("MainWindow", "Fuzzy to Grayscale"))
        self.actionOpen_Aritmatics_Panel.setText(_translate("MainWindow", "Open Aritmatics Panel"))
        self.actionIdentity.setText(_translate("MainWindow", "Identity"))
        self.actionEdge_Detection_1.setText(_translate("MainWindow", "Edge Detection 1"))
        self.actionEdge_Detection_2.setText(_translate("MainWindow", "Edge Detection 2"))
        self.actionEdge_Detection_3.setText(_translate("MainWindow", "Edge Detection 3"))
        self.actionSharpen.setText(_translate("MainWindow", "Sharpen"))
        self.actionUnsharp_Masking.setText(_translate("MainWindow", "Unsharp Masking"))
        self.actionAverage_Filter.setText(_translate("MainWindow", "Average Filter"))
        self.actionLow_Pass_Filter.setText(_translate("MainWindow", "Low Pass Filter"))
        self.actionHigh_Pass_Filter.setText(_translate("MainWindow", "High Pass Filter"))
        self.actionBandstop_Filter.setText(_translate("MainWindow", "Bandstop Filter"))
        self.actionPrewitt.setText(_translate("MainWindow", "Prewitt"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionRobert.setText(_translate("MainWindow", "Robert"))
        self.actionESquare_3.setText(_translate("MainWindow", "Square 3"))
        self.actionESquare_5.setText(_translate("MainWindow", "Square 5"))
        self.actionECross_3.setText(_translate("MainWindow", "Cross 3"))
        self.actionDSquare_3.setText(_translate("MainWindow", "Square 3"))
        self.actionDSquare_5.setText(_translate("MainWindow", "Square 5"))
        self.actionDCross_3.setText(_translate("MainWindow", "Cross 3"))
        self.actionOSquare_9.setText(_translate("MainWindow", "Square 9"))
        self.actionCSquare_9.setText(_translate("MainWindow", "Square 9"))
        self.actionYellow.setText(_translate("MainWindow", "Yellow"))
        self.actionCyan.setText(_translate("MainWindow", "Cyan"))
        self.actionPurple.setText(_translate("MainWindow", "Purple"))
        self.actionRed.setText(_translate("MainWindow", "Red"))
        self.actionGreen.setText(_translate("MainWindow", "Green"))
        self.actionBlue.setText(_translate("MainWindow", "Blue"))
        self.actionOrange.setText(_translate("MainWindow", "Orange"))
        self.actionPink.setText(_translate("MainWindow", "Pink"))
        self.actionGray.setText(_translate("MainWindow", "Gray"))
        self.actionAverage.setText(_translate("MainWindow", "Average"))
        self.actionLightness.setText(_translate("MainWindow", "Lightness"))
        self.actionLuminance.setText(_translate("MainWindow", "Luminance"))
        self.actionGaussian_Blur_3x3.setText(_translate("MainWindow", "Gaussian Blur 3x3"))
        self.actionGaussian_Blur_5x5.setText(_translate("MainWindow", "Gaussian Blur 5x5"))
        self.actionEnable.setText(_translate("MainWindow", "Enable"))
        self.actionDisable.setText(_translate("MainWindow", "Disable"))
        self.actionBox.setText(_translate("MainWindow", "Box"))
        self.actionWindows.setText(_translate("MainWindow", "Windows"))
        self.actionNo_Border.setText(_translate("MainWindow", "No Border"))
        self.actionSegoe_UI.setText(_translate("MainWindow", "Segoe UI"))
        self.actionAbout_Apps.setText(_translate("MainWindow", "About Apps"))
        self.actionCheck_For_Updates.setText(_translate("MainWindow", "Check For Updates"))
        self.actionRemove_Background.setText(_translate("MainWindow", "Remove Background"))
        self.actionAI_HD_Photo_Upscaling.setText(_translate("MainWindow", "AI HD Photo and Upscaling"))
        self.actionAI_Image_Generator.setText(_translate("MainWindow", "AI Image Generator"))
        self.action90_degree.setText(_translate("MainWindow", "90 degree"))
        self.action180_degree.setText(_translate("MainWindow", "180 degree"))
        self.Set_value.setText(_translate("MainWindow", "Set Value"))
        self.actionTranslation.setText(_translate("MainWindow", "Translation"))
        self.actionCrop.setText(_translate("MainWindow", "Cropping"))
        self.actionUniform_Scaling.setText(_translate("MainWindow", "Uniform Scaling"))
        self.actionNon_Uniform_Scaling.setText(_translate("MainWindow", "Non-Uniform Scaling"))
        self.actionThreshold.setText(_translate("MainWindow", "Threshold"))
        self.actionEkstraksi_Warna.setText(_translate("MainWindow", "Ekstraksi Warna"))
        self.actionColor_RGB.setText(_translate("MainWindow", "Color RGB to HSL"))
        self.actionColor_RGB_to_HSV.setText(_translate("MainWindow", "Color RGB to HSV"))
        self.actionColor_RGB_to_YCrCb.setText(_translate("MainWindow", "Color RGB to YCrCb"))
        self.actionThreshold_2.setText(_translate("MainWindow", "Threshold"))
        self.actionColor_RGB_to_CMYK.setText(_translate("MainWindow", "Color RGB to CMYK"))
        self.action270_degree.setText(_translate("MainWindow", "270 degree"))
        # Tampilan UI Tombol
        self.label.setText(_translate("MainWindow", "Input Image"))
        self.label_2.setText(_translate("MainWindow", "Output Image"))
        self.labelEfek.setText(_translate("MainWindow", "Effect :"))
        self.labelInput_6.setText(_translate("MainWindow", "*Click an effect to show it in preview "))
        self.buttonClear.setText(_translate("MainWindow", "Clear Image"))
        self.buttonUndo.setText(_translate("MainWindow", "Undo Effect"))
        self.buttonTetapImport.setText(_translate("MainWindow", "Keep Importing"))
        self.buttonSimpan.setText(_translate("MainWindow", "Save"))

    def changeLanguageToIndonesia(self):
        self.languageCondition = 1
        _translate = QtCore.QCoreApplication.translate
        # Tampilan UI Aksi
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.buttonEffect1.setText("Tidak ada efek 1")
        self.buttonEffect2.setText("Tidak ada efek 2")
        self.buttonEffect3.setText("Tidak ada efek 3")
        self.buttonSet.setText("Atur ke efek 1")
        self.menuView.setTitle(_translate("MainWindow", "Tampilan"))
        self.menuHistogram.setTitle(_translate("MainWindow", "Histogram Kecerahan"))
        self.menuColor.setTitle(_translate("MainWindow", "Warna"))
        self.menuRGB_to_Grayscale.setTitle(_translate("MainWindow", "RGB ke Grayscale"))
        self.menuBit_Depth.setTitle(_translate("MainWindow", "Kedalaman Bit"))
        self.menuImage_Processing.setTitle(_translate("MainWindow", "Pemrosesan Gambar"))
        self.menuAritmatics_Operation.setTitle(_translate("MainWindow", "Operasi Aritmatika"))
        self.menuFilter.setTitle(_translate("MainWindow", "Filter"))
        self.menuGaussian_Blur.setTitle(_translate("MainWindow", "Blur Gaussian"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Deteksi Tepi"))
        self.menuMorphology.setTitle(_translate("MainWindow", "Morfologi"))
        self.menuErosion.setTitle(_translate("MainWindow", "Erosi"))
        self.menuOpening.setTitle(_translate("MainWindow", "Pembukaan"))
        self.menuDilation.setTitle(_translate("MainWindow", "Dilasi"))
        self.menuClosing.setTitle(_translate("MainWindow", "Penutup"))
        self.menuAbout.setTitle(_translate("MainWindow", "Lainnya"))
        self.menuAppearance.setTitle(_translate("MainWindow", "Penampilan"))
        self.menuType_Font.setTitle(_translate("MainWindow", "Tipe Font"))
        self.menuAuto_Fit_Image.setTitle(_translate("MainWindow", "Paskan Gambar Otomatis"))
        self.menuInputBorderStyle.setTitle(_translate("MainWindow", "Gaya Tepi Input Gambar"))
        self.menuSize_Font.setTitle(_translate("MainWindow", "Ukuran Font"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Bahasa"))
        self.menuThird_Apps.setTitle(_translate("MainWindow", "Aplikasi Ketiga"))
        self.menuAbout_2.setTitle(_translate("MainWindow", "Tentang"))
        self.menuGeometry.setTitle(_translate("MainWindow", "Geometri"))
        self.menuRotation.setTitle(_translate("MainWindow", "Rotasi"))
        self.menuScaling.setTitle(_translate("MainWindow", "Penskalaan"))
        self.menuFeature_Extraction.setTitle(_translate("MainWindow", "Ekstraksi Fitur"))
        self.actionOpen.setText(_translate("MainWindow", "Buka"))
        self.actionSave_As.setText(_translate("MainWindow", "Simpan Sebagai"))
        self.actionExit.setText(_translate("MainWindow", "Keluar"))
        self.actionInput.setText(_translate("MainWindow", "Input"))
        self.actionOutput.setText(_translate("MainWindow", "Output"))
        self.actionInput_Output.setText(_translate("MainWindow", "Input Output"))
        self.actionBrightness.setText(_translate("MainWindow", "Kecerahan"))
        self.actionBrightness_Contrast.setText(_translate("MainWindow", "Kecerahan - Kontras"))
        self.actionLog_Brightness.setText(_translate("MainWindow", "Log Kecerahan"))
        self.actionInvers.setText(_translate("MainWindow", "Balikkan"))
        self.actionGamma_Correction.setText(_translate("MainWindow", "Koreksi Gamma"))
        self.actionHistogram_Equalization_HE.setText(_translate("MainWindow", "Penyetaraan Histogram (HE)"))
        self.actionFuzzy_HE_RGB.setText(_translate("MainWindow", "Fuzzy HE RGB"))
        self.actionFuzzy_to_Grayscale.setText(_translate("MainWindow", "Fuzzy ke Grayscale"))
        self.actionOpen_Aritmatics_Panel.setText(_translate("MainWindow", "Buka Panel Aritmatika"))
        self.actionIdentity.setText(_translate("MainWindow", "Identitas"))
        self.actionSharpen.setText(_translate("MainWindow", "Pengasah"))
        self.actionUnsharp_Masking.setText(_translate("MainWindow", "Masking Tidak Tajam"))
        self.actionAverage_Filter.setText(_translate("MainWindow", "Filter Rata-rata"))
        self.actionLow_Pass_Filter.setText(_translate("MainWindow", "Filter Pass Rendah"))
        self.actionHigh_Pass_Filter.setText(_translate("MainWindow", "Filter Pass Tinggi"))
        self.actionBandstop_Filter.setText(_translate("MainWindow", "Filter Pemberhentian Band"))
        self.actionPrewitt.setText(_translate("MainWindow", "Prewitt"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionRobert.setText(_translate("MainWindow", "Robert"))
        self.actionESquare_3.setText(_translate("MainWindow", "Persegi 3"))
        self.actionESquare_5.setText(_translate("MainWindow", "Persegi 5"))
        self.actionECross_3.setText(_translate("MainWindow", "Silang 3"))
        self.actionDSquare_3.setText(_translate("MainWindow", "Persegi 3"))
        self.actionDSquare_5.setText(_translate("MainWindow", "Persegi 5"))
        self.actionDCross_3.setText(_translate("MainWindow", "Silang 3"))
        self.actionOSquare_9.setText(_translate("MainWindow", "Persegi 9"))
        self.actionCSquare_9.setText(_translate("MainWindow", "Persegi 9"))
        self.actionYellow.setText(_translate("MainWindow", "Kuning"))
        self.actionCyan.setText(_translate("MainWindow", "Biru Muda"))
        self.actionPurple.setText(_translate("MainWindow", "Ungu"))
        self.actionRed.setText(_translate("MainWindow", "Merah"))
        self.actionGreen.setText(_translate("MainWindow", "Hijau"))
        self.actionBlue.setText(_translate("MainWindow", "Biru"))
        self.actionOrange.setText(_translate("MainWindow", "Jingga"))
        self.actionPink.setText(_translate("MainWindow", "Merah Muda"))
        self.actionGray.setText(_translate("MainWindow", "Abu-abu"))
        self.actionAverage.setText(_translate("MainWindow", "Rata-rata"))
        self.actionLightness.setText(_translate("MainWindow", "Kecerahan Ringan"))
        self.actionLuminance.setText(_translate("MainWindow", "Pencahayaan"))
        self.actionGaussian_Blur_3x3.setText(_translate("MainWindow", "Blur Gaussian 3x3"))
        self.actionGaussian_Blur_5x5.setText(_translate("MainWindow", "Blur Gaussian 5x5"))
        self.actionEnable.setText(_translate("MainWindow", "Hidupkan"))
        self.actionDisable.setText(_translate("MainWindow", "Matikan"))
        self.actionBox.setText(_translate("MainWindow", "Kotak"))
        self.actionWindows.setText(_translate("MainWindow", "Windows"))
        self.actionNo_Border.setText(_translate("MainWindow", "Tidak ada Border"))
        self.actionSegoe_UI.setText(_translate("MainWindow", "Segoe UI"))
        self.actionAbout_Apps.setText(_translate("MainWindow", "Tentang Aplikasi"))
        self.actionCheck_For_Updates.setText(_translate("MainWindow", "Cek Pembaruan"))
        self.actionRemove_Background.setText(_translate("MainWindow", "Hilangkan Latar Belakang"))
        self.actionAI_HD_Photo_Upscaling.setText(_translate("MainWindow", "AI Pertajam dan Penskalaan Foto"))
        self.actionAI_Image_Generator.setText(_translate("MainWindow", "AI Pembuat Gambar"))
        self.action90_degree.setText(_translate("MainWindow", "90 derajat"))
        self.action180_degree.setText(_translate("MainWindow", "180 derajat"))
        self.Set_value.setText(_translate("MainWindow", "Set Nilai"))
        self.actionTranslation.setText(_translate("MainWindow", "Translasi"))
        self.actionCrop.setText(_translate("MainWindow", "Pemotongan"))
        self.actionUniform_Scaling.setText(_translate("MainWindow", "Penskalaan Seragam"))
        self.actionNon_Uniform_Scaling.setText(_translate("MainWindow", "Penskalaan Tidak Seragam"))
        self.actionThreshold.setText(_translate("MainWindow", "Ambang"))
        self.actionColor_RGB.setText(_translate("MainWindow", "Warna RGB ke HSL"))
        self.actionColor_RGB_to_HSV.setText(_translate("MainWindow", "Warna RGB ke HSV"))
        self.actionColor_RGB_to_YCrCb.setText(_translate("MainWindow", "Warna RGB ke YCrCb"))
        self.actionColor_RGB_to_CMYK.setText(_translate("MainWindow", "Warna RGB ke CMYK"))
        self.actionThreshold_2.setText(_translate("MainWindow", "Ambang"))
        self.action270_degree.setText(_translate("MainWindow", "270 derajat"))
        # Tampilan UI Tombol
        self.label.setText(_translate("MainWindow", "Gambar Masukan"))
        self.label_2.setText(_translate("MainWindow", "Gambar Keluaran"))
        self.labelEfek.setText(_translate("MainWindow", "Efek :"))
        self.labelInput_6.setText(_translate("MainWindow", "*Klik efek untuk menampilkannya pada preview "))
        self.buttonClear.setText(_translate("MainWindow", "Bersihkan Gambar"))
        self.buttonUndo.setText(_translate("MainWindow", "Undo Efek"))
        self.buttonTetapImport.setText(_translate("MainWindow", "Tetap Impor"))
        self.buttonSimpan.setText(_translate("MainWindow", "Simpan"))


        # ----------------------------------------------------------------------------------------------------------
        # FUNGSI MENU FILE -----------------------------------------------------------------------------------------
        # 1) RGB - KUNING
    def convertToYellowRGB(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            yellow_image = self.pixmap1.toImage()  # Mengambil gambar dari pbInput
            if yellow_image.isNull():
                return

            width = yellow_image.width()
            height = yellow_image.height()

            

            for y in range(height):
                for x in range(width):
                    pixel = yellow_image.pixel(x, y)
                    r, g, b, a = QColor(pixel).getRgb()  # Mendapatkan nilai R, G, B dari pixel

                    # # Konversi ke efek kuning dengan mengatur nilai G dan B ke 0
                    # new_pixel = QColor(255, g, 0, a)  # Set R ke 255 (merah) dan G ke 0 (hijau)

                    # Konversi ke efek kuning dengan mengatur nilai G dan B ke 0
                    new_pixel = QColor(r, 255, 100, a)  # Set G ke 255 (kuning) dan B ke 0

                    # Tetapkan pixel baru ke gambar
                    yellow_image.setPixel(x, y, new_pixel.rgb())
                    self.progressBar.setProperty("value", 100)

            # Tampilkan gambar yang sudah diubah pada pbOutput
            self.pbOutput.setPixmap(QPixmap.fromImage(yellow_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Yellow '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)


        # FUNGSI MENU COLORS -----------------------------------------------------------------------------------------
        # 2) RGB TO GRAYSCALE - AVERAGE
    def convertToGreyscaleAverage(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            input_image = self.pixmap1.toImage()
            width = input_image.width()
            height = input_image.height()
                    
                    # Buat gambar abu-abu dengan ukuran yang sama
            grey_image = QImage(width, height, QImage.Format_Grayscale8)
                    
            for y in range(height):
                for x in range(width):
                    pixel = input_image.pixel(x, y)
                    color = QtGui.QColor(pixel)
                    # Ambil nilai merah, hijau, dan biru dari warna pixel
                    red = color.red()
                    green = color.green()
                    blue = color.blue()
                    
                    # Hitung nilai rata-rata komponen warna dan atur ke nilai abu-abu
                    grey_value = (red + green + blue) // 3
                            
                    grey_pixel = qRgb(grey_value, grey_value, grey_value)
                    grey_image.setPixel(x, y, grey_pixel)
                    self.progressBar.setProperty("value", 100)

            self.pbOutput.setPixmap(QPixmap.fromImage(grey_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Average '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)

                    

        # 2) RGB TO GRAYSCALE - LIGHTNESS
    def convertToGreyscaleLightness(self):
            if self.pixmap1 is not None and not self.pixmap1.isNull():
                self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
                input_image = self.pixmap1.toImage()
                width = input_image.width()
                height = input_image.height()
                
                # Buat gambar abu-abu dengan ukuran yang sama
                grey_image = QImage(width, height, QImage.Format_Grayscale8)

                for y in range(height):
                    for x in range(width):
                        pixel = input_image.pixel(x, y)
                        color = QtGui.QColor(pixel)
                        # Ambil nilai merah, hijau, dan biru dari warna pixel
                        red = color.red()
                        green = color.green()
                        blue = color.blue()

                        
                        # Hitung nilai kecerahan menggunakan metode Lightness
                        max_value = max(red, green, blue)
                        min_value = min(red, green, blue)
                        lightness = (max_value + min_value) // 2
                        grey_pixel = qRgb(lightness, lightness, lightness)
                        grey_image.setPixel(x, y, grey_pixel)
                        self.progressBar.setProperty("value", 100)

                self.pbOutput.setPixmap(QPixmap.fromImage(grey_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Lightness '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()
                

        # 2) RGB TO GRAYSCALE - LUMINANCE
    def convertToGreyscaleLuminance(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            img = self.pixmap1.toImage()
            width, height = img.width(), img.height()

            self.progressBar.setProperty("value", 25)

            for y in range(height):
                for x in range(width):
                    pixel = img.pixel(x, y)
                    # Dapatkan nilai merah (red), hijau (green), dan biru (blue) dari pixel
                    red = QtGui.qRed(pixel)
                    green = QtGui.qGreen(pixel)
                    blue = QtGui.qBlue(pixel)
                    
                    # Konversi RGB ke greyscale menggunakan formula Luminance
                    luminance = int(0.299 * red + 0.587 * green + 0.114 * blue)
                    # Buat warna greyscale
                    greyscale_color = QtGui.QColor(luminance, luminance, luminance)
                    # Set pixel ke warna greyscale pada gambar
                    img.setPixel(x, y, greyscale_color.rgb())
                    self.progressBar.setProperty("value", 100)


                self.pbOutput.setPixmap(QPixmap.fromImage(img))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Luminance '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()


        # 6) INVERS
    def convertToInvers(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
        # Ambil pixmap dari pbInput
            img = self.pixmap1.toImage()
            width, height = img.width(), img.height()

            for y in range(height):
                for x in range(width):
                    pixel = img.pixel(x, y)
                    # Dapatkan nilai merah (red), hijau (green), dan biru (blue) dari pixel
                    red = QtGui.qRed(pixel)
                    green = QtGui.qGreen(pixel)
                    blue = QtGui.qBlue(pixel)
                    
                    # Inversi warna
                    inverted_color = QtGui.QColor(255 - red, 255 - green, 255 - blue)
                    # Set pixel ke warna invers pada gambar
                    img.setPixel(x, y, inverted_color.rgb())
                    self.progressBar.setProperty("value", 100)
                    

                self.pbOutput.setPixmap(QPixmap.fromImage(img))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Invers '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

        # 3) BRIGHTNESS
    def applyContrastEffect(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            input_image = self.pixmap1.toImage()

            # Dapatkan ukuran gambar
            width = input_image.width()
            height = input_image.height()

            # Membuat salinan gambar untuk diubah
            output_image = QImage(width, height, QImage.Format_RGB32)

            # Faktor kontras (misalnya, 1.5 untuk meningkatkan kontras)
            contrast_factor = 1.5

            for x in range(width):
                for y in range(height):
                    pixel_color = QtGui.QColor(*input_image.pixelColor(x, y).getRgb())

                    

                    # Mengubah nilai warna pixel dengan faktor kontras
                    new_red = self.applyContrastToColor(pixel_color.red(), contrast_factor)
                    new_green = self.applyContrastToColor(pixel_color.green(), contrast_factor)
                    new_blue = self.applyContrastToColor(pixel_color.blue(), contrast_factor)

                    # Menetapkan warna baru untuk pixel
                    output_image.setPixelColor(x, y, QtGui.QColor(new_red, new_green, new_blue))
                    self.progressBar.setProperty("value", 100)
                    

            # Setelah selesai mengubah gambar, Anda hanya perlu mengatur gambar di salah satu pixmap, bukan dalam semua kondisi
            if (self.pixmap2 is None):
                self.pixmap2 = output_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Contrast '  # Ganti label sesuai dengan efek yang benar
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()
                

        
    def applyContrastToColor(self, color_value, contrast_factor):
        # Mengaplikasikan kontras pada nilai warna individual
        new_color_value = (color_value - 128) * contrast_factor + 128
        return max(0, min(255, int(new_color_value)))
    
        

        # 4) BRIGHTNESS - CONTRAST
    def showBrightnessContrastDialog(self):
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Brightness and Contrast")
        dialog.setModal(True)
        dialog.resize(300, 150)

        layout = QtWidgets.QVBoxLayout()

        # Tambahkan slider untuk brightness
        brightness_label = QtWidgets.QLabel("Brightness:")
        brightness_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        brightness_slider.setRange(-100, 100)
        brightness_slider.setValue(0)
        brightness_value_label = QtWidgets.QLabel("0")
        # Tambahkan slider untuk contrast
        contrast_label = QtWidgets.QLabel("Contrast:")
        contrast_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        contrast_slider.setRange(-100, 100)
        contrast_slider.setValue(0)
        contrast_value_label = QtWidgets.QLabel("0")

        # Tambahkan tombol "Apply"
        apply_button = QtWidgets.QPushButton("Apply")
        apply_button.clicked.connect(dialog.accept)

        layout.addWidget(brightness_label)
        layout.addWidget(brightness_slider)
        layout.addWidget(brightness_value_label) # Tambahkan label nilai brightness
        layout.addWidget(contrast_label)
        layout.addWidget(contrast_slider)
        layout.addWidget(contrast_value_label) # Tambahkan label nilai contrast
        layout.addWidget(apply_button)

        dialog.setLayout(layout)

        # Tambahkan label nilai brightness
        def updateBrightnessLabel(value):
            brightness_value_label.setText(str(value))
        # Tambahkan label nilai contrast
        def updateContrastLabel(value):
            contrast_value_label.setText(str(value))

        brightness_slider.valueChanged.connect(updateBrightnessLabel)
        contrast_slider.valueChanged.connect(updateContrastLabel)

        result = dialog.exec_()

        if result == QtWidgets.QDialog.Accepted:
            # Dapatkan nilai brightness dan contrast yang dipilih
            brightness_value = brightness_slider.value()
            contrast_value = contrast_slider.value()
            # Terapkan efek brightness dan contrast ke gambar
            self.progressBar.setProperty("value", 100)
            self.applyBrightnessContrast(brightness_value, contrast_value)
            self.stringefek1 = 'Effect : Brightness '
            self.labelOutput.setText(self.stringefek1)
            self.progressBar.setProperty("value", 0)
            self.showEffectComplete()


    def applyBrightnessContrast(self, brightness_value, contrast_value):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
        # Konversi QPixmap ke QImage
            input_image = self.pixmap1.toImage()

            # Dapatkan ukuran gambar
            width = input_image.width()
            height = input_image.height()

            # Faktor brightness dari nilai slider (-100 hingga 100)
            brightness_factor = brightness_value / 100.0

            # Faktor contrast dari nilai slider (-100 hingga 100)
            contrast_factor = contrast_value / 100.0

            # Membuat salinan gambar untuk diubah
            output_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            for x in range(width):
                for y in range(height):
                    pixel_color = QtGui.QColor(*input_image.pixelColor(x, y).getRgb())

                    # Mengubah nilai warna pixel dengan faktor brightness
                    new_red = self.applyBrightnessToColor(pixel_color.red(), brightness_factor)
                    new_green = self.applyBrightnessToColor(pixel_color.green(), brightness_factor)
                    new_blue = self.applyBrightnessToColor(pixel_color.blue(), brightness_factor)

                    

                    # Mengubah nilai warna pixel dengan faktor contrast
                    new_red = self.applyContrastToColor(new_red, contrast_factor)
                    new_green = self.applyContrastToColor(new_green, contrast_factor)
                    new_blue = self.applyContrastToColor(new_blue, contrast_factor)

                    # Menetapkan warna baru untuk pixel
                    output_image.setPixelColor(x, y, QtGui.QColor(new_red, new_green, new_blue))
                    self.progressBar.setProperty("value", 100)

                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Brightness-Contrast '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()
    
    def applyBrightnessToColor(self, color_value, brightness_factor):

        new_color_value = color_value + brightness_factor
        # Pastikan nilai warna tetap dalam rentang 0-255
        new_color_value = max(0, min(255, new_color_value))

        return new_color_value
    


    # Bit Depth
    def applyThreshold(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
           
            input_image = self.pixmap1.toImage()

            # tinggi lebar gambar
            width = input_image.width()
            height = input_image.height()

            output_image = QImage(width, height, QImage.Format_RGB888)

            # definisi nilai threshold
            threshold = 128

            for y in range(height):
                for x in range(width):
                    pixel_color = input_image.pixelColor(x, y)
                    # (0.299R + 0.587G + 0.114B)
                    gray_value = int(0.299 * pixel_color.red() + 0.587 * pixel_color.green() + 0.114 * pixel_color.blue())

                    
                    
                    if gray_value >= threshold:
                        output_image.setPixelColor(x, y, QColor(255, 255, 255))  # White
                    else:
                        output_image.setPixelColor(x, y, QColor(0, 0, 0))  # Black
                        self.progressBar.setProperty("value", 100)

                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Threshold '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

    def applyGammaCorrection(self, gamma):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            img = self.pixmap1.toImage()
            width, height = img.width(), img.height()

            gamma_corrected_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            for y in range(height):
                for x in range(width):
                    pixel = img.pixel(x, y)
                    red = QtGui.qRed(pixel)
                    green = QtGui.qGreen(pixel)
                    blue = QtGui.qBlue(pixel)

                    # # Koreksi gamma untuk setiap saluran warna (red, green, dan blue)
                    # red = int(255 * (red / 255) ** gamma)
                    # green = int(255 * (green / 255) ** gamma)
                    # blue = int(255 * (blue / 255) ** gamma)
                    red = int(255 * (red / 255) * gamma)
                    green = int(255 * (green / 255) * gamma)
                    blue = int(255 * (blue / 255) * gamma)

                    

                    gamma_corrected_color = QtGui.QColor(red, green, blue)
                    gamma_corrected_image.setPixel(x, y, gamma_corrected_color.rgb())
                    self.progressBar.setProperty("value", 100)

                self.pbOutput.setPixmap(QPixmap.fromImage(gamma_corrected_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Gamma Correction '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()


    def showLogBrightness(self):
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Log Brightness")
        dialog.setModal(True)
        dialog.resize(300, 150)

        layout = QtWidgets.QVBoxLayout()

        # Tambahkan slider untuk brightness
        brightness_label = QtWidgets.QLabel("Log Level:")
        log_brightness_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        log_brightness_slider.setRange(0, 100)
        log_brightness_slider.setValue(0)
        brightness_value_label = QtWidgets.QLabel("0")

        # Tambahkan tombol "Apply"
        apply_button = QtWidgets.QPushButton("Terapkan")
        apply_button.clicked.connect(dialog.accept)

        layout.addWidget(brightness_label)
        layout.addWidget(log_brightness_slider)
        layout.addWidget(brightness_value_label) # Tambahkan label nilai brightness
        layout.addWidget(apply_button)

        dialog.setLayout(layout)

        def updateBrightnessLabel(value):
            brightness_value_label.setText(str(value))

        log_brightness_slider.valueChanged.connect(updateBrightnessLabel)
        result = dialog.exec_()

        if result == QtWidgets.QDialog.Accepted:
            log_brightness_value = log_brightness_slider.value()
            self.applyLogBrightness(log_brightness_value)

    def applyLogBrightness(self, log_brightness_value):
            input_image = self.pbInput.pixmap().toImage()
            log_brightness_factor = log_brightness_value * 2.55

            self.progressBar.setProperty("value", 0)

            width = input_image.width()
            height = input_image.height()

            output_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            for i in range(width):
                for j in range(height):
                    pixel_color = input_image.pixelColor(i, j)
                    r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()
                    r1 = int(log_brightness_factor * (math.log10(1 + r)))
                    g1 = int(log_brightness_factor * (math.log10(1 + g)))
                    b1 = int(log_brightness_factor * (math.log10(1 + b)))

                    self.progressBar.setProperty("value", 0)

                    # Gunakan setPixel untuk mengatur nilai piksel dengan QColor yang dihitung
                    output_image.setPixel(i, j, QtGui.qRgb(r1, g1, b1))
                    self.progressBar.setProperty("value", 100)

                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = "Effect : Log Brightness. Value: "+str(log_brightness_factor)
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()


    def applyKirshFilter(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            img = self.pixmap1.toImage()
            width, height = img.width(), img.height()

            kirsh_filtered_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Matriks filter Kirsh
            kirsh_kernel = [
                [-3, -3, -3],
                [-3,  0, -3],
                [ 5,  5,  5]
            ]

            for y in range(1, height - 1):
                for x in range(1, width - 1):
                    red_sum = 0
                    green_sum = 0
                    blue_sum = 0

                    for ky in range(3):
                        for kx in range(3):
                            pixel = img.pixel(x - 1 + kx, y - 1 + ky)
                            red = QtGui.qRed(pixel)
                            green = QtGui.qGreen(pixel)
                            blue = QtGui.qBlue(pixel)

                            

                            # Mengalikan nilai piksel dengan matriks kernel Kirsh
                            red_sum += red * kirsh_kernel[ky][kx]
                            green_sum += green * kirsh_kernel[ky][kx]
                            blue_sum += blue * kirsh_kernel[ky][kx]

                    # Menyimpan hasil dari filter Kirsh
                    red_sum = max(0, min(255, red_sum))
                    green_sum = max(0, min(255, green_sum))
                    blue_sum = max(0, min(255, blue_sum))

                    kirsh_filtered_color = QtGui.QColor(red_sum, green_sum, blue_sum)
                    kirsh_filtered_image.setPixel(x, y, kirsh_filtered_color.rgb())
                    self.progressBar.setProperty("value", 100)

                self.pbOutput.setPixmap(QPixmap.fromImage(kirsh_filtered_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Kirsh Filter '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

    
    def applyScharrFilter(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            img = self.pixmap1.toImage()
            width, height = img.width(), img.height()

            scharr_filtered_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Matriks filter Scharr untuk deteksi tepi vertikal
            scharr_vertical_kernel = [
                [-3, 0, 3],
                [-10, 0, 10],
                [-3, 0, 3]
            ]

            # Matriks filter Scharr untuk deteksi tepi horizontal
            scharr_horizontal_kernel = [
                [-3, -10, -3],
                [0, 0, 0],
                [3, 10, 3]
            ]

            for y in range(1, height - 1):
                for x in range(1, width - 1):
                    red_sum_v = 0
                    green_sum_v = 0
                    blue_sum_v = 0
                    red_sum_h = 0
                    green_sum_h = 0
                    blue_sum_h = 0

                    for ky in range(3):
                        for kx in range(3):
                            pixel = img.pixel(x - 1 + kx, y - 1 + ky)
                            red = QtGui.qRed(pixel)
                            green = QtGui.qGreen(pixel)
                            blue = QtGui.qBlue(pixel)

                            # Mengalikan nilai piksel dengan matriks kernel Scharr
                            red_sum_v += red * scharr_vertical_kernel[ky][kx]
                            green_sum_v += green * scharr_vertical_kernel[ky][kx]
                            blue_sum_v += blue * scharr_vertical_kernel[ky][kx]

                            red_sum_h += red * scharr_horizontal_kernel[ky][kx]
                            green_sum_h += green * scharr_horizontal_kernel[ky][kx]
                            blue_sum_h += blue * scharr_horizontal_kernel[ky][kx]

                    # Menyimpan hasil dari filter Scharr (vertikal dan horizontal)
                    red_sum_v = max(0, min(255, red_sum_v))
                    green_sum_v = max(0, min(255, green_sum_v))
                    blue_sum_v = max(0, min(255, blue_sum_v))
            
                    

                    red_sum_h = max(0, min(255, red_sum_h))
                    green_sum_h = max(0, min(255, green_sum_h))
                    blue_sum_h = max(0, min(255, blue_sum_h))

                    scharr_filtered_color = QtGui.QColor(red_sum_v, green_sum_v, blue_sum_v)
                    scharr_filtered_image.setPixel(x, y, scharr_filtered_color.rgb())
                    self.progressBar.setProperty("value", 100)

                self.pbOutput.setPixmap(QPixmap.fromImage(scharr_filtered_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Scharr Filter '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()


    def applyLaplacianOfGaussianFilter(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)

            img = self.pixmap1.toImage()
            width, height = img.width(), img.height()

            # Matriks filter LoG (Laplacian of Gaussian)
            log_kernel = np.array([
                [0, 0, -1, 0, 0],
                [0, -1, -2, -1, 0],
                [-1, -2, 16, -2, -1],
                [0, -1, -2, -1, 0],
                [0, 0, -1, 0, 0]
            ])

            # Filter Gauss
            gaussian_kernel = (1/256) * np.array([
                [1, 4, 6, 4, 1],
                [4, 16, 24, 16, 4],
                [6, 24, 36, 24, 6],
                [4, 16, 24, 16, 4],
                [1, 4, 6, 4, 1]
            ])

            # Konvolusi filter Gauss terlebih dahulu
            gaussian_filtered_image = QImage(width, height, QImage.Format_RGB32)

            for y in range(2, height - 2):
                for x in range(2, width - 2):
                    red_sum = 0
                    green_sum = 0
                    blue_sum = 0

                    for ky in range(5):
                        for kx in range(5):
                            pixel = img.pixel(x - 2 + kx, y - 2 + ky)
                            red = QColor(pixel).red()
                            green = QColor(pixel).green()
                            blue = QColor(pixel).blue()

                            red_sum += red * gaussian_kernel[ky][kx]
                            green_sum += green * gaussian_kernel[ky][kx]
                            blue_sum += blue * gaussian_kernel[ky][kx]

                    red_sum = max(0, min(255, int(red_sum)))
                    green_sum = max(0, min(255, int(green_sum)))
                    blue_sum = max(0, min(255, int(blue_sum)))

                    gaussian_filtered_color = QColor(red_sum, green_sum, blue_sum)
                    gaussian_filtered_image.setPixel(x, y, gaussian_filtered_color.rgb())

            # Kemudian, konvolusi dengan filter LoG
            laplacian_filtered_image = QImage(width, height, QImage.Format_RGB32)

            for y in range(2, height - 2):
                for x in range(2, width - 2):
                    red_sum = 0
                    green_sum = 0
                    blue_sum = 0

                    for ky in range(5):
                        for kx in range(5):
                            pixel = gaussian_filtered_image.pixel(x - 2 + kx, y - 2 + ky)
                            red = QColor(pixel).red()
                            green = QColor(pixel).green()
                            blue = QColor(pixel).blue()

                            red_sum += red * log_kernel[ky][kx]
                            green_sum += green * log_kernel[ky][kx]
                            blue_sum += blue * log_kernel[ky][kx]

                    red_sum = max(0, min(255, int(red_sum)))
                    green_sum = max(0, min(255, int(green_sum)))
                    blue_sum = max(0, min(255, int(blue_sum)))

                    laplacian_filtered_color = QColor(red_sum, green_sum, blue_sum)
                    laplacian_filtered_image.setPixel(x, y, laplacian_filtered_color.rgb())
                    self.progressBar.setProperty("value", 100)
            
            self.pbOutput.setPixmap(QPixmap.fromImage(laplacian_filtered_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Laplacian of Gaussian Filter '
            self.labelOutput.setText(self.stringefek1)
            self.progressBar.setProperty("value", 0)
            self.showEffectComplete()


    def applyLaplacianFilter(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
                        
            self.progressBar.setProperty("value", 0)

            img = self.pixmap1.toImage()
            width, height = img.width(), img.height()

            laplacian_filtered_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Matriks filter Laplacian
            laplacian_kernel = [
                [0, -1, 0],
                [-1, 4, -1],
                [0, -1, 0]
            ]

            for y in range(1, height - 1):
                for x in range(1, width - 1):
                    red_sum = 0
                    green_sum = 0
                    blue_sum = 0

                    for ky in range(3):
                        for kx in range(3):
                            pixel = img.pixel(x - 1 + kx, y - 1 + ky)
                            red = QtGui.qRed(pixel)
                            green = QtGui.qGreen(pixel)
                            blue = QtGui.qBlue(pixel)

                            

                            # Mengalikan nilai piksel dengan matriks kernel Laplacian
                            red_sum += red * laplacian_kernel[ky][kx]
                            green_sum += green * laplacian_kernel[ky][kx]
                            blue_sum += blue * laplacian_kernel[ky][kx]

                    # Menyimpan hasil dari filter Laplacian
                    red_sum = max(0, min(255, red_sum))
                    green_sum = max(0, min(255, green_sum))
                    blue_sum = max(0, min(255, blue_sum))

                    laplacian_filtered_color = QtGui.QColor(red_sum, green_sum, blue_sum)
                    laplacian_filtered_image.setPixel(x, y, laplacian_filtered_color.rgb())
                    self.progressBar.setProperty("value", 100)

                self.pbOutput.setPixmap(QPixmap.fromImage(laplacian_filtered_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Laplacian Filter '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

    



    def apply1Bit(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
       
            input_image = self.pixmap1.toImage()

            
            width = input_image.width()
            height = input_image.height()

           
            output_image = QImage(width, height, QImage.Format_Mono)

           
            threshold = 128

           
            for y in range(height):
                for x in range(width):
                    pixel_color = input_image.pixelColor(x, y)
                    #(0.299R + 0.587G + 0.114B)
                    gray_value = int(0.299 * pixel_color.red() + 0.587 * pixel_color.green() + 0.114 * pixel_color.blue())
                    if gray_value >= threshold:
                        output_image.setPixel(x, y, 1)
                    else:
                        output_image.setPixel(x, y, 0)
                        self.progressBar.setProperty("value", 100)

                    

                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Bit Depth - 1 bit '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

            
    def apply2Bit(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():

            self.progressBar.setProperty("value", 0)

            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
        
            input_image = self.pixmap1.toImage()

            
            width = input_image.width()
            height = input_image.height()

            
            output_image = QImage(width, height, QImage.Format_MonoLSB)

            levels = [0, 85, 170, 255]

            
            for y in range(height):
                for x in range(width):
                    pixel_color = input_image.pixelColor(x, y)
                    #(0.299R + 0.587G + 0.114B)
                    gray_value = int(0.299 * pixel_color.red() + 0.587 * pixel_color.green() + 0.114 * pixel_color.blue())
                    
                    quantized_value = min(levels, key=lambda x: abs(x - gray_value))
                    output_image.setPixel(x, y, quantized_value)
                    self.progressBar.setProperty("value", 100)

                

                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Bit Depth - 2 bit '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

    def apply3Bit(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
        # Load the input image using PyQt5
            input_image = self.pixmap1.toImage()

           
            width = input_image.width()
            height = input_image.height()

          
            output_image = QImage(width, height, QImage.Format_RGB888)

          
            levels = [0, 32, 64, 96, 128, 160, 192, 224, 255]

           
            for y in range(height):
                for x in range(width):
                    pixel_color = input_image.pixelColor(x, y)
                    #(0.299R + 0.587G + 0.114B)
                    gray_value = int(0.299 * pixel_color.red() + 0.587 * pixel_color.green() + 0.114 * pixel_color.blue())
                    #3-bit (8 levels)
                    quantized_value = min(levels, key=lambda x: abs(x - gray_value))
                    
                    quantized_color = QColor(quantized_value, quantized_value, quantized_value)
                    
                    output_image.setPixelColor(x, y, quantized_color)
                    self.progressBar.setProperty("value", 100)

                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Bit Depth - 3 bit '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

    def apply4Bit(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
        
            input_image = self.pixmap1.toImage()

          
            width = input_image.width()
            height = input_image.height()

           # 4-bit image
            output_image = QImage(width, height, QImage.Format_RGB888)

            # Define the quantization levels (adjust as needed)
            levels = [0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]

            # 
            for y in range(height):
                for x in range(width):
                    pixel_color = input_image.pixelColor(x, y)
                    # (0.299R + 0.587G + 0.114B)
                    gray_value = int(0.299 * pixel_color.red() + 0.587 * pixel_color.green() + 0.114 * pixel_color.blue())
                    # 4-bit (16 levels)
                    quantized_value = min(levels, key=lambda x: abs(x - gray_value))
                    
                    quantized_color = QColor(quantized_value, quantized_value, quantized_value)
                    
                    output_image.setPixelColor(x, y, quantized_color)
                    self.progressBar.setProperty("value", 100)

                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Bit Depth - 4 bit '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()


    def apply5Bit(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
       
            input_image = self.pixmap1.toImage()

           
            width = input_image.width()
            height = input_image.height()

            # 5-bit image
            output_image = QImage(width, height, QImage.Format_RGB888)

            
            levels = [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 255]

            for y in range(height):
                for x in range(width):
                    pixel_color = input_image.pixelColor(x, y)
                    #(0.299R + 0.587G + 0.114B)
                    gray_value = int(0.299 * pixel_color.red() + 0.587 * pixel_color.green() + 0.114 * pixel_color.blue())
                    #5-bit (32 levels)
                    quantized_value = min(levels, key=lambda x: abs(x - gray_value))
                   
                    quantized_color = QColor(quantized_value, quantized_value, quantized_value)
                    
                    output_image.setPixelColor(x, y, quantized_color)
                    self.progressBar.setProperty("value", 100)

                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Bit Depth - 5 bit '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

    def apply6Bit(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
        
            input_image = self.pixmap1.toImage()

           
            width = input_image.width()
            height = input_image.height()

            #6-bit image
            output_image = QImage(width, height, QImage.Format_RGB888)

            levels = [
                0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60,
                64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112, 116, 120, 124,
                128, 132, 136, 140, 144, 148, 152, 156, 160, 164, 168, 172, 176, 180, 184, 188,
                192, 196, 200, 204, 208, 212, 216, 220, 224, 228, 232, 236, 240, 244, 248, 255
            ]

            for y in range(height):
                for x in range(width):
                    pixel_color = input_image.pixelColor(x, y)
                    #(0.299R + 0.587G + 0.114B)
                    gray_value = int(0.299 * pixel_color.red() + 0.587 * pixel_color.green() + 0.114 * pixel_color.blue())
                    #6-bit (64 levels)
                    quantized_value = min(levels, key=lambda x: abs(x - gray_value))
                    
                    quantized_color = QColor(quantized_value, quantized_value, quantized_value)
                    
                    output_image.setPixelColor(x, y, quantized_color)
                    self.progressBar.setProperty("value", 100)

                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Bit Depth - 6 bit '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

    def apply7Bit(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            input_image = self.pixmap1.toImage()

            width = input_image.width()
            height = input_image.height()

            #7-bit image
            output_image = QImage(width, height, QImage.Format_RGB888)

            # definisi 7 bit
            levels = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30,
                    32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62,
                    64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94,
                    96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 255]

            for y in range(height):
                for x in range(width):
                    pixel_color = input_image.pixelColor(x, y)
                    #(0.299R + 0.587G + 0.114B)
                    gray_value = int(0.299 * pixel_color.red() + 0.587 * pixel_color.green() + 0.114 * pixel_color.blue())
                    #7-bit (128 levels)
                    quantized_value = min(levels, key=lambda x: abs(x - gray_value))
                    
                    quantized_color = QColor(quantized_value, quantized_value, quantized_value)
                    
                    output_image.setPixelColor(x, y, quantized_color)
                    self.progressBar.setProperty("value", 100)

                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Bit Depth - 7 bit '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

    def apply8Bit(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
        
            input_image = self.pixmap1.toImage()

           
            width = input_image.width()
            height = input_image.height()

            #8-bit image
            output_image = QImage(width, height, QImage.Format_RGB888)

            #levels (256 levels)
            levels = list(range(256))

            
            for y in range(height):
                for x in range(width):
                    pixel_color = input_image.pixelColor(x, y)
                    #(0.299R + 0.587G + 0.114B)
                    gray_value = int(0.299 * pixel_color.red() + 0.587 * pixel_color.green() + 0.114 * pixel_color.blue())
                    #8-bit (256 levels)
                    quantized_value = min(levels, key=lambda x: abs(x - gray_value))
                
                    quantized_color = QColor(quantized_value, quantized_value, quantized_value)
                   
                    output_image.setPixelColor(x, y, quantized_color)
                    self.progressBar.setProperty("value", 100)

                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Bit Depth - 8 bit '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()
        

        # ----------------------------------------------------------------------------------------------------------
        # FUNGSI MENU IMAGE PROCESSING -----------------------------------------------------------------------------------------
        #HISTOGRAM EQUALIZATION (HE)
    def applyHistogramEqualization(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            input_image = self.pixmap1.toImage()
            width = input_image.width()
            height = input_image.height()

            equalized_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Menghitung histogram
            histogram = [0] * 256
            total_pixels = width * height
            

            for x in range(width):
                for y in range(height):
                    pixel_color = QtGui.QColor(*input_image.pixelColor(x, y).getRgb())
                    intensity = pixel_color.red()  # Kami asumsikan gambar grayscale

                    histogram[intensity] += 1

            # Menghitung distribusi kumulatif
            cumulative_distribution = [0] * 256
            cumulative_distribution[0] = histogram[0] / total_pixels

            for i in range(1, 256):
                cumulative_distribution[i] = cumulative_distribution[i - 1] + histogram[i] / total_pixels

            # Menyesuaikan nilai pixel pada gambar hasil
            for x in range(width):
                for y in range(height):
                    pixel_color = QtGui.QColor(*input_image.pixelColor(x, y).getRgb())
                    intensity = pixel_color.red()  # Kami asumsikan gambar grayscale

                    new_intensity = int(255 * cumulative_distribution[intensity])
                    new_color = QtGui.QColor(new_intensity, new_intensity, new_intensity)
                    equalized_image.setPixelColor(x, y, new_color)
                    self.progressBar.setProperty("value", 100)
            
                self.pbOutput.setPixmap(QPixmap.fromImage(equalized_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Histogram Equalization '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()
            
        #FUZZY HISTOGRAM EQUALIZATION (HE) RGB
    def fuzzy_he_rgb(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            input_image = self.pixmap1.toImage()
            width = input_image.width()
            height = input_image.height()

            # Mengambil data piksel dari gambar input
            input_data = np.zeros((height, width, 3), dtype=np.uint8)
            for y in range(height):
                for x in range(width):
                    color = QColor(input_image.pixel(x, y))
                    input_data[y, x, 0] = color.red()
                    input_data[y, x, 1] = color.green()
                    input_data[y, x, 2] = color.blue()

            # Menerapkan rumus Fuzzy HE RGB
            output_data = np.zeros_like(input_data)
            for i in range(3):  # Loop untuk saluran warna (R, G, B)
                for y in range(height):
                    for x in range(width):
                        val = input_data[y, x, i]
                        if val < 128:
                            output_data[y, x, i] = int(2 * val ** 2 / 255.0)
                        else:
                            output_data[y, x, i] = int(255 - 2 * (255 - val) ** 2 / 255.0)

            # Membuat gambar output dan menampilkannya di pbOutput
                output_image = QImage(output_data.data, width, height, width * 3, QImage.Format_RGB888)
                self.progressBar.setProperty("value", 100)

                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Fuzzy HE RGB '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

        #FUZZY TO GRAYSCALE
    def fuzzy_greyscale(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            input_image = self.pixmap1.toImage()
            width = input_image.width()
            height = input_image.height()

            # Mengambil data piksel dari gambar input
            input_data = np.zeros((height, width), dtype=np.uint8)
            for y in range(height):
                for x in range(width):
                    color = QColor(input_image.pixel(x, y))
                    # Menghitung nilai greyscale menggunakan rumus Fuzzy
                    val = int(0.3 * color.red() + 0.59 * color.green() + 0.11 * color.blue())
                    input_data[y, x] = val

            # Membuat gambar output dan menampilkannya di pbOutput
                output_image = QImage(input_data.data, width, height, width, QImage.Format_Grayscale8)
                self.progressBar.setProperty("value", 100)
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Fuzzy Grayscale '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

    def applyIdentity(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            img = self.pixmap1.toImage()
            width, height = img.width(), img.height()
          
            output_image = QImage(width, height, QImage.Format_RGB32)

            for y in range(height):
                for x in range(width):
                  
                    pixel = img.pixel(x, y)

                  
                    output_image.setPixel(x, y, pixel)
                    self.progressBar.setProperty("value", 100)

            # Display the output image
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Identity '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

    def applySharpen(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
        
            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

         
            output_image = QImage(width, height, QImage.Format_RGB32)

          
            kernel = [
                [-1, -1, -1],
                [-1, 9, -1],
                [-1, -1, -1]
            ]

            for y in range(1, height - 1):
                for x in range(1, width - 1):
                
                    new_red = 0
                    new_green = 0
                    new_blue = 0

                    for i in range(3):
                        for j in range(3):
                            pixel = img.pixel(x + i - 1, y + j - 1)
                            red = QColor(pixel).red()
                            green = QColor(pixel).green()
                            blue = QColor(pixel).blue()

                            new_red += red * kernel[i][j]
                            new_green += green * kernel[i][j]
                            new_blue += blue * kernel[i][j]

                    # [0, 255]
                    new_red = max(0, min(255, new_red))
                    new_green = max(0, min(255, new_green))
                    new_blue = max(0, min(255, new_blue))

                    
                    output_image.setPixel(x, y, qRgb(new_red, new_green, new_blue))
                    self.progressBar.setProperty("value", 100)

            # output Gambar
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Sharpen '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()


    def applyUnsharpMasking(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
        
            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            blur_kernel = [
                [1, 4, 6, 4, 1],
                [4, 16, 24, 16, 4],
                [6, 24, 36, 24, 6],
                [4, 16, 24, 16, 4],
                [1, 4, 6, 4, 1]
            ]

           
            blur_kernel_sum = sum(sum(row) for row in blur_kernel)
            blur_kernel = [[val / blur_kernel_sum for val in row] for row in blur_kernel]

            sharpen_kernel = [
                [-1, -1, -1],
                [-1, 9, -1],
                [-1, -1, -1]
            ]

            for y in range(2, height - 2):
                for x in range(2, width - 2):
                    blurred_red = 0
                    blurred_green = 0
                    blurred_blue = 0

                    for i in range(5):
                        for j in range(5):
                            pixel = img.pixel(x + i - 2, y + j - 2)
                            red = QColor(pixel).red()
                            green = QColor(pixel).green()
                            blue = QColor(pixel).blue()

                            blurred_red += red * blur_kernel[i][j]
                            blurred_green += green * blur_kernel[i][j]
                            blurred_blue += blue * blur_kernel[i][j]

                    #[0, 255]
                    blurred_red = max(0, min(255, int(blurred_red)))
                    blurred_green = max(0, min(255, int(blurred_green)))
                    blurred_blue = max(0, min(255, int(blurred_blue)))

                   
                    sharpened_red = 0
                    sharpened_green = 0
                    sharpened_blue = 0

                    for i in range(3):
                        for j in range(3):
                            pixel = img.pixel(x + i - 1, y + j - 1)
                            red = QColor(pixel).red()
                            green = QColor(pixel).green()
                            blue = QColor(pixel).blue()

                            sharpened_red += red * sharpen_kernel[i][j]
                            sharpened_green += green * sharpen_kernel[i][j]
                            sharpened_blue += blue * sharpen_kernel[i][j]

                    sharpened_red = max(0, min(255, int(sharpened_red)))
                    sharpened_green = max(0, min(255, int(sharpened_green)))
                    sharpened_blue = max(0, min(255, int(sharpened_blue)))

                    new_red = max(0, min(255, int(blurred_red - sharpened_red)))
                    new_green = max(0, min(255, int(blurred_green - sharpened_green)))
                    new_blue = max(0, min(255, int(blurred_blue - sharpened_blue)))

                    output_image.setPixel(x, y, qRgb(new_red, new_green, new_blue))
                    self.progressBar.setProperty("value", 100)

            # output gambar
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Unsharp Masking '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()


    def applyAverageFilter(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            filter_kernel = [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ]

            kernel_sum = sum(sum(row) for row in filter_kernel)
            filter_kernel = [[val / kernel_sum for val in row] for row in filter_kernel]

            for y in range(1, height - 1):
                for x in range(1, width - 1):
                
                    new_red = 0
                    new_green = 0
                    new_blue = 0

                    for i in range(3):
                        for j in range(3):
                            pixel = img.pixel(x + i - 1, y + j - 1)
                            red = QColor(pixel).red()
                            green = QColor(pixel).green()
                            blue = QColor(pixel).blue()

                            new_red += red * filter_kernel[i][j]
                            new_green += green * filter_kernel[i][j]
                            new_blue += blue * filter_kernel[i][j]

                    new_red = max(0, min(255, int(new_red)))
                    new_green = max(0, min(255, int(new_green)))
                    new_blue = max(0, min(255, int(new_blue)))

                    output_image.setPixel(x, y, qRgb(new_red, new_green, new_blue))
                    self.progressBar.setProperty("value", 100)

            #output gambar
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Average Filter '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()


    def applyLowPassFilter(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImagee
            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            filter_kernel = [
                [1, 2, 1],
                [2, 4, 2],
                [1, 2, 1]
            ]

            kernel_sum = sum(sum(row) for row in filter_kernel)
            filter_kernel = [[val / kernel_sum for val in row] for row in filter_kernel]

            for y in range(1, height - 1):
                for x in range(1, width - 1):
     
                    new_red = 0
                    new_green = 0
                    new_blue = 0

                    for i in range(3):
                        for j in range(3):
                            pixel = img.pixel(x + i - 1, y + j - 1)
                            red = QColor(pixel).red()
                            green = QColor(pixel).green()
                            blue = QColor(pixel).blue()

                            new_red += red * filter_kernel[i][j]
                            new_green += green * filter_kernel[i][j]
                            new_blue += blue * filter_kernel[i][j]

                    new_red = max(0, min(255, int(new_red)))
                    new_green = max(0, min(255, int(new_green)))
                    new_blue = max(0, min(255, int(new_blue)))

                    output_image.setPixel(x, y, qRgb(new_red, new_green, new_blue))
                    self.progressBar.setProperty("value", 100)

            # output gambar
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Low Pass Filter '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

    def applyHighPassFilter(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            filter_kernel = [
                [-1, -1, -1],
                [-1, 8, -1],
                [-1, -1, -1]
            ]

            for y in range(1, height - 1):
                for x in range(1, width - 1):
                    new_red = 0
                    new_green = 0
                    new_blue = 0

                    for i in range(3):
                        for j in range(3):
                            pixel = img.pixel(x + i - 1, y + j - 1)
                            red = QColor(pixel).red()
                            green = QColor(pixel).green()
                            blue = QColor(pixel).blue()

                            new_red += red * filter_kernel[i][j]
                            new_green += green * filter_kernel[i][j]
                            new_blue += blue * filter_kernel[i][j]

                    new_red = max(0, min(255, int(new_red)))
                    new_green = max(0, min(255, int(new_green)))
                    new_blue = max(0, min(255, int(new_blue)))

                    output_image.setPixel(x, y, qRgb(new_red, new_green, new_blue))
                    self.progressBar.setProperty("value", 100)

            # output gambar
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : High Pass Filter '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

        
    def applyBandstopFilter(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)

            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            filter_kernel = [
                [0, -1, 0],
                [-1, 5, -1],
                [0, -1, 0]
            ]

            for y in range(1, height - 1):
                for x in range(1, width - 1):

                    new_red = 0
                    new_green = 0
                    new_blue = 0

                    for i in range(3):
                        for j in range(3):
                            pixel = img.pixel(x + i - 1, y + j - 1)
                            red = QColor(pixel).red()
                            green = QColor(pixel).green()
                            blue = QColor(pixel).blue()

                            new_red += red * filter_kernel[i][j]
                            new_green += green * filter_kernel[i][j]
                            new_blue += blue * filter_kernel[i][j]

                    new_red = max(0, min(255, int(new_red)))
                    new_green = max(0, min(255, int(new_green)))
                    new_blue = max(0, min(255, int(new_blue)))

                    output_image.setPixel(x, y, qRgb(new_red, new_green, new_blue))
                    self.progressBar.setProperty("value", 100)

            # output gambar
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : BandStop Filter '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()
        
        # ----------------------------------------------------------------------------------------------------------
        # FUNGSI MENU EDGE DETECTION -----------------------------------------------------------------------------------------
        # PREWITT
    def applyPrewitt(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage

            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            prewitt_x = [
                [-1, 0, 1],
                [-1, 0, 1],
                [-1, 0, 1]
            ]

            prewitt_y = [
                [-1, -1, -1],
                [0, 0, 0],
                [1, 1, 1]
            ]

            for y in range(1, height - 1):
                for x in range(1, width - 1):
                    gradient_x_red = 0
                    gradient_x_green = 0
                    gradient_x_blue = 0
                    gradient_y_red = 0
                    gradient_y_green = 0
                    gradient_y_blue = 0

                    for i in range(3):
                        for j in range(3):
                            pixel = img.pixel(x + i - 1, y + j - 1)
                            red = QColor(pixel).red()
                            green = QColor(pixel).green()
                            blue = QColor(pixel).blue()

                            gradient_x_red += red * prewitt_x[i][j]
                            gradient_x_green += green * prewitt_x[i][j]
                            gradient_x_blue += blue * prewitt_x[i][j]

                            gradient_y_red += red * prewitt_y[i][j]
                            gradient_y_green += green * prewitt_y[i][j]
                            gradient_y_blue += blue * prewitt_y[i][j]

                    magnitude_red = abs(gradient_x_red) + abs(gradient_y_red)
                    magnitude_green = abs(gradient_x_green) + abs(gradient_y_green)
                    magnitude_blue = abs(gradient_x_blue) + abs(gradient_y_blue)

                    magnitude_red = max(0, min(255, int(magnitude_red)))
                    magnitude_green = max(0, min(255, int(magnitude_green)))
                    magnitude_blue = max(0, min(255, int(magnitude_blue)))

                    output_image.setPixel(x, y, qRgb(magnitude_red, magnitude_green, magnitude_blue))
                    self.progressBar.setProperty("value", 100)

            # output gambar
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Prewitt '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

        # SOBEL
    def applySobel(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage

            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            sobel_x = [
                [-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]
            ]

            sobel_y = [
                [-1, -2, -1],
                [0, 0, 0],
                [1, 2, 1]
            ]

            for y in range(1, height - 1):
                for x in range(1, width - 1):

                    gradient_x_red = 0
                    gradient_x_green = 0
                    gradient_x_blue = 0
                    gradient_y_red = 0
                    gradient_y_green = 0
                    gradient_y_blue = 0

                    for i in range(3):
                        for j in range(3):
                            pixel = img.pixel(x + i - 1, y + j - 1)
                            red = QColor(pixel).red()
                            green = QColor(pixel).green()
                            blue = QColor(pixel).blue()

                            gradient_x_red += red * sobel_x[i][j]
                            gradient_x_green += green * sobel_x[i][j]
                            gradient_x_blue += blue * sobel_x[i][j]

                            gradient_y_red += red * sobel_y[i][j]
                            gradient_y_green += green * sobel_y[i][j]
                            gradient_y_blue += blue * sobel_y[i][j]

                    magnitude_red = abs(gradient_x_red) + abs(gradient_y_red)
                    magnitude_green = abs(gradient_x_green) + abs(gradient_y_green)
                    magnitude_blue = abs(gradient_x_blue) + abs(gradient_y_blue)

                    magnitude_red = max(0, min(255, int(magnitude_red)))
                    magnitude_green = max(0, min(255, int(magnitude_green)))
                    magnitude_blue = max(0, min(255, int(magnitude_blue)))

                    output_image.setPixel(x, y, qRgb(magnitude_red, magnitude_green, magnitude_blue))
                    self.progressBar.setProperty("value", 100)

            # output gambar
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Sobel '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()
            
        # ROBERT
    def applyRobert(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage

            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            roberts_x = [
                [1, 0],
                [0, -1]
            ]

            roberts_y = [
                [0, 1],
                [-1, 0]
            ]

            for y in range(1, height - 1):
                for x in range(1, width - 1):
      
                    gradient_x_red = 0
                    gradient_x_green = 0
                    gradient_x_blue = 0
                    gradient_y_red = 0
                    gradient_y_green = 0
                    gradient_y_blue = 0

                    for i in range(2):
                        for j in range(2):
                            pixel = img.pixel(x + i - 1, y + j - 1)
                            red = QColor(pixel).red()
                            green = QColor(pixel).green()
                            blue = QColor(pixel).blue()

                            gradient_x_red += red * roberts_x[i][j]
                            gradient_x_green += green * roberts_x[i][j]
                            gradient_x_blue += blue * roberts_x[i][j]

                            gradient_y_red += red * roberts_y[i][j]
                            gradient_y_green += green * roberts_y[i][j]
                            gradient_y_blue += blue * roberts_y[i][j]

                    magnitude_red = abs(gradient_x_red) + abs(gradient_y_red)
                    magnitude_green = abs(gradient_x_green) + abs(gradient_y_green)
                    magnitude_blue = abs(gradient_x_blue) + abs(gradient_y_blue)

                    magnitude_red = max(0, min(255, int(magnitude_red)))
                    magnitude_green = max(0, min(255, int(magnitude_green)))
                    magnitude_blue = max(0, min(255, int(magnitude_blue)))

                    output_image.setPixel(x, y, qRgb(magnitude_red, magnitude_green, magnitude_blue))
                    self.progressBar.setProperty("value", 100)

            # output gambar
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Robert '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()
            
        # CANNY
    def applyCanny(self):
    # Load gambar dengan OpenCV
        input_image = self.pixmap1.toImage().convertToFormat(QImage.Format_Grayscale8)
        self.progressBar.setProperty("value", 0)

    # Mendapatkan ukuran gambar
        width = input_image.width()
        height = input_image.height()

        # Mengonversi gambar menjadi NumPy array
        input_image_np = np.empty((height, width), dtype=np.uint8)

        for y in range(height):
            for x in range(width):
                gray_val = input_image.pixelColor(x, y).black()
                input_image_np[y, x] = gray_val

        # Menerapkan Gaussian Blur
        blurred_image = cv2.GaussianBlur(input_image_np, (5, 5), 0)

        edges = cv2.Canny(blurred_image, 100, 200)

        height, width = edges.shape
        bytes_per_line = 1 * width
        output_image = QImage(edges.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
        self.progressBar.setProperty("value", 100)

        self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
        self.pbOutput.setScaledContents(True)
        self.stringefek1 = 'Effect : Canny '
        self.labelOutput.setText(self.stringefek1)
        self.showEffectComplete()
        self.progressBar.setProperty("value", 0)


    

            

        # ----------------------------------------------------------------------------------------------------------
        # FUNGSI MENU VIEW -----------------------------------------------------------------------------------------
        # HISTOGRAM INPUT
    def show_input_histogram(self):
            if self.pixmap1 is not None and not self.pixmap1.isNull():
                self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
                input_image = self.pixmap1.toImage()

                # Mengambil data piksel dari gambar input
                width = input_image.width()
                height = input_image.height()
                input_data = np.zeros((height, width), dtype=np.uint8)
                for y in range(height):
                    for x in range(width):
                        color = QColor(input_image.pixel(x, y))
                        val = int(0.3 * color.red() + 0.59 * color.green() + 0.11 * color.blue())
                        input_data[y, x] = val

                # Menghitung histogram
                histogram, bins = np.histogram(input_data, bins=256, range=(0, 256))

                # Menampilkan grafik histogram
                plt.figure(figsize=(8, 6))
                plt.bar(bins[:-1], histogram, width=1, color='blue')
                plt.title('Histogram Input')
                plt.xlabel('Intensitas Piksel')
                plt.ylabel('Frekuensi')
                plt.show()
    

    def show_output_histogram(self):
        output_image = self.pbOutput.pixmap().toImage()

        self.progressBar.setProperty("value", 0)

        width = output_image.width()
        height = output_image.height()
        output_data = np.zeros((height, width), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                color = QColor(output_image.pixel(x, y))
                val = int(0.3 * color.red() + 0.59 * color.green() + 0.11 * color.blue())
                output_data[y, x] = val

        histogram, bins = np.histogram(output_data, bins=256, range=(0, 256))

        plt.figure(figsize=(8, 6))
        plt.bar(bins[:-1], histogram, width=1, color='green')
        plt.title('Histogram Output')
        plt.xlabel('Intensitas Piksel')
        plt.ylabel('Frekuensi')
        plt.show()


        # ----------------------------------------------------------------------------------------------------------
        # FUNGSI AKSI PADA TOMBOL ----------------------------------------------------------------------------------
        # ATUR KE EFEK

    def undoEfek(self):
         if(self.pixmap4 is not None):
                self.stringefek3 = None
                self.pixmap4 = None
                if isinstance(self.pixmap3, QtGui.QImage):
                        self.pixmap1.setPixmap(QtGui.QPixmap.fromImage(self.pixmap3))
                elif isinstance(self.pixmap3, QtGui.QPixmap):
                        self.pixmap1.setPixmap(self.pixmap3)
                self.pbOutput.setPixmap(QtGui.QPixmap())
                self.buttonEffect3.setText("Tidak ada efek 3")
                self.buttonSet.setText("Atur ke efek 3")
                self.buttonSet.setEnabled(True)
                self.labelOutput.setText(None)
                self.pbPreview.setPixmap(QtGui.QPixmap())
         elif(self.pixmap3 is not None):
                self.stringefek2 = None
                self.pixmap3 = None
                if isinstance(self.pixmap2, QtGui.QImage):
                        self.pixmap1.setPixmap(QtGui.QPixmap.fromImage(self.pixmap2))
                elif isinstance(self.pixmap2, QtGui.QPixmap):
                        self.pixmap1.setPixmap(self.pixmap2)
                self.pbOutput.setPixmap(QtGui.QPixmap())
                self.buttonEffect2.setText("Tidak ada efek 2")
                self.buttonSet.setText("Atur ke efek 2")
                self.labelOutput.setText(None)
                self.pbPreview.setPixmap(QtGui.QPixmap())
         elif(self.pixmap2 is not None):
                self.stringefek1 = None
                self.pixmap2 = None
                if isinstance(self.pixmap1, QtGui.QImage):
                        self.pixmap1.setPixmap(QtGui.QPixmap.fromImage(self.pixmap1))
                elif isinstance(self.pixmap1, QtGui.QPixmap):
                        self.pixmap1.setPixmap(self.pixmap1)
                self.pbOutput.setPixmap(QtGui.QPixmap())
                self.buttonEffect1.setText("Tidak ada efek 1")
                self.buttonSet.setText("Atur ke efek 1")
                self.labelOutput.setText(None)
                self.pbPreview.setPixmap(QtGui.QPixmap())
 
    def showWarning(self):
        self.labelWarning.setText("Tidak ada efek yang diterapkan pada Gambar Keluaran")
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.clearWarning)
        self.timer.start()

    def showWarningAtur1(self):
        self.labelWarning.setText("Efek tidak dapat diatur!")
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.clearWarning)
        self.timer.start()

    def showImageData(self):
        if (self.width > 1000 and self.height > 1000):
             self.labelWarning.setText("<b>Lebar Gambar (Width) :</b> " + str(self.width) + "<br><b>Tinggi Gambar (Height) :</b> " + str(self.height) + "<br>Gambar dengan resolusi di atas 1000 x 1000 mungkin akan memakan lebih<br>banyak waktu ketika menerapkan efek")
        else:
             self.labelWarning.setText("<b>Lebar Gambar (Width) :</b> " + str(self.width) + "<br><b>Tinggi Gambar (Height) :</b> " + str(self.height))
        self.timer.setInterval(30000)
        self.timer.timeout.connect(self.clearWarning)
        self.timer.start()

    def showWarningSave(self):
        self.labelWarning.setText("Gambar output kosong\nHarap tambahkan efek untuk menampilkan pada gambar output")
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.clearWarning)
        self.timer.start()

    def showEffectprogress(self):
        self.labelLoading.setText( self.stringefek1 + "Berhasil Diterapkan")
        self.timerEfek.setInterval(3000)
        self.timerEfek.timeout.connect(self.clearLoading)
        self.timerEfek.start()


    def showEffectComplete(self):
        self.labelLoading.setText( self.stringefek1 + "Sedang Diterapkan")
        self.timerEfek.setInterval(0)
        self.timerEfek.timeout.connect(self.showEffectprogress)
        self.timerEfek.start()
        # self.showEffectprogress()

    

    def clearLoading(self):
        self.labelLoading.clear()
        self.timerEfek.stop()

    def clearWarning(self):
        self.labelWarning.clear()
        self.timer.stop()

    def showPreviewEffect1(self):
        if isinstance(self.pixmap2, QtGui.QImage):
                self.pbPreview.setPixmap(QtGui.QPixmap.fromImage(self.pixmap2))
        elif isinstance(self.pixmap2, QtGui.QPixmap):
                self.pbPreview.setPixmap(self.pixmap2)

    def showPreviewEffect2(self):
        if isinstance(self.pixmap3, QtGui.QImage):
                self.pbPreview.setPixmap(QtGui.QPixmap.fromImage(self.pixmap3))
        elif isinstance(self.pixmap3, QtGui.QPixmap):
                self.pbPreview.setPixmap(self.pixmap3)

    def showPreviewEffect3(self):
        if isinstance(self.pixmap4, QtGui.QImage):
                self.pbPreview.setPixmap(QtGui.QPixmap.fromImage(self.pixmap4))
        elif isinstance(self.pixmap4, QtGui.QPixmap):
                self.pbPreview.setPixmap(self.pixmap4)

    def open_aritmatics_panel(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Aritmath()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()


    def open_roi(self):
    # Periksa apakah instance Ui_roi sudah ada atau belum
        if not hasattr(self, 'roi_window'):
            self.roi_window = Ui_roi()
            self.roi_window.show()
        else:
            # Jika instance sudah ada, hanya perlihatkan jendela yang sudah ada
            self.roi_window.show()


    
    def applyRed(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            red_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            for x in range(red_image.width()):
                for y in range(red_image.height()):
                    pixel_color = QColor(red_image.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()
                    # Tingkatkan nilai warna hijau (G), tetapkan nilai warna merah (R) dan biru (B) tetap
                    new_r = min(r + 50, 255)
                    new_color = QColor( new_r, g , b)
                    red_image.setPixelColor(x, y, new_color)
                    self.progressBar.setProperty("value", 100)

            self.pbOutput.setPixmap(QPixmap.fromImage(red_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : RGB Red '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)


    def applyGreen(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            green_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            for x in range(green_image.width()):
                for y in range(green_image.height()):
                    pixel_color = QColor(green_image.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()
                    # Tingkatkan nilai warna hijau (G), tetapkan nilai warna merah (R) dan biru (B) tetap
                    new_g = min(g + 50, 255)
                    new_color = QColor(r, new_g, b)
                    green_image.setPixelColor(x, y, new_color)
                    self.progressBar.setProperty("value", 100)
            self.pbOutput.setPixmap(QPixmap.fromImage(green_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : RGB Green '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)


    def applyBlue(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            blue_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            for x in range(blue_image.width()):
                for y in range(blue_image.height()):
                    pixel_color = QColor(blue_image.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()
                    # Tingkatkan nilai warna biru (B), tetapkan nilai warna merah (R) dan hijau (G) tetap
                    new_b = min(b + 50, 255)
                    new_color = QColor(r, g, new_b)
                    blue_image.setPixelColor(x, y, new_color)
                    self.progressBar.setProperty("value", 100)
            self.pbOutput.setPixmap(QPixmap.fromImage(blue_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : RGB Blue '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)


    def applyGray(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            gray_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            for x in range(gray_image.width()):
                for y in range(gray_image.height()):
                    pixel_color = QColor(gray_image.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()
                    # Hitung rata-rata dari komponen warna (merah, hijau, biru) dan tetapkan semuanya ke nilai yang sama
                    gray_value = (r + g + b) // 3
                    new_color = QColor(gray_value, gray_value, gray_value)
                    gray_image.setPixelColor(x, y, new_color)
                    self.progressBar.setProperty("value", 100)
            self.pbOutput.setPixmap(QPixmap.fromImage(gray_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : RGB Gray '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)


    def applyPink(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            pink_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            for x in range(pink_image.width()):
                for y in range(pink_image.height()):
                    pixel_color = QColor(pink_image.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()
                    # Tingkatkan nilai warna merah (R) dan biru (B), tetapkan nilai warna hijau (G) tetap
                    new_r = min(r + 50, 255)
                    new_b = min(b + 50, 255)
                    new_color = QColor(new_r, g, new_b)
                    pink_image.setPixelColor(x, y, new_color)
                    self.progressBar.setProperty("value", 100)
            self.pbOutput.setPixmap(QPixmap.fromImage(pink_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : RGB Pink '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)


    # kode warna Kuning
    def applyYellow(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            for x in range(yellow_image.width()):
                for y in range(yellow_image.height()):
                    color = yellow_image.pixelColor(x, y)
                    r, g, b = color.red(), color.green(), color.blue()
                    new_r = r
                    new_g = g
                    new_b = 0 
                    yellow_image.setPixelColor(x, y, QColor(new_r, new_g, new_b))
                    self.progressBar.setProperty("value", 100)
            self.pbOutput.setPixmap(QPixmap.fromImage(yellow_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : RGB Yellow '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)

    def applyOrange(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            orange_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            for x in range(orange_image.width()):
                for y in range(orange_image.height()):
                    pixel_color = QColor(orange_image.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()

                    new_r = min(r + 50, 255)
                    new_g = max(g - 50, 0)
                    new_b = max(b - 50, 0)
                    new_color = QColor(new_r, new_g, new_b)
                    orange_image.setPixelColor(x, y, new_color)
                    self.progressBar.setProperty("value", 100)
            self.pbOutput.setPixmap(QPixmap.fromImage(orange_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : RGB Orange '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)
    



    def applyCyan(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            cyan_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            for x in range(cyan_image.width()):
                for y in range(cyan_image.height()):
                    pixel_color = QColor(cyan_image.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()
                    # Tingkatkan nilai warna hijau (G) dan biru (B), tetapkan nilai warna merah (R) tetap
                    new_g = min(g + 50, 255)
                    new_b = min(b + 50, 255)
                    new_color = QColor(r, new_g, new_b)
                    cyan_image.setPixelColor(x, y, new_color)
                    self.progressBar.setProperty("value", 100)
            self.pbOutput.setPixmap(QPixmap.fromImage(cyan_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : RGB Cyan '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)


    def applyPurple(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            purple_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            for x in range(purple_image.width()):
                for y in range(purple_image.height()):
                    pixel_color = QColor(purple_image.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()

                    new_r = max(r - 50, 0)
                    new_g = max(g - 50, 0)
                    new_b = max(b + 50, 255)
                    new_color = QColor(new_r, new_g, new_b)
                    purple_image.setPixelColor(x, y, new_color)
                    self.progressBar.setProperty("value", 100)
            self.pbOutput.setPixmap(QPixmap.fromImage(purple_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : RGB Purple '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)

    # def applyPurple(self):
    #     if self.pixmap1 is not None and not self.pixmap1.isNull():
            # self.progressBar.setProperty("value", 0)
    #         image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
    #         for x in range(image.width()):
    #             for y in range(image.height()):
    #                 pixel_color = QColor(image.pixel(x, y))
    #                 red, green, blue = pixel_color.red(), pixel_color.green(), pixel_color.blue()
            
    #                 pixel_color.setRed(255)
    #                 pixel_color.setBlue(255)
               
    #                 image.setPixel(x, y, pixel_color.rgb())
     
    #         modified_pixmap = QPixmap.fromImage(image)
    #         self.pbOutput.setPixmap(modified_pixmap)
    #         self.stringefek1 = 'Effect : RGB Purple '
    #         self.labelOutput.setText(self.stringefek1)
    #         self.progressBar.setProperty("value", 0)
    #         self.progressBar.setProperty("value", 25)
    #         
    #         self.progressBar.setProperty("value", 75)
    #         self.progressBar.setProperty("value", 0)
    #         self.showEffectComplete()



    def load_data(self):
       
        self.progressBar.show()

        # Simulate a loading process
        for i in range(101):
            QtCore.QCoreApplication.processEvents(Ui_MainWindow)  
            self.progressBar.setValue(i)  
            QtCore.QThread.msleep(20)  
        self.progressBar.hide()


    def flip_horizontal(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            width = image.width()  # Perubahan ini
            height = image.height()  # Perubahan ini

            flipped_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGBA8888)

            for y in range(height):
                for x in range(width):
                    pixel_color = QtGui.QColor(image.pixel(x, y))
                    flipped_image.setPixelColor(width - 1 - x, y, pixel_color)
                    self.progressBar.setProperty("value", 100)       

            flipped_pixmap = QtGui.QPixmap.fromImage(flipped_image)
            self.pbOutput.setPixmap(flipped_pixmap)
            self.pbOutput.setAlignment(QtCore.Qt.AlignCenter)
            self.image = flipped_image
            self.stringefek1 = 'Effect : Flip Horizontal '
            self.labelOutput.setText(self.stringefek1)
            self.progressBar.setProperty("value", 0)
            self.showEffectComplete()

            
    def flip_vertical(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            width = image.width()
            height = image.height()

            flipped_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGBA8888)

            for y in range(height):
                for x in range(width):
                    pixel_color = QtGui.QColor(image.pixel(x, y))
                    flipped_image.setPixelColor(x, height - 1 - y, pixel_color) 

            flipped_pixmap = QtGui.QPixmap.fromImage(flipped_image)
            self.progressBar.setProperty("value", 100)
            self.pbOutput.setPixmap(flipped_pixmap)
            self.pbOutput.setAlignment(QtCore.Qt.AlignCenter)
            self.image = flipped_image 
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Flip Vertical '
            self.labelOutput.setText(self.stringefek1)
            self.progressBar.setProperty("value", 0)
            self.showEffectComplete()


    def rotate(self):
        rotation, ok = QtWidgets.QInputDialog.getInt(None, "Rotate Image", "Enter rotation angle (degrees):", 0, -360, 360)
        if ok:
            if self.pixmap1 is not None and not self.pixmap1.isNull():
                self.progressBar.setProperty("value", 0)
                current_pixmap = self.pixmap1
                second_pixmap = self.pbOutput.pixmap()

                if self.pbOutput.pixmap() is None:
                    rotated_image = current_pixmap.transformed(QtGui.QTransform().rotate(rotation))
                    self.progressBar.setProperty("value", 100)
                    self.pbOutput.setPixmap(rotated_image)
                    self.pbOutput.setAlignment(QtCore.Qt.AlignCenter)
                    self.pbOutput.setScaledContents(True)
                    self.image = rotated_image.toImage()
                    self.stringefek1 = 'Effect : Rotate '
                    self.labelOutput.setText(self.stringefek1)
                    self.progressBar.setProperty("value", 0)
                    self.showEffectComplete()
                else:
                    rotated_image = second_pixmap.transformed(QtGui.QTransform().rotate(rotation))
                    self.progressBar.setProperty("value", 100)
                    self.pbOutput.setPixmap(rotated_image)
                    self.pbOutput.setAlignment(QtCore.Qt.AlignCenter)
                    self.pbOutput.setScaledContents(True)
                    self.image = rotated_image.toImage()
                    self.stringefek2 = 'Effect : Rotate '
                    self.labelOutput.setText(self.stringefek2)
                    self.progressBar.setProperty("value", 0)
                    self.showEffectComplete()
            else:
                print("self.pixmap1 is not a valid QPixmap")

    
    def applyCropping(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            input_image = self.pixmap1.toImage()

            width = input_image.width()
            height = input_image.height()

            crop_x = width // 4
            crop_y = height // 4
            crop_width = width // 2
            crop_height = height // 2

            output_image = QImage(crop_width, crop_height, QImage.Format_RGB32)

            for y in range(crop_height):
                for x in range(crop_width):
                    source_x = crop_x + x
                    source_y = crop_y + y

                    pixel_color = input_image.pixelColor(source_x, source_y)

                    output_image.setPixelColor(x, y, pixel_color)
                    self.progressBar.setProperty("value", 100)

            # output gambar
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Cropping '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()
            
    def applyTranslasi(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            input_image = self.pixmap1.toImage()

            width = input_image.width()
            height = input_image.height()

            dx = 50  # Horizontal
            dy = 30  # Vertical

            output_image = QImage(width, height, QImage.Format_RGB32)

            for y in range(height):
                for x in range(width):
                    if 0 <= x - dx < width and 0 <= y - dy < height:
                        pixel_color = input_image.pixelColor(x - dx, y - dy)
                    else:
                        pixel_color = input_image.pixelColor(x, y)

                    output_image.setPixelColor(x, y, pixel_color)
                    self.progressBar.setProperty("value", 100)

            # output gambar
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Translasi '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()


    def applyGaussianBlur3(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            kernel = [
                [1, 2, 1],
                [2, 4, 2],
                [1, 2, 1]
            ]

            kernel_sum = sum(sum(row) for row in kernel)
            kernel = [[val / kernel_sum for val in row] for row in kernel]

            for y in range(1, height - 1):
                for x in range(1, width - 1):
   
                    new_red = 0
                    new_green = 0
                    new_blue = 0

                    for i in range(3):
                        for j in range(3):
                            pixel = img.pixel(x + i - 1, y + j - 1)
                            red = QColor(pixel).red()
                            green = QColor(pixel).green()
                            blue = QColor(pixel).blue()

                            new_red += red * kernel[i][j]
                            new_green += green * kernel[i][j]
                            new_blue += blue * kernel[i][j]

                    new_red = max(0, min(255, int(new_red)))
                    new_green = max(0, min(255, int(new_green)))
                    new_blue = max(0, min(255, int(new_blue)))

                    output_image.setPixel(x, y, qRgb(new_red, new_green, new_blue))
                    self.progressBar.setProperty("value", 100)

            # output gambar
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Gaussian Blur 3x3 '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

    def applyGaussianBlur5(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            kernel = [
                [1, 4, 6, 4, 1],
                [4, 16, 24, 16, 4],
                [6, 24, 36, 24, 6],
                [4, 16, 24, 16, 4],
                [1, 4, 6, 4, 1]
            ]

            kernel_sum = sum(sum(row) for row in kernel)
            kernel = [[val / kernel_sum for val in row] for row in kernel]

            for y in range(2, height - 2):
                for x in range(2, width - 2):
        
                    new_red = 0
                    new_green = 0
                    new_blue = 0

                    for i in range(5):
                        for j in range(5):
                            pixel = img.pixel(x + i - 2, y + j - 2)
                            red = QColor(pixel).red()
                            green = QColor(pixel).green()
                            blue = QColor(pixel).blue()

                            new_red += red * kernel[i][j]
                            new_green += green * kernel[i][j]
                            new_blue += blue * kernel[i][j]

                    new_red = max(0, min(255, int(new_red)))
                    new_green = max(0, min(255, int(new_green)))
                    new_blue = max(0, min(255, int(new_blue)))

                    output_image.setPixel(x, y, qRgb(new_red, new_green, new_blue))
                    self.progressBar.setProperty("value", 100)

            # output gambar
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Gaussian Blur 5x5 '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()

    

    # def applyUniformScaling(self):
    #     if self.pixmap1 is not None and not self.pixmap1.isNull():
    #         self.progressBar.setProperty("value", 0)
    #         # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
    #         input_image = self.pixmap1.toImage()

    #         width = input_image.width()
    #         height = input_image.height()

    #         scale_factor = 2.0

    #         new_width = int(width * scale_factor)
    #         new_height = int(height * scale_factor)

    #         output_image = QImage(new_width, new_height, QImage.Format_RGB32)

    #         transform = QTransform()
    #         transform.scale(scale_factor, scale_factor)

    #         for y in range(new_height):
    #             for x in range(new_width):
    #                 source_x, source_y = transform.map(x, y)
    #                 if 0 <= source_x < width and 0 <= source_y < height:
    #                     pixel_color = input_image.pixelColor(source_x, source_y)
    #                 else:
    #                     pixel_color = input_image.pixelColor(0, 0)

    #                 output_image.setPixelColor(x, y, pixel_color)

    #         # output gambar
    #             self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
    #             self.pbOutput.setScaledContents(True)
    #             self.stringefek1 = 'Effect : Uniform Scalling '
    #             self.labelOutput.setText(self.stringefek1)
    #             self.showEffectComplete()
    #             self.progressBar.setProperty("value", 0)

    def applyUniformScaling(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            
            scale_factor, ok = QInputDialog.getDouble(self.centralwidget, "Uniform Scaling", "Enter scaling factor:")
            if not ok:
                return

            input_image = self.pixmap1.toImage()

            width = input_image.width()
            height = input_image.height()

            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)

            output_image = QImage(new_width, new_height, QImage.Format_RGB32)

            transform = QTransform()
            transform.scale(scale_factor, scale_factor)

            for y in range(new_height):
                for x in range(new_width):
                    source_x, source_y = transform.map(x, y)
                    if 0 <= source_x < width and 0 <= source_y < height:
                        pixel_color = input_image.pixelColor(source_x, source_y)
                    else:
                        pixel_color = input_image.pixelColor(0, 0)

                    output_image.setPixelColor(x, y, pixel_color)
                    self.progressBar.setProperty("value", 100)

            self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Uniform Scalling '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)


    def applyNonUniformScaling(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            input_image = self.pixmap1.toImage()

            width = input_image.width()
            height = input_image.height()

            scale_factor_x = 1.5  #(horizontal scaling)
            scale_factor_y = 0.5  #(vertical scaling)

            new_width = int(width * scale_factor_x)
            new_height = int(height * scale_factor_y)

            output_image = QImage(new_width, new_height, QImage.Format_RGB32)

            transform = QTransform()
            transform.scale(scale_factor_x, scale_factor_y)

            for y in range(new_height):
                for x in range(new_width):
                    source_x, source_y = transform.map(x, y)
                    if 0 <= source_x < width and 0 <= source_y < height:
                        pixel_color = input_image.pixelColor(source_x, source_y)
                    else:
                        pixel_color = input_image.pixelColor(0, 0)  #background color

                    output_image.setPixelColor(x, y, pixel_color)
                    self.progressBar.setProperty("value", 100)

            # output gambar
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : NonUniform Scalling '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()


    # def applyNonUniformScaling(self):
    #     if self.pixmap1 is not None and not self.pixmap1.isNull():
    #         self.progressBar.setProperty("value", 0)

    #         scale_factor_x, ok_x = QInputDialog.getDouble(self.centralwidget, "Non-Uniform Scaling", "Enter X scaling factor:")
    #         scale_factor_y, ok_y = QInputDialog.getDouble(self.centralwidget, "Non-Uniform Scaling", "Enter Y scaling factor:")

    #         if ok_x and ok_y:
    #             input_image = self.pixmap1.toImage()

    #             width = input_image.width()
    #             height = input_image.height()

    #             new_width = int(width * scale_factor_x)
    #             new_height = int(height * scale_factor_y)

    #             output_image = QImage(new_width, new_height, QImage.Format_RGB32)

    #             for y in range(new_height):
    #                 for x in range(new_width):
    #                     source_x = x / scale_factor_x
    #                     source_y = y / scale_factor_y

    #                     x1 = int(source_x)
    #                     y1 = int(source_y)
    #                     x2 = min(x1 + 1, width - 1)
    #                     y2 = min(y1 + 1, height - 1)

    #                     dx = source_x - x1
    #                     dy = source_y - y1

    #                     pixel_color1 = input_image.pixelColor(x1, y1)
    #                     pixel_color2 = input_image.pixelColor(x2, y1)
    #                     pixel_color3 = input_image.pixelColor(x1, y2)
    #                     pixel_color4 = input_image.pixelColor(x2, y2)

    #                     interpolated_color = QColor()
    #                     interpolated_color.setRedF((1 - dx) * (1 - dy) * pixel_color1.redF() +
    #                                             dx * (1 - dy) * pixel_color2.redF() +
    #                                             (1 - dx) * dy * pixel_color3.redF() +
    #                                             dx * dy * pixel_color4.redF())
    #                     interpolated_color.setGreenF((1 - dx) * (1 - dy) * pixel_color1.greenF() +
    #                                                 dx * (1 - dy) * pixel_color2.greenF() +
    #                                                 (1 - dx) * dy * pixel_color3.greenF() +
    #                                                 dx * dy * pixel_color4.greenF())
    #                     interpolated_color.setBlueF((1 - dx) * (1 - dy) * pixel_color1.blueF() +
    #                                                 dx * (1 - dy) * pixel_color2.blueF() +
    #                                                 (1 - dx) * dy * pixel_color3.blueF() +
    #                                                 dx * dy * pixel_color4.blueF())

    #                     output_image.setPixelColor(x, y, interpolated_color)

    #             self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
    #             self.pbOutput.setScaledContents(True)
    #             self.stringefek1 = 'Effect : NonUniform Scalling '
    #             self.labelOutput.setText(self.stringefek1)
    #             self.showEffectComplete()
    #             self.progressBar.setProperty("value", 0)




    # def applyNonUniformScaling(self):
    #     if self.pixmap1 is not None and not self.pixmap1.isNull():
    #         self.progressBar.setProperty("value", 0)
            
    #         scale_factor_width, ok_width = QInputDialog.getDouble(self.centralwidget, "Non-Uniform Scaling", "Enter scaling factor for width:")
    #         scale_factor_height, ok_height = QInputDialog.getDouble(self.centralwidget, "Non-Uniform Scaling", "Enter scaling factor for height:")
            
    #         if not ok_width or not ok_height:
    #             return

    #         input_image = self.pixmap1.toImage()

    #         width = input_image.width()
    #         height = input_image.height()

    #         new_width = int(width * scale_factor_width)
    #         new_height = int(height * scale_factor_height)

    #         output_image = QImage(new_width, new_height, QImage.Format_RGB32)

    #         for y in range(new_height):
    #             for x in range(new_width):
    #                 source_x = int(x / scale_factor_width)
    #                 source_y = int(y / scale_factor_height)
                    
    #                 if 0 <= source_x < width and 0 <= source_y < height:
    #                     pixel_color = input_image.pixelColor(source_x, source_y)
    #                 else:
    #                     pixel_color = input_image.pixelColor(0, 0)

    #                 output_image.setPixelColor(x, y, pixel_color)

    #         self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
    #         self.pbOutput.setScaledContents(True)
    #         self.stringefek1 = 'Effect : Non-Uniform Scalling '
    #         self.labelOutput.setText(self.stringefek1)
    #         self.showEffectComplete()
    #         self.progressBar.setProperty("value", 0)



        # ----------------------------------------------------------------------------------------------------------
        # FUNGSI MENU MORPHOLOGY -----------------------------------------------------------------------------------------
        # EROTION - SQUARE 3X3
    def applyErotionSquare3(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()
            output_image = QImage(width, height, QImage.Format_RGB32)

            for y in range(1, height - 1):
                for x in range(1, width - 1):
                    pixels = []
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            pixel = img.pixel(x + i, y + j)
                            pixels.append(QColor(pixel).red())

                    min_value = min(pixels)

                    output_image.setPixel(x, y, qRgb(min_value, min_value, min_value))
                    self.progressBar.setProperty("value", 100)

            # output gambar
                self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Erotion-Square 3 '
                self.labelOutput.setText(self.stringefek1)
                self.progressBar.setProperty("value", 0)
                self.showEffectComplete()
            
        # EROTION - SQUARE 5X5
    def applyErotionSquare5(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            for y in range(2, height - 2):
                for x in range(2, width - 2):

                    pixels = []
                    for i in range(-2, 3):
                        for j in range(-2, 3):
                            pixel = img.pixel(x + i, y + j)
                            pixels.append(QColor(pixel).red())

                    min_value = min(pixels)

                    output_image.setPixel(x, y, qRgb(min_value, min_value, min_value))
                    self.progressBar.setProperty("value", 100)

            # output gambar
            self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Erotion-Square 5 '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)

        # EROTION - CROSS 3X3
    def applyErotionCross3(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            for y in range(1, height - 1):
                for x in range(1, width - 1):
                    pixels = [
                        QColor(img.pixel(x, y - 1)).red(),
                        QColor(img.pixel(x, y + 1)).red(),
                        QColor(img.pixel(x - 1, y)).red(),
                        QColor(img.pixel(x + 1, y)).red(),
                        QColor(img.pixel(x, y)).red()
                    ]
                    min_value = min(pixels)

                    output_image.setPixel(x, y, qRgb(min_value, min_value, min_value))
                    self.progressBar.setProperty("value", 100)

            # output gambar
            self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Erotion-cross 3 '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)

        # DILATION - SQUARE 3X3
    def applyDilationSquare3(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            for y in range(1, height - 1):
                for x in range(1, width - 1):
                    pixels = [
                        QColor(img.pixel(x - 1, y - 1)).red(),
                        QColor(img.pixel(x, y - 1)).red(),
                        QColor(img.pixel(x + 1, y - 1)).red(),
                        QColor(img.pixel(x - 1, y)).red(),
                        QColor(img.pixel(x, y)).red(),
                        QColor(img.pixel(x + 1, y)).red(),
                        QColor(img.pixel(x - 1, y + 1)).red(),
                        QColor(img.pixel(x, y + 1)).red(),
                        QColor(img.pixel(x + 1, y + 1)).red()
                    ]

                    max_value = max(pixels)

                    output_image.setPixel(x, y, qRgb(max_value, max_value, max_value))
                    self.progressBar.setProperty("value", 100)

            # output gambar
            self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Dilation-Square 3 '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)

        # DILATION - SQUARE 5X5
    def applyDilationSquare5(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            for y in range(2, height - 2):
                for x in range(2, width - 2):
                    pixels = [
                        QColor(img.pixel(x - 2, y - 2)).red(),
                        QColor(img.pixel(x - 1, y - 2)).red(),
                        QColor(img.pixel(x, y - 2)).red(),
                        QColor(img.pixel(x + 1, y - 2)).red(),
                        QColor(img.pixel(x + 2, y - 2)).red(),
                        QColor(img.pixel(x - 2, y - 1)).red(),
                        QColor(img.pixel(x - 1, y - 1)).red(),
                        QColor(img.pixel(x, y - 1)).red(),
                        QColor(img.pixel(x + 1, y - 1)).red(),
                        QColor(img.pixel(x + 2, y - 1)).red(),
                        QColor(img.pixel(x - 2, y)).red(),
                        QColor(img.pixel(x - 1, y)).red(),
                        QColor(img.pixel(x, y)).red(),
                        QColor(img.pixel(x + 1, y)).red(),
                        QColor(img.pixel(x + 2, y)).red(),
                        QColor(img.pixel(x - 2, y + 1)).red(),
                        QColor(img.pixel(x - 1, y + 1)).red(),
                        QColor(img.pixel(x, y + 1)).red(),
                        QColor(img.pixel(x + 1, y + 1)).red(),
                        QColor(img.pixel(x + 2, y + 1)).red(),
                        QColor(img.pixel(x - 2, y + 2)).red(),
                        QColor(img.pixel(x - 1, y + 2)).red(),
                        QColor(img.pixel(x, y + 2)).red(),
                        QColor(img.pixel(x + 1, y + 2)).red(),
                        QColor(img.pixel(x + 2, y + 2)).red()
                    ]

                    max_value = max(pixels)

                    output_image.setPixel(x, y, qRgb(max_value, max_value, max_value))
                    self.progressBar.setProperty("value", 100)

            # output gambar
            self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Dilation-Square 5 '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)

        # DILATION - CROSS 3X3
    def applyDilationCross3(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            for y in range(1, height - 1):
                for x in range(1, width - 1):
                    pixels = [
                        QColor(img.pixel(x, y - 1)).red(),
                        QColor(img.pixel(x, y + 1)).red(),
                        QColor(img.pixel(x - 1, y)).red(),
                        QColor(img.pixel(x + 1, y)).red(),
                        QColor(img.pixel(x, y)).red()
                    ]

                    max_value = max(pixels)

                    output_image.setPixel(x, y, qRgb(max_value, max_value, max_value))
                    self.progressBar.setProperty("value", 100)

            # output gambar
            self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Dilation-Cross 3 '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)

        # OPENING - SQUARE 9X9
    # def applyOpeningSquare9(self):
    #     if self.pixmap1 is not None and not self.pixmap1.isNull():
    #         self.progressBar.setProperty("value", 0)
    #         # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
    #         img = self.pixmap1.toImage()

    #         width, height = img.width(), img.height()

    #         output_image = QImage(width, height, QImage.Format_RGB32)

    #         structuring_element_size = 9

    #         padding_size = structuring_element_size // 2

    #         for y in range(padding_size, height - padding_size):
    #             for x in range(padding_size, width - padding_size):
    #                 pixels = []
    #                 for i in range(-padding_size, padding_size + 1):
    #                     for j in range(-padding_size, padding_size + 1):
    #                         pixel = img.pixel(x + i, y + j)
    #                         pixels.append(QColor(pixel).red())

    #                 if all(pixel == 255 for pixel in pixels):

    #                     output_image.setPixel(x, y, qRgb(255, 255, 255))
    #                 else:
    #                     output_image.setPixel(x, y, qRgb(0, 0, 0))

    #         # output gambar
    #         self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
    #         self.pbOutput.setScaledContents(True)
    #         self.stringefek1 = 'Effect : Opening-Square 9 '
    #         self.labelOutput.setText(self.stringefek1)
    #         self.showEffectComplete()
    #         self.progressBar.setProperty("value", 0)

    # def applyOpeningSquare9(self):
    #     if self.pixmap1 is not None and not self.pixmap1.isNull():
    #         self.progressBar.setProperty("value", 0)
            
    #         img = self.pixmap1.toImage()
    #         width, height = img.width(), img.height()

    #         # Buat citra hasil erosi dan dilasi
    #         eroded_image = QImage(width, height, QImage.Format_RGB32)
    #         dilated_image = QImage(width, height, QImage.Format_RGB32)

    #         structuring_element_size = 9
    #         padding_size = structuring_element_size // 2

    #         # Tahap erosi
    #         for y in range(padding_size, height - padding_size):
    #             for x in range(padding_size, width - padding_size):
    #                 pixels = []
    #                 for i in range(-padding_size, padding_size + 1):
    #                     for j in range(-padding_size, padding_size + 1):
    #                         pixel = img.pixel(x + i, y + j)
    #                         pixels.append(QColor(pixel).red())

    #                 if all(pixel == 255 for pixel in pixels):
    #                     eroded_image.setPixel(x, y, qRgb(255, 255, 255))
    #                 else:
    #                     eroded_image.setPixel(x, y, qRgb(0, 0, 0))

    #         # Tahap dilasi
    #         for y in range(padding_size, height - padding_size):
    #             for x in range(padding_size, width - padding_size):
    #                 pixels = []
    #                 for i in range(-padding_size, padding_size + 1):
    #                     for j in range(-padding_size, padding_size + 1):
    #                         pixel = eroded_image.pixel(x + i, y + j)
    #                         pixels.append(QColor(pixel).red())

    #                 if any(pixel == 255 for pixel in pixels):
    #                     dilated_image.setPixel(x, y, qRgb(255, 255, 255))
    #                 else:
    #                     dilated_image.setPixel(x, y, qRgb(0, 0, 0))

    #         # output gambar setelah dilasi
    #         self.pbOutput.setPixmap(QPixmap.fromImage(dilated_image))
    #         self.pbOutput.setScaledContents(True)
    #         self.stringefek1 = 'Effect : Opening-Square 9 '
    #         self.labelOutput.setText(self.stringefek1)
    #         self.showEffectComplete()
    #         self.progressBar.setProperty("value", 0)

    def applyOpeningSquare9(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            input_image = self.pixmap1.toImage()

            width, height = input_image.width(), input_image.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            structuring_element_size = 9

            padding_size = structuring_element_size // 2

            for y in range(padding_size, height - padding_size):
                for x in range(padding_size, width - padding_size):
                    pixels = []
                    for i in range(-padding_size, padding_size + 1):
                        for j in range(-padding_size, padding_size + 1):
                            pixel = input_image.pixel(x + i, y + j)
                            pixels.append(QColor(pixel).red())

                    if all(pixel == 255 for pixel in pixels):
                        output_image.setPixel(x, y, qRgb(255, 255, 255))
                    else:
                        output_image.setPixel(x, y, qRgb(0, 0, 0))
                        self.progressBar.setProperty("value", 100)

                    self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
                    self.pbOutput.setScaledContents(True)
                    self.stringefek1 = 'Effect : Opening-Square 9 '
                    self.labelOutput.setText(self.stringefek1)
                    self.showEffectComplete()
                    self.progressBar.setProperty("value", 0)


        # CLOSING - SQUARE 9X9
    def applyClosingSquare9(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            img = self.pixmap1.toImage()

            width, height = img.width(), img.height()

            output_image = QImage(width, height, QImage.Format_RGB32)

            structuring_element_size = 9

            padding_size = structuring_element_size // 2

            for y in range(padding_size, height - padding_size):
                for x in range(padding_size, width - padding_size):

                    pixels = []
                    for i in range(-padding_size, padding_size + 1):
                        for j in range(-padding_size, padding_size + 1):
                            pixel = img.pixel(x + i, y + j)
                            pixels.append(QColor(pixel).red())

                    if all(pixel == 0 for pixel in pixels):
                        output_image.setPixel(x, y, qRgb(0, 0, 0))

                    else:
                        output_image.setPixel(x, y, qRgb(255, 255, 255))
                        self.progressBar.setProperty("value", 100)

            # output gambar
            self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Closing-Square 9 '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)

        # ----------------------------------------------------------------------------------------------------------
        # FUNGSI MENU FEATURE EXTRACTION -----------------------------------------------------------------------------------------
        # COLOR RGB TO HSV

    def applyColorRGBtoHSV(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
            input_image = self.pixmap1.toImage()

            width = input_image.width()
            height = input_image.height()

            output_image = QImage(width, height, QImage.Format_RGB888)

            for y in range(height):
                for x in range(width):
                    pixel_color = input_image.pixelColor(x, y)
                    r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()
                    r, g, b = r / 255.0, g / 255.0, b / 255.0

                    cmax = max(r, g, b)
                    cmin = min(r, g, b)
                    delta = cmax - cmin

                    # menghitung hue (H)
                    if delta == 0:
                        h = 0
                    elif cmax == r:
                        h = 60 * (((g - b) / delta) % 6)
                    elif cmax == g:
                        h = 60 * (((b - r) / delta) + 2)
                    elif cmax == b:
                        h = 60 * (((r - g) / delta) + 4)

                    # menghitung saturation (S)
                    if cmax == 0:
                        s = 0
                    else:
                        s = delta / cmax

                    # menghitung value (V)
                    v = cmax

                    # Normalisasi hue dengan rentang [0, 360]
                    h = (h + 360) % 360

                    # Normalisasi saturation dan value dengan rentange [0, 255]
                    s = int(s * 255)
                    v = int(v * 255)

                    output_image.setPixel(x, y, QColor.fromHsv(int(h), int(s), int(v)).rgb())
                    self.progressBar.setProperty("value", 100)

            # output gambar
            self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Color RGB to HSV '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)


    def applyColorRGBtoHSL(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            input_image = self.pixmap1.toImage()

            # Dapatkan lebar dan tinggi gambar
            width = input_image.width()
            height = input_image.height()

            # Buat QImage untuk gambar HSL keluaran
            output_image = QImage(width, height, QImage.Format_RGB888)

            # Lakukan konversi RGB ke HSL dengan mengulangi piksel
            for y in range(height):
                for x in range(width):
                    pixel_color = input_image.pixelColor(x, y)
                    r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()
                    r, g, b = r / 255.0, g / 255.0, b / 255.0

                    cmax = max(r, g, b)
                    cmin = min(r, g, b)
                    delta = cmax - cmin

                    # Hitung hue (H)
                    if delta == 0:
                        h = 0
                    elif cmax == r:
                        h = 60 * (((g - b) / delta) % 6)
                    elif cmax == g:
                        h = 60 * (((b - r) / delta) + 2)
                    elif cmax == b:
                        h = 60 * (((r - g) / delta) + 4)

                    # Hitung lightness (L)
                    l = (cmax + cmin) / 2

                    # Hitung saturation (S)
                    if delta == 0:
                        s = 0
                    else:
                        s = delta / (1 - abs(2 * l - 1))

                    # Normalisasi hue untuk berada dalam rentang [0, 360]
                    h = (h + 360) % 360

                    # Normalisasi lightness dan saturation untuk berada dalam rentang [0, 255]
                    l = int(l * 255)
                    s = int(s * 255)

                    # Set warna piksel di gambar keluaran
                    output_image.setPixel(x, y, QColor.fromHsl(int(h), int(s), int(l)).rgb())
                    self.progressBar.setProperty("value", 100)

            # Tampilkan gambar keluaran
            self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Color RGB to HSL '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)



    def applyColorRGBtoYCrCb(self):
        # if self.pixmap1 is not None and not self.pixmap1.isNull():
        #     self.progressBar.setProperty("value", 0)
        #     # yellow_image = self.pixmap1.toImage()  # Konversi QPixmap ke QImage
        #     input_image = self.pixmap1.toImage()

        #     width = input_image.width()
        #     height = input_image.height()

        #     output_image = QImage(width, height, QImage.Format_RGB888)

        #     for y in range(height):
        #         for x in range(width):
        #             if x < width and y < height:  # mengecek koordinat
        #                 pixel_color = input_image.pixelColor(x, y)
        #                 r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()

        #                 # Normalisasi RGB dengan nilai [0, 1]
        #                 r /= 255.0
        #                 g /= 255.0
        #                 b /= 255.0

        #                 # menghitung Y, Cr, and Cb
        #                 y = int(0.299 * r + 0.587 * g + 0.114 * b)
        #                 cr = int(128 + 0.5 * r - 0.41869 * g - 0.08131 * b)
        #                 cb = int(128 - 0.16874 * r - 0.33126 * g + 0.5 * b)

        #                 y = min(max(y, 0), 255)
        #                 cr = min(max(cr, 0), 255)
        #                 cb = min(max(cb, 0), 255)

        #                 # Convert YCrCb back to RGB
        #                 r = int(y + 1.402 * (cr - 128))
        #                 g = int(y - 0.34414 * (cb - 128) - 0.71414 * (cr - 128))
        #                 b = int(y + 1.772 * (cb - 128))

        #                 r = min(max(r, 0), 255)
        #                 g = min(max(g, 0), 255)
        #                 b = min(max(b, 0), 255)

        #                 output_image.setPixelColor(x, y, QColor(r, g, b))
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            input_image = self.pixmap1.toImage()
            width = input_image.width()
            height = input_image.height()

            output_image = QImage(width, height, QImage.Format_RGB888)

            for y in range(height):
                for x in range(width):
                    color = QColor(input_image.pixel(x, y))
                    r, g, b = color.red(), color.green(), color.blue()

                    # Konversi RGB ke YCrCb
                    y_value = int(0.299 * r + 0.587 * g + 0.114 * b)
                    cr_value = int(128 + 0.5 * r - 0.418688 * g - 0.081312 * b)
                    cb_value = int(128 - 0.168736 * r - 0.331264 * g + 0.5 * b)

                    # Pastikan nilai-nilai berada dalam rentang 0-255
                    y_value = max(0, min(255, y_value))
                    cr_value = max(0, min(255, cr_value))
                    cb_value = max(0, min(255, cb_value))

                    output_image.setPixel(x, y, QColor(y_value, cr_value, cb_value).rgb())
                    self.progressBar.setProperty("value", 100)

            # output gambar
            self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Color RGB to YCrCB '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)



    def applyColorRGBtoCMYK(self):

        def rgb_to_cmyk(r, g, b):
            r, g, b = r / 255.0, g / 255.0, b / 255.0
            k = 1 - max(r, g, b)
            if k == 1:
                c, m, y = 0, 0, 0
            else:
                c = (1 - r - k) / (1 - k)
                m = (1 - g - k) / (1 - k)
                y = (1 - b - k) / (1 - k)
            return c, m, y, k

        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            input_image = self.pixmap1.toImage()

            width = input_image.width()
            height = input_image.height()

            output_image = QImage(width, height, QImage.Format_ARGB32)

            for y in range(height):
                for x in range(width):
                    pixel_color = input_image.pixelColor(x, y)
                    r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()
                    # cmyk_c, cmyk_m, cmyk_y, cmyk_k = rgb_to_cmyk(r, g, b)
                    c, m, y, k = rgb_to_cmyk(r, g, b)

                    # Normalisasi CMYK dengan nilai [0, 255]
                    c = min(255, max(0, int(c * 255)))
                    m = min(255, max(0, int(m * 255)))
                    y = min(255, max(0, int(y * 255)))
                    k = min(255, max(0, int(k * 255)))

                    color = QColor.fromCmyk(c, m, y, k)
                    output_image.setPixelColor(x, y, color)
                    self.progressBar.setProperty("value", 100)

            # output gambar
            self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Color RGB to CMYK '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)


# Diskontinuitas, pendekatannya dengan mempartisi citra berdasarkan pada
# perubahan intensitas yang menonjol, seperti deteksi titik, garis, dan tepi citra. 
# Cara yang paling umum digunakan untuk mencari diskontinyuitas adalah
# dengan menjalankan suatu filter (kernel) pada seluruh area citra.

    def applyImageSegmentation(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            input_image = self.pixmap1.toImage()

            width = input_image.width()
            height = input_image.height()

            segmented_image = QImage(width, height, QImage.Format_ARGB32)

            lower_color = QColor(100, 0, 0)  #warna bawah yaitu warna merah
            upper_color = QColor(255, 100, 100) #warna atas yaitu warna-orange

            for y in range(height):
                for x in range(width):
                    pixel_color = input_image.pixelColor(x, y)

                    r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()

                    if (lower_color.red() <= r <= upper_color.red() and
                        lower_color.green() <= g <= upper_color.green() and
                        lower_color.blue() <= b <= upper_color.blue()):
                        #set the pixel to white (255, 255, 255)
                        segmented_image.setPixel(x, y, qRgb(255, 255, 255))
                    else:
                        #set the pixel to black (0, 0, 0)
                        segmented_image.setPixel(x, y, qRgb(0, 0, 0))
                        self.progressBar.setProperty("value", 100)

            # output gambar
            self.pbOutput.setPixmap(QPixmap.fromImage(segmented_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Image Segmentation '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)

    # def applyImageSegmentation(self):
    #     if self.pixmap1 is not None and not self.pixmap1.isNull():
    #         self.progressBar.setProperty("value", 0)
    #         input_image = self.pixmap1.toImage()

    #         width = input_image.width()
    #         height = input_image.height()

    #         segmented_image = QImage(width, height, QImage.Format_ARGB32)

    #         lower_color = QColor(100, 0, 0)  
    #         upper_color = QColor(255, 100, 100) 

    #         visited = [[False for _ in range(width)] for _ in range(height)]

    #         def flood_fill(x, y):
    #             stack = [(x, y)]

    #             while stack:
    #                 x, y = stack.pop()

    #                 if x < 0 or x >= width or y < 0 or y >= height:
    #                     continue
    #                 if visited[y][x]:
    #                     continue

    #                 pixel_color = input_image.pixelColor(x, y)
    #                 r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()

    #                 if (lower_color.red() <= r <= upper_color.red() and
    #                     lower_color.green() <= g <= upper_color.green() and
    #                     lower_color.blue() <= b <= upper_color.blue()):
    #                     visited[y][x] = True
    #                     segmented_image.setPixel(x, y, qRgb(255, 255, 255))

    #                     # Push neighboring pixels onto the stack
    #                     stack.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])

    #         # Apply flood fill from each unvisited pixel
    #         for y in range(height):
    #             for x in range(width):
    #                 if not visited[y][x]:
    #                     flood_fill(x, y)

    #         # Output gambar
    #         self.pbOutput.setPixmap(QPixmap.fromImage(segmented_image))
    #         self.pbOutput.setScaledContents(True)
    #         self.stringefek1 = 'Effect : Image Segmentation '
    #         self.labelOutput.setText(self.stringefek1)
    #         self.showEffectComplete()
    #         self.progressBar.setProperty("value", 0)




    # def applyImageSegmentation(self):
    #     if self.pixmap1 is not None and not self.pixmap1.isNull():
    #         self.progressBar.setProperty("value", 0)
    #         input_image = self.pixmap1.toImage()

    #         width = input_image.width()
    #         height = input_image.height()

    #         segmented_image = QImage(width, height, QImage.Format_ARGB32)

    #         lower_color = QColor(100, 0, 0)
    #         upper_color = QColor(255, 100, 100)

    #         # Define kernel
    #         kernel = np.array([[1, 1, 1],
    #                         [1, 1, 1],
    #                         [1, 1, 1]])

    #         kernel_size = kernel.shape[0]
    #         padding_size = kernel_size // 2

    #         for y in range(padding_size, height - padding_size):
    #             for x in range(padding_size, width - padding_size):
    #                 # Initialize a sum for each channel (R, G, B)
    #                 sum_r, sum_g, sum_b = 0, 0, 0
    #                 for i in range(-padding_size, padding_size + 1):
    #                     for j in range(-padding_size, padding_size + 1):
    #                         pixel_color = input_image.pixelColor(x + i, y + j)
    #                         sum_r += pixel_color.red() * kernel[i + padding_size, j + padding_size]
    #                         sum_g += pixel_color.green() * kernel[i + padding_size, j + padding_size]
    #                         sum_b += pixel_color.blue() * kernel[i + padding_size, j + padding_size]

    #                 # Check if the sum is in the desired color range
    #                 if (lower_color.red() <= sum_r <= upper_color.red() and
    #                     lower_color.green() <= sum_g <= upper_color.green() and
    #                     lower_color.blue() <= sum_b <= upper_color.blue()):
    #                     # Set the pixel to white (255, 255, 255)
    #                     segmented_image.setPixel(x, y, qRgb(255, 255, 255))
    #                 else:
    #                     # Set the pixel to black (0, 0, 0)
    #                     segmented_image.setPixel(x, y, qRgb(0, 0, 0))

    #         # Output gambar
    #         self.pbOutput.setPixmap(QPixmap.fromImage(segmented_image))
    #         self.pbOutput.setScaledContents(True)
    #         self.stringefek1 = 'Effect : Image Segmentation '
    #         self.labelOutput.setText(self.stringefek1)
    #         self.showEffectComplete()
    #         self.progressBar.setProperty("value", 0)


    def removeBackground(self):
        if self.pixmap1 is not None and not self.pixmap1.isNull():
            self.progressBar.setProperty("value", 0)
            input_image = self.pixmap1.toImage()

            width = input_image.width()
            height = input_image.height()

            output_image = QImage(width, height, QImage.Format_ARGB32)
            output_image.fill(Qt.transparent)

            # background_color = QColor(255, 255, 255)  # White
            # background_color = QColor(139, 69, 19)
            background_color = QColor(0,0,0)
            # background_color1 = QColor(0, 255, 0)  # White
            # background_color2 = QColor(0, 0, 255)  # White

            color_threshold = 100

            for y in range(height):
                for x in range(width):
                    pixel_color = input_image.pixelColor(x, y)
        
                    color_diff = abs(pixel_color.red() - background_color.red()) + \
                                abs(pixel_color.green() - background_color.green()) + \
                                abs(pixel_color.blue() - background_color.blue())
                   
                    if color_diff >= color_threshold:
                        output_image.setPixelColor(x, y, pixel_color)
                        self.progressBar.setProperty("value", 100)

            # output gambar
            self.pbOutput.setPixmap(QPixmap.fromImage(output_image))
            self.pbOutput.setScaledContents(True)
            self.stringefek1 = 'Effect : Remove Background '
            self.labelOutput.setText(self.stringefek1)
            self.showEffectComplete()
            self.progressBar.setProperty("value", 0)


    # def removeBackground(self):
    #     pixmap = self.pixmap1.pixmap()
    #     if pixmap:
    #         image = pixmap.toImage()

    #         # Mengonversi pixmap menjadi QImage
    #         qimage = QtGui.QImage(image)

    #         # Mengambil data piksel QImage
    #         img_data = qimage.bits().asstring(qimage.byteCount())

    #         # Mengonversi data piksel menjadi format PNG
    #         img = image.frombytes("RGBA", (qimage.width(), qimage.height()), img_data, "raw", "BGRA")
    #         buffer = io.BytesIO()
    #         img.save(buffer, format="PNG")
    #         image_data = buffer.getvalue()

    #         # Menghapus latar belakang menggunakan rembg
    #         removed_bg_image = remove(image_data)

    #         # Convert the removed background image to QPixmap and display it
    #         removed_bg_pixmap = QtGui.QPixmap()
    #         removed_bg_pixmap.loadFromData(removed_bg_image)
    #         self.pbOutput.setPixmap(removed_bg_pixmap)
    #         self.pbOutput.setScaledContents(True)
    

    # def applyROI123(self):
    #     if self.pixmap1 is not None and not self.pixmap1.isNull():
    #         self.progressBar.setProperty("value", 0)
    #         image = self.pixmap1.toImage()
    #         print("Dimensi gambar:", image.width(), image.height())

    #         # Konversi ke format yang sesuai (CV_8UC3)
    #         image = image.convertToFormat(QtGui.QImage.Format_RGB888)

    #         # Dapatkan data gambar sebagai byte array
    #         buffer = QtCore.QBuffer()
    #         buffer.open(QtCore.QIODevice.ReadWrite)
    #         image.save(buffer, "PNG")  # Anda dapat mengganti format "PNG" sesuai kebutuhan
    #         data = buffer.data().data()

    #         # Reshape data menjadi array numpy dengan bentuk yang sesuai
    #         image_np = np.frombuffer(data, dtype=np.uint8).reshape(image.height(), image.width(), 3)

    #         # Memilih ROI dengan Qt
    #         # rect = cv2.selectROI(np.array(image), False)
    #         rect = cv2.selectROI("Pilih ROI", image_np, False)

    #         # Cropping gambar
    #         x, y, w, h = rect
    #         cropped_image = image.copy(x, y, w, h)  # Memperbaiki penggunaan image.copy
    #         self.progressBar.setProperty("value", 100)

    #         if self.pixmap2 is None:
    #             self.pixmap2 = QtGui.QPixmap.fromImage(cropped_image)

    #             # Menampilkan gambar di QLabel (misalnya, self.labelOutput)
    #             self.labelOutput.setPixmap(self.pixmap2)
    #             self.labelOutput.setScaledContents(True)
    #             self.stringefek1 = 'Effect : Luminance '
    #             self.labelOutput.setText(self.stringefek1)

    #             # Mengatur nilai progressBar
    #             self.progressBar.setProperty("value", 0)
    #             self.showEffectComplete()


    # def roi(self):
    #     roi_dialog = QtWidgets.QDialog()
    #     roi_dialog.setWindowTitle("Select Region of Interest")

    #     label = QLabel(roi_dialog)
    #     label.setText("Drag mouse to select ROI and release.")

    #     roi_label = QLabel(roi_dialog)
    #     roi_label.setGeometry(QtCore.QRect(10, 30, 471, 500))
    #     roi_label.setPixmap(self.pixmap1)

    #     self.selection_rect = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, roi_label) # Menambahkan kotak seleksi

    #     def mousePressEvent(event):
    #         self.start_roi = event.pos()
    #         self.selection_rect.setGeometry(QtCore.QRect(self.start_roi, QtCore.QSize()))
    #         self.selection_rect.show()

    #     def mouseMoveEvent(event):
    #         if self.selection_rect.isVisible():
    #             self.selection_rect.setGeometry(QtCore.QRect(self.start_roi, event.pos()).normalized())

    #     def mouseReleaseEvent(event):
    #         self.end_roi = event.pos()
    #         self.selection_rect.hide()
    #         self.process_roi()
    #         roi_dialog.accept()

    #     roi_label.mousePressEvent = mousePressEvent
    #     roi_label.mouseMoveEvent = mouseMoveEvent
    #     roi_label.mouseReleaseEvent = mouseReleaseEvent

    #     layout = QtWidgets.QVBoxLayout()
    #     layout.addWidget(label)
    #     layout.addWidget(roi_label)
    #     roi_dialog.setLayout(layout)

    #     roi_dialog.exec_()


    # def applyROI(self):
    #     if self.pixmap1 is not None and not self.pixmap1.isNull():
    #         self.progressBar.setProperty("value", 0)
    #         qImg = self.pixmap1.toImage()
    #         # Mengonversi QImage menjadi citra NumPy
    #         width, height = qImg.width(), qImg.height()
    #         ptr = qImg.constBits()
    #         ptr.setsize(qImg.byteCount())
    #         image_data = np.array(ptr).reshape(height, width, 4)  # 4 channel (RGBA)
    #         # Load gambar
    #         image = cv2.imread('1.jpg')


    #         # Konversi gambar ke grayscale
    #         gray = cv2.cvtColor(image_data, cv2.COLOR_RGBA2RGB)

    #         # Buat objek detektor wajah Haar Cascade
    #         face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    #         # Lakukan deteksi objek
    #         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    #         # Loop melalui objek yang terdeteksi dan tambahkan garis pen
    #         for (x, y, w, h) in faces:
    #             cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Tambahkan kotak hijau di sekitar objek

    #         rgbImage = cv2.cvtColor(gray, cv2.COLOR_RGBA2RGB)
    #         # Menampilkan gambar dengan objek yang terdeteksi
    #         height, width, channel = rgbImage.shape
    #         bytes_per_line = 3 * width
    #         q_image = QtGui.QImage(rgbImage.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888).rgbSwapped()
    #         pixmap = QtGui.QPixmap.fromImage(q_image)
    #         self.progressBar.setProperty("value", 100)

    #         # Tampilkan gambar pada QLabel
    #         self.pbOutput.setPixmap(pixmap)
    #         self.pbOutput.setScaledContents(True)
    #         self.stringefek1 = 'Effect : Remove Background '
    #         self.labelOutput.setText(self.stringefek1)
    #         self.showEffectComplete()
    #         self.progressBar.setProperty("value", 0)


    # def detect_color(self, pixmap1):
    #     # Inisialisasi variabel untuk menghitung jumlah piksel warna tertentu
    #     red_pixels = green_pixels = blue_pixels = 0

    #     width = pixmap1.width()
    #     height = pixmap1.height()

    #     for i in range(width):
    #         for j in range(height):
    #             color = pixmap1.pixelColor(i, j)

    #             # Mendapatkan komponen RGB
    #             red = color.red()
    #             green = color.green()
    #             blue = color.blue()

    #             # Menambahkan jumlah piksel berdasarkan warna tertentu
    #             red_pixels += red
    #             green_pixels += green
    #             blue_pixels += blue

    #     # Menghitung rata-rata warna
    #     total_pixels = width * height
    #     avg_red = red_pixels / total_pixels
    #     avg_green = green_pixels / total_pixels
    #     avg_blue = blue_pixels / total_pixels

    #     return avg_red, avg_green, avg_blue

    # def process_roi(self):
    #     if self.pixmap1 is not None:
    #         # ... (kode sebelumnya tetap sama)
    #         x1 = min(self.start_roi.x(), self.end_roi.x())
    #         y1 = min(self.start_roi.y(), self.end_roi.y())
    #         x2 = max(self.start_roi.x(), self.end_roi.x())
    #         y2 = max(self.start_roi.y(), self.end_roi.y())
    #         # Mendapatkan citra asli
    #         input_image = self.pixmap1.toImage()
    #         input_image = input_image.copy(x1, y1, x2 - x1, y2 - y1)

    #         #deteksi warna pada ROI
    #         avg_red, avg_green, avg_blue = self.detect_color(input_image)

    #         # Membuat gambar warna deteksi
    #         avg_red = int(avg_red)  # Mengonversi ke integer
    #         avg_green = int(avg_green)  # Mengonversi ke integer
    #         avg_blue = int(avg_blue)  # Mengonversi ke integer
    #         color_image = QtGui.QImage(input_image.size(), QtGui.QImage.Format_RGB32)
    #         color_image.fill(QtGui.qRgb(avg_red, avg_green, avg_blue))
    #         self.progressBar.setProperty("value", 100)

    #         # Mengonversi citra ke Pixmap dan menampilkannya di pbOutput
    #         self.pbOutput.setPixmap(QPixmap.fromImage(color_image))
    #         self.pbOutput.setScaledContents(True)
    #         self.stringefek1 = 'Effect : ROI '
    #         self.labelOutput.setText(self.stringefek1)
    #         self.showEffectComplete()
    #         self.progressBar.setProperty("value", 0)




    def showprogressBar(self, value):
        self.progressBar.setValue(value)
        self.timerEfek1.setInterval(1000)
        self.timerEfek1.timeout.connect(self.clearprogressbar)
        self.timerEfek1.start()

    def clearprogressbar(self):
        self.progressBar.clear()
        self.timerEfek1.stop()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    iconMain = QtGui.QIcon()
    iconMain.addPixmap(QtGui.QPixmap("Icon/5812.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    MainWindow.setWindowIcon(iconMain)
    sys.exit(app.exec_())
    