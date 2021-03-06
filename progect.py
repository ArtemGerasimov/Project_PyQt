from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.criteria = QtWidgets.QComboBox(self.centralwidget)
        self.criteria.setGeometry(QtCore.QRect(0, 0, 161, 31))
        self.criteria.setObjectName("criteria")
        self.criteria_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.criteria_2.setGeometry(QtCore.QRect(160, 0, 311, 31))
        self.criteria_2.setObjectName("criteria_2")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(470, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.search.setFont(font)
        self.search.setObjectName("search")
        self.code_1 = QtWidgets.QLabel(self.centralwidget)
        self.code_1.setGeometry(QtCore.QRect(0, 90, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.code_1.setFont(font)
        self.code_1.setObjectName("code_1")
        self.code_2 = QtWidgets.QLabel(self.centralwidget)
        self.code_2.setGeometry(QtCore.QRect(150, 90, 401, 31))
        self.code_2.setText("")
        self.code_2.setObjectName("code_2")
        self.name_1 = QtWidgets.QLabel(self.centralwidget)
        self.name_1.setGeometry(QtCore.QRect(0, 60, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_1.setFont(font)
        self.name_1.setObjectName("name_1")
        self.name_2 = QtWidgets.QLabel(self.centralwidget)
        self.name_2.setGeometry(QtCore.QRect(150, 60, 401, 31))
        self.name_2.setText("")
        self.name_2.setObjectName("name_2")
        self.metod_1 = QtWidgets.QLabel(self.centralwidget)
        self.metod_1.setGeometry(QtCore.QRect(0, 120, 151, 31))
        self.metod_1.setObjectName("metod_1")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 250, 296, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.event = QtWidgets.QLineEdit(self.centralwidget)
        self.event.setGeometry(QtCore.QRect(0, 430, 291, 21))
        self.event.setObjectName("event")
        self.event_record = QtWidgets.QPushButton(self.centralwidget)
        self.event_record.setGeometry(QtCore.QRect(0, 450, 291, 21))
        self.event_record.setObjectName("event_record")
        self.statistic = QtWidgets.QPushButton(self.centralwidget)
        self.statistic.setGeometry(QtCore.QRect(360, 310, 141, 31))
        self.statistic.setObjectName("statistic")
        self.meaning = QtWidgets.QLineEdit(self.centralwidget)
        self.meaning.setGeometry(QtCore.QRect(0, 520, 221, 21))
        self.meaning.setObjectName("meaning")
        self.quantity = QtWidgets.QSpinBox(self.centralwidget)
        self.quantity.setGeometry(QtCore.QRect(220, 520, 51, 22))
        self.quantity.setObjectName("quantity")
        self.record = QtWidgets.QPushButton(self.centralwidget)
        self.record.setGeometry(QtCore.QRect(270, 520, 75, 23))
        self.record.setObjectName("record")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(160, 30, 231, 31))
        self.error.setText("")
        self.error.setObjectName("error")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(388, 30, 191, 31))
        self.comboBox.setObjectName("comboBox")
        self.help_2 = QtWidgets.QPushButton(self.centralwidget)
        self.help_2.setGeometry(QtCore.QRect(360, 340, 141, 31))
        self.help_2.setObjectName("help_2")
        self.metod_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.metod_2.setGeometry(QtCore.QRect(145, 121, 411, 131))
        self.metod_2.setObjectName("metod_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-200, 290, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 500, 311, 21))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search.setText(_translate("MainWindow", "??????????"))
        self.code_1.setText(_translate("MainWindow", "?????? ????????????????????"))
        self.name_1.setText(_translate("MainWindow", "???????????????? ??????????????????"))
        self.metod_1.setText(_translate("MainWindow", "???????????? ????????????????????"))
        self.event_record.setText(_translate("MainWindow", "???????????????? ??????????????"))
        self.statistic.setText(_translate("MainWindow", "????????????????????"))
        self.record.setText(_translate("MainWindow", "????????????????"))
        self.help_2.setText(_translate("MainWindow", "????????????"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "?????????? ???? ???????????? ?????????? ???????????????????? ?????????????? ??????????."))
