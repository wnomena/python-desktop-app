# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 490)
        MainWindow.setMinimumSize(QSize(900, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.circuits_ui = QWidget()
        self.circuits_ui.setObjectName(u"circuits_ui")
        self.verticalLayout_2 = QVBoxLayout(self.circuits_ui)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.circuits_ui)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(53, 132, 228);")

        self.verticalLayout_2.addWidget(self.label)

        self.tableView = QTableView(self.circuits_ui)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_2.addWidget(self.tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.circuits_ui)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(46, 194, 126);")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.circuits_ui)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(28, 113, 216);")

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.tableView_2 = QTableView(self.page)
        self.tableView_2.setObjectName(u"tableView_2")

        self.verticalLayout_4.addWidget(self.tableView_2)

        self.stackedWidget.addWidget(self.page)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 0))
        self.widget.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tours_btn = QPushButton(self.widget)
        self.tours_btn.setObjectName(u"tours_btn")

        self.verticalLayout.addWidget(self.tours_btn)

        self.contact_btn = QPushButton(self.widget)
        self.contact_btn.setObjectName(u"contact_btn")

        self.verticalLayout.addWidget(self.contact_btn)

        self.config_btn = QPushButton(self.widget)
        self.config_btn.setObjectName(u"config_btn")

        self.verticalLayout.addWidget(self.config_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Madagascar-Tours", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Circuits", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ajouter de nouveau circuit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Contacts", None))
        self.tours_btn.setText(QCoreApplication.translate("MainWindow", u"Circuits", None))
        self.contact_btn.setText(QCoreApplication.translate("MainWindow", u"Contacts", None))
        self.config_btn.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
    # retranslateUi

