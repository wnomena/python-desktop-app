# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuration.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setMinimumSize(QSize(500, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_for_server_host = QLabel(self.centralwidget)
        self.label_for_server_host.setObjectName(u"label_for_server_host")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_for_server_host)

        self.input_for_server_host = QLineEdit(self.centralwidget)
        self.input_for_server_host.setObjectName(u"input_for_server_host")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input_for_server_host)

        self.Nom_de_la_base_de_donnees_label = QLabel(self.centralwidget)
        self.Nom_de_la_base_de_donnees_label.setObjectName(u"Nom_de_la_base_de_donnees_label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.Nom_de_la_base_de_donnees_label)

        self.Nom_de_la_base_de_donnees_input = QLineEdit(self.centralwidget)
        self.Nom_de_la_base_de_donnees_input.setObjectName(u"Nom_de_la_base_de_donnees_input")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.Nom_de_la_base_de_donnees_input)

        self.nom_d_utilisateur_label = QLabel(self.centralwidget)
        self.nom_d_utilisateur_label.setObjectName(u"nom_d_utilisateur_label")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.nom_d_utilisateur_label)

        self.nom_d_utilisateur_input = QLineEdit(self.centralwidget)
        self.nom_d_utilisateur_input.setObjectName(u"nom_d_utilisateur_input")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.nom_d_utilisateur_input)

        self.password_label = QLabel(self.centralwidget)
        self.password_label.setObjectName(u"password_label")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.password_label)

        self.password_input = QLineEdit(self.centralwidget)
        self.password_input.setObjectName(u"password_input")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.password_input)

        self.port_label = QLabel(self.centralwidget)
        self.port_label.setObjectName(u"port_label")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.port_label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.Valider = QPushButton(self.centralwidget)
        self.Valider.setObjectName(u"Valider")
        self.Valider.setStyleSheet(u"background-color: rgb(51, 209, 122);")

        self.verticalLayout.addWidget(self.Valider)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(224, 27, 36);")

        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.label_for_server_host.setText(QCoreApplication.translate("MainWindow", u"Serveur de la base de donn\u00e9es", None))
        self.input_for_server_host.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom de domaine ou adresse IP", None))
        self.Nom_de_la_base_de_donnees_label.setText(QCoreApplication.translate("MainWindow", u"Nom de la base de donn\u00e9es", None))
        self.Nom_de_la_base_de_donnees_input.setText("")
        self.Nom_de_la_base_de_donnees_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"caponmad_caponmada", None))
        self.nom_d_utilisateur_label.setText(QCoreApplication.translate("MainWindow", u"Nom de l'utilisateur", None))
        self.nom_d_utilisateur_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"root", None))
        self.password_label.setText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Caponmada2025?", None))
        self.port_label.setText(QCoreApplication.translate("MainWindow", u"Num\u00e9ro de port", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"3306", None))
        self.Valider.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
    # retranslateUi

