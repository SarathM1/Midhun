# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Monthly Statement.ui'
#
# Created: Sat Jul  5 10:23:52 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1024, 681)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.PushButtonNew = QtGui.QPushButton(self.centralwidget)
        self.PushButtonNew.setGeometry(QtCore.QRect(160, 840, 61, 27))
        self.PushButtonNew.setObjectName(_fromUtf8("PushButtonNew"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(770, 10, 241, 461))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEditTin = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditTin.setEnabled(False)
        self.lineEditTin.setText(_fromUtf8(""))
        self.lineEditTin.setObjectName(_fromUtf8("lineEditTin"))
        self.gridLayout_2.addWidget(self.lineEditTin, 3, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 5, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.doubleSpinBox5 = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox5.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.doubleSpinBox5.setMaximum(50000.0)
        self.doubleSpinBox5.setObjectName(_fromUtf8("doubleSpinBox5"))
        self.gridLayout_2.addWidget(self.doubleSpinBox5, 6, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)
        self.doubleSpinBoxVat145 = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBoxVat145.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.doubleSpinBoxVat145.setMaximum(50000.0)
        self.doubleSpinBoxVat145.setObjectName(_fromUtf8("doubleSpinBoxVat145"))
        self.gridLayout_2.addWidget(self.doubleSpinBoxVat145, 9, 1, 1, 1)
        self.doubleSpinBoxRoundOff = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBoxRoundOff.setEnabled(True)
        self.doubleSpinBoxRoundOff.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.doubleSpinBoxRoundOff.setMinimum(-0.99)
        self.doubleSpinBoxRoundOff.setMaximum(0.99)
        self.doubleSpinBoxRoundOff.setSingleStep(0.01)
        self.doubleSpinBoxRoundOff.setObjectName(_fromUtf8("doubleSpinBoxRoundOff"))
        self.gridLayout_2.addWidget(self.doubleSpinBoxRoundOff, 11, 1, 1, 1)
        self.lineEditItems = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditItems.setObjectName(_fromUtf8("lineEditItems"))
        self.gridLayout_2.addWidget(self.lineEditItems, 4, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 8, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_2.addWidget(self.label_16, 11, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 9, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_2.addWidget(self.label_15, 10, 0, 1, 1)
        self.doubleSpinBoxVat5 = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBoxVat5.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.doubleSpinBoxVat5.setMaximum(50000.0)
        self.doubleSpinBoxVat5.setObjectName(_fromUtf8("doubleSpinBoxVat5"))
        self.gridLayout_2.addWidget(self.doubleSpinBoxVat5, 7, 1, 1, 1)
        self.doubleSpinBoxLessScheme = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBoxLessScheme.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.doubleSpinBoxLessScheme.setMaximum(1000.0)
        self.doubleSpinBoxLessScheme.setObjectName(_fromUtf8("doubleSpinBoxLessScheme"))
        self.gridLayout_2.addWidget(self.doubleSpinBoxLessScheme, 10, 1, 1, 1)
        self.comboBoxParty = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.comboBoxParty.setInsertPolicy(QtGui.QComboBox.InsertAtBottom)
        self.comboBoxParty.setObjectName(_fromUtf8("comboBoxParty"))
        self.gridLayout_2.addWidget(self.comboBoxParty, 2, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 6, 0, 1, 1)
        self.lineEditBillNo = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditBillNo.setPlaceholderText(_fromUtf8(""))
        self.lineEditBillNo.setObjectName(_fromUtf8("lineEditBillNo"))
        self.gridLayout_2.addWidget(self.lineEditBillNo, 1, 1, 1, 1)
        self.doubleSpinBox145 = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox145.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.doubleSpinBox145.setMaximum(50000.0)
        self.doubleSpinBox145.setObjectName(_fromUtf8("doubleSpinBox145"))
        self.gridLayout_2.addWidget(self.doubleSpinBox145, 8, 1, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.gridLayout_2.addWidget(self.dateEdit, 0, 1, 1, 1)
        self.doubleSpinBoxExemted = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBoxExemted.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.doubleSpinBoxExemted.setMaximum(50000.0)
        self.doubleSpinBoxExemted.setObjectName(_fromUtf8("doubleSpinBoxExemted"))
        self.gridLayout_2.addWidget(self.doubleSpinBoxExemted, 5, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 7, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(60, 750, 98, 80))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_20 = QtGui.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_7.addWidget(self.label_20)
        self.label_21 = QtGui.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout_7.addWidget(self.label_21)
        self.label_22 = QtGui.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.verticalLayout_7.addWidget(self.label_22)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(1070, 740, 131, 80))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.labelTotalPurchase = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelTotalPurchase.setFont(font)
        self.labelTotalPurchase.setTextInteractionFlags(QtCore.Qt.TextEditable)
        self.labelTotalPurchase.setObjectName(_fromUtf8("labelTotalPurchase"))
        self.verticalLayout_6.addWidget(self.labelTotalPurchase)
        self.labelTotalVat = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelTotalVat.setFont(font)
        self.labelTotalVat.setObjectName(_fromUtf8("labelTotalVat"))
        self.verticalLayout_6.addWidget(self.labelTotalVat)
        self.labelNetTotal = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelNetTotal.setFont(font)
        self.labelNetTotal.setObjectName(_fromUtf8("labelNetTotal"))
        self.verticalLayout_6.addWidget(self.labelNetTotal)
        self.pushButtonSave = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSave.setGeometry(QtCore.QRect(940, 600, 61, 27))
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(7, 0, 251, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 741, 411))
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(16)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(15, item)
        self.PushButtonNewSave = QtGui.QPushButton(self.centralwidget)
        self.PushButtonNewSave.setGeometry(QtCore.QRect(600, 570, 85, 27))
        self.PushButtonNewSave.setObjectName(_fromUtf8("PushButtonNewSave"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 480, 69, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEditNewParty = QtGui.QLineEdit(self.centralwidget)
        self.lineEditNewParty.setGeometry(QtCore.QRect(520, 470, 171, 31))
        self.lineEditNewParty.setObjectName(_fromUtf8("lineEditNewParty"))
        self.lineEditNewTin = QtGui.QLineEdit(self.centralwidget)
        self.lineEditNewTin.setGeometry(QtCore.QRect(520, 522, 171, 31))
        self.lineEditNewTin.setObjectName(_fromUtf8("lineEditNewTin"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(460, 530, 41, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(750, 10, 20, 621))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(-70, 620, 1091, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 0, 1021, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.pushButtonEditDone = QtGui.QPushButton(self.centralwidget)
        self.pushButtonEditDone.setGeometry(QtCore.QRect(200, 570, 85, 27))
        self.pushButtonEditDone.setObjectName(_fromUtf8("pushButtonEditDone"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(380, 420, 20, 211))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(770, 480, 239, 116))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.doubleSpinBox_2.setFont(font)
        self.doubleSpinBox_2.setMaximum(50000.0)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.gridLayout.addWidget(self.doubleSpinBox_2, 2, 1, 1, 1)
        self.doubleSpinBoxTotalVat = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBoxTotalVat.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.doubleSpinBoxTotalVat.setFont(font)
        self.doubleSpinBoxTotalVat.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.doubleSpinBoxTotalVat.setMaximum(500000000.0)
        self.doubleSpinBoxTotalVat.setObjectName(_fromUtf8("doubleSpinBoxTotalVat"))
        self.gridLayout.addWidget(self.doubleSpinBoxTotalVat, 2, 1, 1, 1)
        self.label_23 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout.addWidget(self.label_23, 1, 0, 1, 1)
        self.doubleSpinBoxNetTotal = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBoxNetTotal.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.doubleSpinBoxNetTotal.setFont(font)
        self.doubleSpinBoxNetTotal.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.doubleSpinBoxNetTotal.setMaximum(500000000.0)
        self.doubleSpinBoxNetTotal.setObjectName(_fromUtf8("doubleSpinBoxNetTotal"))
        self.gridLayout.addWidget(self.doubleSpinBoxNetTotal, 3, 1, 1, 1)
        self.doubleSpinBoxTotal = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBoxTotal.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.doubleSpinBoxTotal.setFont(font)
        self.doubleSpinBoxTotal.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.doubleSpinBoxTotal.setMaximum(500000000.0)
        self.doubleSpinBoxTotal.setObjectName(_fromUtf8("doubleSpinBoxTotal"))
        self.gridLayout.addWidget(self.doubleSpinBoxTotal, 1, 1, 1, 1)
        self.label_25 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout.addWidget(self.label_25, 3, 0, 1, 1)
        self.label_24 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout.addWidget(self.label_24, 2, 0, 1, 1)
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(760, 470, 261, 16))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(170, 430, 58, 15))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(530, 430, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.comboBoxOptions = QtGui.QComboBox(self.centralwidget)
        self.comboBoxOptions.setEnabled(False)
        self.comboBoxOptions.setGeometry(QtCore.QRect(160, 520, 131, 31))
        self.comboBoxOptions.setObjectName(_fromUtf8("comboBoxOptions"))
        self.comboBoxOptions.addItem(_fromUtf8(""))
        self.comboBoxOptions.addItem(_fromUtf8(""))
        self.spinBoxSNo = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxSNo.setGeometry(QtCore.QRect(160, 470, 131, 31))
        self.spinBoxSNo.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBoxSNo.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.spinBoxSNo.setMinimum(1)
        self.spinBoxSNo.setMaximum(500)
        self.spinBoxSNo.setObjectName(_fromUtf8("spinBoxSNo"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(90, 530, 61, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(110, 480, 31, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionDeleteTableMonthlyStatement = QtGui.QAction(MainWindow)
        self.actionDeleteTableMonthlyStatement.setObjectName(_fromUtf8("actionDeleteTableMonthlyStatement"))
        self.actionExportToExcel = QtGui.QAction(MainWindow)
        self.actionExportToExcel.setObjectName(_fromUtf8("actionExportToExcel"))
        self.actionDeleteTableParty = QtGui.QAction(MainWindow)
        self.actionDeleteTableParty.setObjectName(_fromUtf8("actionDeleteTableParty"))
        self.menuFile.addAction(self.actionExportToExcel)
        self.menuFile.addSeparator()
        self.menuEdit.addAction(self.actionDeleteTableMonthlyStatement)
        self.menuEdit.addAction(self.actionDeleteTableParty)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dateEdit, self.lineEditBillNo)
        MainWindow.setTabOrder(self.lineEditBillNo, self.comboBoxParty)
        MainWindow.setTabOrder(self.comboBoxParty, self.lineEditTin)
        MainWindow.setTabOrder(self.lineEditTin, self.lineEditItems)
        MainWindow.setTabOrder(self.lineEditItems, self.doubleSpinBoxExemted)
        MainWindow.setTabOrder(self.doubleSpinBoxExemted, self.doubleSpinBox5)
        MainWindow.setTabOrder(self.doubleSpinBox5, self.doubleSpinBoxVat5)
        MainWindow.setTabOrder(self.doubleSpinBoxVat5, self.doubleSpinBox145)
        MainWindow.setTabOrder(self.doubleSpinBox145, self.doubleSpinBoxVat145)
        MainWindow.setTabOrder(self.doubleSpinBoxVat145, self.doubleSpinBoxLessScheme)
        MainWindow.setTabOrder(self.doubleSpinBoxLessScheme, self.doubleSpinBoxRoundOff)
        MainWindow.setTabOrder(self.doubleSpinBoxRoundOff, self.pushButtonSave)
        MainWindow.setTabOrder(self.pushButtonSave, self.lineEditNewParty)
        MainWindow.setTabOrder(self.lineEditNewParty, self.lineEditNewTin)
        MainWindow.setTabOrder(self.lineEditNewTin, self.PushButtonNewSave)
        MainWindow.setTabOrder(self.PushButtonNewSave, self.spinBoxSNo)
        MainWindow.setTabOrder(self.spinBoxSNo, self.comboBoxOptions)
        MainWindow.setTabOrder(self.comboBoxOptions, self.pushButtonEditDone)
        MainWindow.setTabOrder(self.pushButtonEditDone, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.PushButtonNew)
        MainWindow.setTabOrder(self.PushButtonNew, self.doubleSpinBox_2)
        MainWindow.setTabOrder(self.doubleSpinBox_2, self.doubleSpinBoxTotalVat)
        MainWindow.setTabOrder(self.doubleSpinBoxTotalVat, self.doubleSpinBoxNetTotal)
        MainWindow.setTabOrder(self.doubleSpinBoxNetTotal, self.doubleSpinBoxTotal)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Monthly Statement", None))
        self.PushButtonNew.setText(_translate("MainWindow", "New", None))
        self.lineEditTin.setStatusTip(_translate("MainWindow", "Automatically Updated. \"NA\" corresponds to \"New Party ?\"", None))
        self.label_10.setText(_translate("MainWindow", "Exemted", None))
        self.label_3.setText(_translate("MainWindow", "Bill Number", None))
        self.label_4.setText(_translate("MainWindow", "Date", None))
        self.label_9.setText(_translate("MainWindow", "Items", None))
        self.doubleSpinBoxRoundOff.setStatusTip(_translate("MainWindow", "Can take Negative values also. Values in the range -0.99 to 0.99", None))
        self.lineEditItems.setStatusTip(_translate("MainWindow", "Enter items seperated by comma", None))
        self.lineEditItems.setPlaceholderText(_translate("MainWindow", "Item1, Item2, . . .", None))
        self.label_13.setText(_translate("MainWindow", "14.50%", None))
        self.label_16.setText(_translate("MainWindow", "Round Off", None))
        self.label_14.setText(_translate("MainWindow", "VAT (14.50%)", None))
        self.label_15.setText(_translate("MainWindow", "Less Scheme ", None))
        self.comboBoxParty.setStatusTip(_translate("MainWindow", "Enter \"New Party\" if new party is to be added", None))
        self.label_11.setText(_translate("MainWindow", "5% ", None))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy", None))
        self.doubleSpinBoxExemted.setStatusTip(_translate("MainWindow", "Items for which tax is not applicable", None))
        self.label_12.setText(_translate("MainWindow", "VAT (5%) ", None))
        self.label_2.setText(_translate("MainWindow", "Tin No.", None))
        self.label.setText(_translate("MainWindow", "Name of Party ", None))
        self.label_20.setText(_translate("MainWindow", "Total Purchase  ", None))
        self.label_21.setText(_translate("MainWindow", "Total VAT           ", None))
        self.label_22.setText(_translate("MainWindow", "Net Total           ", None))
        self.labelTotalPurchase.setText(_translate("MainWindow", "Total Purchase", None))
        self.labelTotalVat.setText(_translate("MainWindow", "Total VAT", None))
        self.labelNetTotal.setText(_translate("MainWindow", "Net. Total", None))
        self.pushButtonSave.setStatusTip(_translate("MainWindow", "If \"Name Of Party\" is \"New Party\" the enter the new party and tin no . Else save the data to Database", None))
        self.pushButtonSave.setText(_translate("MainWindow", "SAVE", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "S.No", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Bill No", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Name Of Party", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tin No", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Items", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Exemted", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "5%", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Vat (5%)", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "14.50%", None))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Vat (14.50%)", None))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Less Scheme", None))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Round Off", None))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Total", None))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Total Vat", None))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Net Total", None))
        self.PushButtonNewSave.setStatusTip(_translate("MainWindow", "To save to Database and update the \"Name of Party \" ComboBox", None))
        self.PushButtonNewSave.setText(_translate("MainWindow", "SAVE", None))
        self.label_5.setText(_translate("MainWindow", "New Party ", None))
        self.lineEditNewParty.setStatusTip(_translate("MainWindow", "Enter name of the \"New Party\"", None))
        self.lineEditNewTin.setStatusTip(_translate("MainWindow", "Enter corresponding \"Tin No\"", None))
        self.label_6.setText(_translate("MainWindow", "Tin No      ", None))
        self.pushButtonEditDone.setText(_translate("MainWindow", "DONE", None))
        self.doubleSpinBoxTotalVat.setStatusTip(_translate("MainWindow", "Automatically Updated. \"Total Vat = Vat(5%)+Vat(14.50%)\"", None))
        self.label_23.setText(_translate("MainWindow", "Total Purchase", None))
        self.doubleSpinBoxNetTotal.setStatusTip(_translate("MainWindow", "Automatically Updated. \"Net Total=Total Purchase+Total Vat-Less Scheme+Round Off\"", None))
        self.doubleSpinBoxTotal.setStatusTip(_translate("MainWindow", "Automatically Updated. \"Total Purchase=Exemted+5%+14.50%\"", None))
        self.label_25.setText(_translate("MainWindow", "Net Total           ", None))
        self.label_24.setText(_translate("MainWindow", "Total VAT           ", None))
        self.label_7.setText(_translate("MainWindow", "EDITOR", None))
        self.label_17.setText(_translate("MainWindow", "ENTER NEW PARTY", None))
        self.comboBoxOptions.setStatusTip(_translate("MainWindow", "Select the action needed", None))
        self.comboBoxOptions.setItemText(0, _translate("MainWindow", "DELETE", None))
        self.comboBoxOptions.setItemText(1, _translate("MainWindow", "EDIT", None))
        self.spinBoxSNo.setStatusTip(_translate("MainWindow", "Select the row number", None))
        self.label_8.setText(_translate("MainWindow", "OPTIONS", None))
        self.label_18.setText(_translate("MainWindow", "S.No", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.actionDeleteTableMonthlyStatement.setText(_translate("MainWindow", "Delete Table MonthlyStatement", None))
        self.actionExportToExcel.setText(_translate("MainWindow", "Export Table", None))
        self.actionExportToExcel.setStatusTip(_translate("MainWindow", "Saves the database in CSV format which can be read from Excel or programs like Excel", None))
        self.actionExportToExcel.setShortcut(_translate("MainWindow", "Ctrl+E", None))
        self.actionDeleteTableParty.setText(_translate("MainWindow", "Delete Table Party", None))
