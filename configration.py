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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Madagascar_Tours(object):
    def setupUi(self, Madagascar_Tours):
        if not Madagascar_Tours.objectName():
            Madagascar_Tours.setObjectName(u"Madagascar_Tours")
        Madagascar_Tours.resize(582, 246)
        palette = QPalette()
        brush = QBrush(QColor(154, 153, 150, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        Madagascar_Tours.setPalette(palette)
        self.centralwidget = QWidget(Madagascar_Tours)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.submit_and_close_btn = QPushButton(self.centralwidget)
        self.submit_and_close_btn.setObjectName(u"submit_and_close_btn")
        self.submit_and_close_btn.setMinimumSize(QSize(150, 0))
        self.submit_and_close_btn.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.verticalLayout.addWidget(self.submit_and_close_btn)

        self.cancel_and_close_btn = QPushButton(self.centralwidget)
        self.cancel_and_close_btn.setObjectName(u"cancel_and_close_btn")
        self.cancel_and_close_btn.setMinimumSize(QSize(150, 0))
        self.cancel_and_close_btn.setStyleSheet(u"background-color: rgb(224, 27, 36);")

        self.verticalLayout.addWidget(self.cancel_and_close_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_for_server_host = QLabel(self.centralwidget)
        self.label_for_server_host.setObjectName(u"label_for_server_host")
        self.label_for_server_host.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_for_server_host)

        self.Nom_de_la_base_de_donnees_label = QLabel(self.centralwidget)
        self.Nom_de_la_base_de_donnees_label.setObjectName(u"Nom_de_la_base_de_donnees_label")
        self.Nom_de_la_base_de_donnees_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.Nom_de_la_base_de_donnees_label)

        self.nom_d_utilisateur_label = QLabel(self.centralwidget)
        self.nom_d_utilisateur_label.setObjectName(u"nom_d_utilisateur_label")
        self.nom_d_utilisateur_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.nom_d_utilisateur_label)

        self.nom_d_utilisateur_input = QLineEdit(self.centralwidget)
        self.nom_d_utilisateur_input.setObjectName(u"nom_d_utilisateur_input")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.nom_d_utilisateur_input)

        self.password_label = QLabel(self.centralwidget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.password_label)

        self.password_input = QLineEdit(self.centralwidget)
        self.password_input.setObjectName(u"password_input")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.password_input)

        self.port_label = QLabel(self.centralwidget)
        self.port_label.setObjectName(u"port_label")
        self.port_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.port_label)

        self.port_number_input = QLineEdit(self.centralwidget)
        self.port_number_input.setObjectName(u"port_number_input")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.port_number_input)

        self.Nom_de_la_base_de_donnees_input = QLineEdit(self.centralwidget)
        self.Nom_de_la_base_de_donnees_input.setObjectName(u"Nom_de_la_base_de_donnees_input")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.Nom_de_la_base_de_donnees_input)

        self.hosting_database_input = QLineEdit(self.centralwidget)
        self.hosting_database_input.setObjectName(u"hosting_database_input")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.hosting_database_input)


        self.verticalLayout_2.addLayout(self.formLayout)

        Madagascar_Tours.setCentralWidget(self.centralwidget)

        self.retranslateUi(Madagascar_Tours)

        QMetaObject.connectSlotsByName(Madagascar_Tours)
    # setupUi

    def retranslateUi(self, Madagascar_Tours):
        Madagascar_Tours.setWindowTitle(QCoreApplication.translate("Madagascar_Tours", u"Madagascar-Tours", None))
        self.submit_and_close_btn.setText(QCoreApplication.translate("Madagascar_Tours", u"Valider", None))
        self.cancel_and_close_btn.setText(QCoreApplication.translate("Madagascar_Tours", u"Annuler", None))
        self.label_for_server_host.setText(QCoreApplication.translate("Madagascar_Tours", u"Serveur de la base de donn\u00e9es", None))
        self.Nom_de_la_base_de_donnees_label.setText(QCoreApplication.translate("Madagascar_Tours", u"Nom de la base de donn\u00e9es", None))
        self.nom_d_utilisateur_label.setText(QCoreApplication.translate("Madagascar_Tours", u"Nom de l'utilisateur", None))
        self.nom_d_utilisateur_input.setPlaceholderText(QCoreApplication.translate("Madagascar_Tours", u"root", None))
        self.password_label.setText(QCoreApplication.translate("Madagascar_Tours", u"Mot de passe", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("Madagascar_Tours", u"Caponmada2025?", None))
        self.port_label.setText(QCoreApplication.translate("Madagascar_Tours", u"Num\u00e9ro de port", None))
        self.port_number_input.setPlaceholderText(QCoreApplication.translate("Madagascar_Tours", u"3306", None))
        self.Nom_de_la_base_de_donnees_input.setText("")
        self.Nom_de_la_base_de_donnees_input.setPlaceholderText(QCoreApplication.translate("Madagascar_Tours", u"caponmad_caponmada", None))
        self.hosting_database_input.setPlaceholderText(QCoreApplication.translate("Madagascar_Tours", u"caponmada.mg / 192.168.1.1", None))
    # retranslateUi