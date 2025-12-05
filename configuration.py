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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Configuration(object):

    
    def setupUi(self, Configuration):
        if not Configuration.objectName():
            Configuration.setObjectName(u"Configuration")
        Configuration.resize(616, 244)
        Configuration.setStyleSheet(u"background-color: rgb(154, 153, 150);")
        self.verticalLayout = QVBoxLayout(Configuration)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_for_server_host = QLabel(Configuration)
        self.label_for_server_host.setObjectName(u"label_for_server_host")
        self.label_for_server_host.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_for_server_host)

        self.input_for_server_host = QLineEdit(Configuration)
        self.input_for_server_host.setObjectName(u"input_for_server_host")
        self.input_for_server_host.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input_for_server_host)

        self.Nom_de_la_base_de_donnees_label = QLabel(Configuration)
        self.Nom_de_la_base_de_donnees_label.setObjectName(u"Nom_de_la_base_de_donnees_label")
        self.Nom_de_la_base_de_donnees_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.Nom_de_la_base_de_donnees_label)

        self.Nom_de_la_base_de_donnees_input = QLineEdit(Configuration)
        self.Nom_de_la_base_de_donnees_input.setObjectName(u"Nom_de_la_base_de_donnees_input")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.Nom_de_la_base_de_donnees_input)

        self.nom_d_utilisateur_label = QLabel(Configuration)
        self.nom_d_utilisateur_label.setObjectName(u"nom_d_utilisateur_label")
        self.nom_d_utilisateur_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.nom_d_utilisateur_label)

        self.nom_d_utilisateur_input = QLineEdit(Configuration)
        self.nom_d_utilisateur_input.setObjectName(u"nom_d_utilisateur_input")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.nom_d_utilisateur_input)

        self.password_label = QLabel(Configuration)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.password_label)

        self.password_input = QLineEdit(Configuration)
        self.password_input.setObjectName(u"password_input")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.password_input)

        self.port_label = QLabel(Configuration)
        self.port_label.setObjectName(u"port_label")
        self.port_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.port_label)

        self.lineEdit = QLineEdit(Configuration)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.Valider = QPushButton(Configuration)
        self.Valider.setObjectName(u"Valider")
        self.Valider.setStyleSheet(u"background-color: rgb(51, 209, 122);color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.Valider)

        self.pushButton = QPushButton(Configuration)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(224, 27, 36);color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Configuration)

        QMetaObject.connectSlotsByName(Configuration)
    # setupUi

    def retranslateUi(self, Configuration):
        Configuration.setWindowTitle(QCoreApplication.translate("Configuration", u"Configuration", None))
        self.label_for_server_host.setText(QCoreApplication.translate("Configuration", u"Serveur de la base de donn\u00e9es", None))
        self.input_for_server_host.setPlaceholderText(QCoreApplication.translate("Configuration", u"Nom de domaine ou adresse IP", None))
        self.Nom_de_la_base_de_donnees_label.setText(QCoreApplication.translate("Configuration", u"Nom de la base de donn\u00e9es", None))
        self.Nom_de_la_base_de_donnees_input.setText("")
        self.Nom_de_la_base_de_donnees_input.setPlaceholderText(QCoreApplication.translate("Configuration", u"caponmad_caponmada", None))
        self.nom_d_utilisateur_label.setText(QCoreApplication.translate("Configuration", u"Nom de l'utilisateur", None))
        self.nom_d_utilisateur_input.setPlaceholderText(QCoreApplication.translate("Configuration", u"root", None))
        self.password_label.setText(QCoreApplication.translate("Configuration", u"Mot de passe", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("Configuration", u"Caponmada2025?", None))
        self.port_label.setText(QCoreApplication.translate("Configuration", u"Num\u00e9ro de port", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Configuration", u"3306", None))
        self.Valider.setText(QCoreApplication.translate("Configuration", u"Valider", None))
        self.pushButton.setText(QCoreApplication.translate("Configuration", u"Annuler", None))
    # retranslateUi

