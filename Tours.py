# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tours.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_Madagascar_Tours(object):
    def setupUi(self, Madagascar_Tours):
        if not Madagascar_Tours.objectName():
            Madagascar_Tours.setObjectName(u"Madagascar_Tours")
        Madagascar_Tours.resize(983, 588)
        Madagascar_Tours.setStyleSheet(u"background-color: rgb(154, 153, 150);")
        self.horizontalLayout = QHBoxLayout(Madagascar_Tours)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Madagascar_Tours)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(28, 113, 216);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label)

        self.tableView = QTableView(Madagascar_Tours)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.total_number_of_tour = QLabel(Madagascar_Tours)
        self.total_number_of_tour.setObjectName(u"total_number_of_tour")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.total_number_of_tour.setFont(font1)
        self.total_number_of_tour.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.total_number_of_tour)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.add_new_tour = QPushButton(Madagascar_Tours)
        self.add_new_tour.setObjectName(u"add_new_tour")
        self.add_new_tour.setStyleSheet(u"background-color: rgb(38, 162, 105);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.add_new_tour)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.widget = QWidget(Madagascar_Tours)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 0))
        self.widget.setMaximumSize(QSize(200, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(154, 153, 150, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        brush3 = QBrush(QColor(252, 252, 251, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        brush4 = QBrush(QColor(125, 125, 124, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        brush5 = QBrush(QColor(167, 166, 165, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush2)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush6)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 127))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush7)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush2)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush6)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush7)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush2)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush2)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        brush8 = QBrush(QColor(250, 249, 248, 255))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush8)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush6)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
        brush9 = QBrush(QColor(125, 125, 124, 127))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush2)
#endif
        self.widget.setPalette(palette)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        palette1 = QPalette()
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        brush10 = QBrush(QColor(255, 255, 255, 128))
        brush10.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        self.pushButton.setPalette(palette1)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        self.pushButton_2.setPalette(palette2)
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush2)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        self.pushButton_3.setPalette(palette3)
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Madagascar_Tours)

        QMetaObject.connectSlotsByName(Madagascar_Tours)
    # setupUi

    def retranslateUi(self, Madagascar_Tours):
        Madagascar_Tours.setWindowTitle(QCoreApplication.translate("Madagascar_Tours", u"Madagascar_Tours", None))
        self.label.setText(QCoreApplication.translate("Madagascar_Tours", u"Les Circuits", None))
        self.total_number_of_tour.setText(QCoreApplication.translate("Madagascar_Tours", u"Total: 0", None))
        self.add_new_tour.setText(QCoreApplication.translate("Madagascar_Tours", u"Ajouter un nouveau circuit", None))
        self.pushButton.setText(QCoreApplication.translate("Madagascar_Tours", u"Circuits", None))
        self.pushButton_2.setText(QCoreApplication.translate("Madagascar_Tours", u"Contact", None))
        self.pushButton_3.setText(QCoreApplication.translate("Madagascar_Tours", u"Configuration", None))
    # retranslateUi

