# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'circuit_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,Qt,
    QSize, QTime, QUrl, Qt,QAbstractTableModel)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

from Models.Models_for_applications_functionnality.transverse_models import Four_element_from_Circuit_Table
class Model_For_TableView(QAbstractTableModel):
    def __init__(self,parent,header:list[str],list:list,*args):
        super().__init__(parent,*args)
        self.header = header
        self.list = list


    def rowCount(self,parent):
        return len(self.list)
    
    def columnCount(self,parent):
        return len(self.header)
    

    def data(self, index,role):
        if not index.isValid():
            return None
        elif role != Qt.ItemDataRole.DisplayRole:
            return None

        return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self.header[col]



class Ui_MainWindow(object):
        
    def setupUi(self, MainWindow,header:list[str],data:list[Four_element_from_Circuit_Table]):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1089, 655)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(200, 30))
        palette = QPalette()
        brush = QBrush(QColor(192, 191, 188, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 0))
        self.widget.setMaximumSize(QSize(200, 16777215))
        palette1 = QPalette()
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        brush3 = QBrush(QColor(252, 252, 251, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        brush4 = QBrush(QColor(125, 125, 124, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        brush5 = QBrush(QColor(167, 166, 165, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush6)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 127))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush7)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush2)
#endif
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush6)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush7)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush2)
#endif
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush1)
        brush8 = QBrush(QColor(250, 249, 248, 255))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush8)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush6)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush1)
        brush9 = QBrush(QColor(125, 125, 124, 127))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush2)
#endif
        self.widget.setPalette(palette1)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        self.pushButton.setPalette(palette2)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        self.pushButton_2.setPalette(palette3)

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        palette4 = QPalette()
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        self.pushButton_3.setPalette(palette4)

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(28, 113, 216);")

        self.verticalLayout.addWidget(self.label)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.total_number_of_tour = QLabel(self.centralwidget)
        self.total_number_of_tour.setObjectName(u"total_number_of_tour")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.total_number_of_tour.setFont(font1)

        self.horizontalLayout_2.addWidget(self.total_number_of_tour)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.add_new_tour = QPushButton(self.centralwidget)
        self.add_new_tour.setObjectName(u"add_new_tour")
        self.add_new_tour.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.horizontalLayout_2.addWidget(self.add_new_tour)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gestion de circuit", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Circuits", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Les Circuits", None))
        self.total_number_of_tour.setText(QCoreApplication.translate("MainWindow", u"Total: 0", None))
        self.add_new_tour.setText(QCoreApplication.translate("MainWindow", u"Ajouter un nouveau circuit", None))
    # retranslateUi

