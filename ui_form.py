# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(560, 20, 251, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.text_len_3 = QtWidgets.QLabel(self.layoutWidget)
        self.text_len_3.setObjectName("text_len_3")
        self.verticalLayout_5.addWidget(self.text_len_3)
        self.add_picture = QtWidgets.QPushButton(self.layoutWidget)
        self.add_picture.setObjectName("add_picture")
        self.verticalLayout_5.addWidget(self.add_picture)
        self.text_len_c_3 = QtWidgets.QLabel(self.layoutWidget)
        self.text_len_c_3.setObjectName("text_len_c_3")
        self.verticalLayout_5.addWidget(self.text_len_c_3)
        self.len_char_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.len_char_3.setObjectName("len_char_3")
        self.verticalLayout_5.addWidget(self.len_char_3)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 20, 521, 321))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.start_button_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.start_button_3.setObjectName("start_button_3")
        self.horizontalLayout_5.addWidget(self.start_button_3)
        self.clear_button_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.clear_button_3.setObjectName("clear_button_3")
        self.horizontalLayout_5.addWidget(self.clear_button_3)
        spacerItem = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.text_count_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.text_count_3.setText("")
        self.text_count_3.setObjectName("text_count_3")
        self.horizontalLayout_6.addWidget(self.text_count_3)
        self.text_rating_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.text_rating_3.setText("")
        self.text_rating_3.setObjectName("text_rating_3")
        self.horizontalLayout_6.addWidget(self.text_rating_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.generations_field_3 = QtWidgets.QTextBrowser(self.layoutWidget_2)
        self.generations_field_3.setObjectName("generations_field_3")
        self.verticalLayout_6.addWidget(self.generations_field_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 220, 93, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.text_len_c_4 = QtWidgets.QLabel(self.centralwidget)
        self.text_len_c_4.setGeometry(QtCore.QRect(580, 180, 191, 24))
        self.text_len_c_4.setObjectName("text_len_c_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 841, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text_len_3.setText(_translate("MainWindow", "Загрузите картинку"))
        self.add_picture.setText(_translate("MainWindow", "Загрузить картинку"))
        self.text_len_c_3.setText(_translate("MainWindow", "Введите размер шаблона"))
        self.start_button_3.setText(_translate("MainWindow", "▶"))
        self.clear_button_3.setText(_translate("MainWindow", "Очистить всё"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.text_len_c_4.setText(_translate("MainWindow", "Скачать полученную картинку"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "О программе"))
        self.action.setText(_translate("MainWindow", "Сохранить"))
        self.action_3.setText(_translate("MainWindow", "Загрузить"))