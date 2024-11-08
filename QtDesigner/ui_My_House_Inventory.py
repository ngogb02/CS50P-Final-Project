# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'My_House_Inventory.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateTimeEdit, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QTableView, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_My_House_Inventory(object):
    def setupUi(self, My_House_Inventory):
        if not My_House_Inventory.objectName():
            My_House_Inventory.setObjectName(u"My_House_Inventory")
        My_House_Inventory.setEnabled(True)
        My_House_Inventory.resize(733, 391)
        icon = QIcon()
        icon.addFile(u":/newPrefix/images/building.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        My_House_Inventory.setWindowIcon(icon)
        My_House_Inventory.setAutoFillBackground(False)
        self.layoutWidget = QWidget(My_House_Inventory)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 233, 88))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Add_Item_Button = QPushButton(self.layoutWidget)
        self.Add_Item_Button.setObjectName(u"Add_Item_Button")

        self.verticalLayout_2.addWidget(self.Add_Item_Button)

        self.Remove_Item_Button = QPushButton(self.layoutWidget)
        self.Remove_Item_Button.setObjectName(u"Remove_Item_Button")

        self.verticalLayout_2.addWidget(self.Remove_Item_Button)

        self.Create_An_Item_Button = QPushButton(self.layoutWidget)
        self.Create_An_Item_Button.setObjectName(u"Create_An_Item_Button")

        self.verticalLayout_2.addWidget(self.Create_An_Item_Button)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Add_Item_Line_Edit = QLineEdit(self.layoutWidget)
        self.Add_Item_Line_Edit.setObjectName(u"Add_Item_Line_Edit")
        self.Add_Item_Line_Edit.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)

        self.verticalLayout.addWidget(self.Add_Item_Line_Edit)

        self.Remove_Item_Line_Edit = QLineEdit(self.layoutWidget)
        self.Remove_Item_Line_Edit.setObjectName(u"Remove_Item_Line_Edit")

        self.verticalLayout.addWidget(self.Remove_Item_Line_Edit)

        self.Create_Item_Line_Edit = QLineEdit(self.layoutWidget)
        self.Create_Item_Line_Edit.setObjectName(u"Create_Item_Line_Edit")

        self.verticalLayout.addWidget(self.Create_Item_Line_Edit)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.layoutWidget1 = QWidget(My_House_Inventory)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(380, 360, 362, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Date_Time_Title = QLabel(self.layoutWidget1)
        self.Date_Time_Title.setObjectName(u"Date_Time_Title")

        self.horizontalLayout_2.addWidget(self.Date_Time_Title)

        self.Date_Time_Title_Text = QLabel(self.layoutWidget1)
        self.Date_Time_Title_Text.setObjectName(u"Date_Time_Title_Text")

        self.horizontalLayout_2.addWidget(self.Date_Time_Title_Text)

        self.dateTimeEdit = QDateTimeEdit(self.layoutWidget1)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setEnabled(True)
        self.dateTimeEdit.setAcceptDrops(False)
        self.dateTimeEdit.setFrame(True)
        self.dateTimeEdit.setReadOnly(True)
        self.dateTimeEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dateTimeEdit.setProperty(u"showGroupSeparator", False)

        self.horizontalLayout_2.addWidget(self.dateTimeEdit)

        self.MushroomHouse = QLabel(My_House_Inventory)
        self.MushroomHouse.setObjectName(u"MushroomHouse")
        self.MushroomHouse.setGeometry(QRect(610, 40, 91, 61))
        self.MushroomHouse.setPixmap(QPixmap(u":/newPrefix/images/mushroom.png"))
        self.MushroomHouse.setScaledContents(True)
        self.MushroomHouse.setWordWrap(False)
        self.CategoryTabWidget = QTabWidget(My_House_Inventory)
        self.CategoryTabWidget.setObjectName(u"CategoryTabWidget")
        self.CategoryTabWidget.setGeometry(QRect(10, 130, 711, 221))
        self.CategoryTabWidget.setAutoFillBackground(False)
        self.CategoryTabWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.CategoryTabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.CategoryTabWidget.setDocumentMode(False)
        self.CategoryTabWidget.setTabsClosable(False)
        self.CategoryTabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ItemTableFromJson = QTableView(self.tab)
        self.ItemTableFromJson.setObjectName(u"ItemTableFromJson")

        self.horizontalLayout_3.addWidget(self.ItemTableFromJson)

        self.CategoryTabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.CategoryTabWidget.addTab(self.tab_2, "")

        self.retranslateUi(My_House_Inventory)

        self.CategoryTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(My_House_Inventory)
    # setupUi

    def retranslateUi(self, My_House_Inventory):
        My_House_Inventory.setWindowTitle(QCoreApplication.translate("My_House_Inventory", u"Form", None))
        self.Add_Item_Button.setText(QCoreApplication.translate("My_House_Inventory", u"Add Item", None))
        self.Remove_Item_Button.setText(QCoreApplication.translate("My_House_Inventory", u"Remove Item", None))
        self.Create_An_Item_Button.setText(QCoreApplication.translate("My_House_Inventory", u"Create an Item", None))
        self.Date_Time_Title.setText(QCoreApplication.translate("My_House_Inventory", u"Today's Date/Time :", None))
        self.Date_Time_Title_Text.setText(QCoreApplication.translate("My_House_Inventory", u"Today's Date/Time:", None))
        self.MushroomHouse.setText("")
        self.CategoryTabWidget.setTabText(self.CategoryTabWidget.indexOf(self.tab), QCoreApplication.translate("My_House_Inventory", u"Tab 1", None))
        self.CategoryTabWidget.setTabText(self.CategoryTabWidget.indexOf(self.tab_2), QCoreApplication.translate("My_House_Inventory", u"Tab 2", None))
    # retranslateUi

