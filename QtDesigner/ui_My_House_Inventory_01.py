# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'My_House_Inventory_01.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateTimeEdit,
    QFormLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QTableView, QVBoxLayout, QWidget)
import resource_rc

class Ui_My_House_Inventory(object):
    def setupUi(self, My_House_Inventory):
        if not My_House_Inventory.objectName():
            My_House_Inventory.setObjectName(u"My_House_Inventory")
        My_House_Inventory.setEnabled(True)
        My_House_Inventory.resize(763, 628)
        icon = QIcon()
        icon.addFile(u":/newPrefix/images/building.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        My_House_Inventory.setWindowIcon(icon)
        My_House_Inventory.setAutoFillBackground(False)
        self.layoutWidget = QWidget(My_House_Inventory)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(280, 40, 233, 88))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Add_Item_Button = QPushButton(self.layoutWidget)
        self.Add_Item_Button.setObjectName(u"Add_Item_Button")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/images/add-to-cart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Add_Item_Button.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.Add_Item_Button)

        self.Remove_Item_Button = QPushButton(self.layoutWidget)
        self.Remove_Item_Button.setObjectName(u"Remove_Item_Button")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/images/subtract-of-shopping-cart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Remove_Item_Button.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.Remove_Item_Button)


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


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.layoutWidget1 = QWidget(My_House_Inventory)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(390, 580, 362, 25))
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
        self.CategoryTabWidget.setGeometry(QRect(20, 230, 711, 341))
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
        self.Create_Item_Group_Box = QGroupBox(My_House_Inventory)
        self.Create_Item_Group_Box.setObjectName(u"Create_Item_Group_Box")
        self.Create_Item_Group_Box.setEnabled(True)
        self.Create_Item_Group_Box.setGeometry(QRect(20, 20, 227, 181))
        self.Create_Item_Group_Box.setAutoFillBackground(False)
        self.Create_Item_Group_Box.setFlat(True)
        self.Create_Item_Group_Box.setCheckable(False)
        self.layoutWidget2 = QWidget(self.Create_Item_Group_Box)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(13, 30, 203, 141))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Create_An_Item_Button = QPushButton(self.layoutWidget2)
        self.Create_An_Item_Button.setObjectName(u"Create_An_Item_Button")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/images/optimization.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Create_An_Item_Button.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.Create_An_Item_Button)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_item_name = QLabel(self.layoutWidget2)
        self.label_item_name.setObjectName(u"label_item_name")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_item_name)

        self.Create_Item_Item_Name_Line_Edit = QLineEdit(self.layoutWidget2)
        self.Create_Item_Item_Name_Line_Edit.setObjectName(u"Create_Item_Item_Name_Line_Edit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.Create_Item_Item_Name_Line_Edit)

        self.label_quantity = QLabel(self.layoutWidget2)
        self.label_quantity.setObjectName(u"label_quantity")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_quantity)

        self.Create_Item_Quantity_Line_Edit = QLineEdit(self.layoutWidget2)
        self.Create_Item_Quantity_Line_Edit.setObjectName(u"Create_Item_Quantity_Line_Edit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Create_Item_Quantity_Line_Edit)

        self.label_location = QLabel(self.layoutWidget2)
        self.label_location.setObjectName(u"label_location")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_location)

        self.label_date = QLabel(self.layoutWidget2)
        self.label_date.setObjectName(u"label_date")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_date)

        self.Create_Item_Date_Line_Edit = QLineEdit(self.layoutWidget2)
        self.Create_Item_Date_Line_Edit.setObjectName(u"Create_Item_Date_Line_Edit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.Create_Item_Date_Line_Edit)

        self.Location_comboBox = QComboBox(self.layoutWidget2)
        self.Location_comboBox.addItem("")
        self.Location_comboBox.addItem("")
        self.Location_comboBox.addItem("")
        self.Location_comboBox.addItem("")
        self.Location_comboBox.addItem("")
        self.Location_comboBox.setObjectName(u"Location_comboBox")
        self.Location_comboBox.setEditable(True)
        self.Location_comboBox.setMaxVisibleItems(10)
        self.Location_comboBox.setMaxCount(2147483647)
        self.Location_comboBox.setMinimumContentsLength(1)
        self.Location_comboBox.setDuplicatesEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.Location_comboBox)


        self.verticalLayout_3.addLayout(self.formLayout)


        self.retranslateUi(My_House_Inventory)

        self.CategoryTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(My_House_Inventory)
    # setupUi

    def retranslateUi(self, My_House_Inventory):
        My_House_Inventory.setWindowTitle(QCoreApplication.translate("My_House_Inventory", u"Form", None))
        self.Add_Item_Button.setText(QCoreApplication.translate("My_House_Inventory", u"Add Item", None))
        self.Remove_Item_Button.setText(QCoreApplication.translate("My_House_Inventory", u"Remove Item", None))
        self.Date_Time_Title.setText(QCoreApplication.translate("My_House_Inventory", u"Today's Date/Time :", None))
        self.Date_Time_Title_Text.setText(QCoreApplication.translate("My_House_Inventory", u"Today's Date/Time:", None))
        self.MushroomHouse.setText("")
        self.CategoryTabWidget.setTabText(self.CategoryTabWidget.indexOf(self.tab), QCoreApplication.translate("My_House_Inventory", u"Tab 1", None))
        self.CategoryTabWidget.setTabText(self.CategoryTabWidget.indexOf(self.tab_2), QCoreApplication.translate("My_House_Inventory", u"Tab 2", None))
        self.Create_Item_Group_Box.setTitle("")
        self.Create_An_Item_Button.setText(QCoreApplication.translate("My_House_Inventory", u"Create a new item", None))
        self.label_item_name.setText(QCoreApplication.translate("My_House_Inventory", u"Item Name:", None))
        self.label_quantity.setText(QCoreApplication.translate("My_House_Inventory", u"Quantity:", None))
        self.label_location.setText(QCoreApplication.translate("My_House_Inventory", u"Location:", None))
        self.label_date.setText(QCoreApplication.translate("My_House_Inventory", u"Date:", None))
        self.Create_Item_Date_Line_Edit.setInputMask("")
        self.Create_Item_Date_Line_Edit.setText("")
        self.Location_comboBox.setItemText(0, QCoreApplication.translate("My_House_Inventory", u"Fridge", None))
        self.Location_comboBox.setItemText(1, QCoreApplication.translate("My_House_Inventory", u"Cabinet", None))
        self.Location_comboBox.setItemText(2, QCoreApplication.translate("My_House_Inventory", u"Yellow Box", None))
        self.Location_comboBox.setItemText(3, QCoreApplication.translate("My_House_Inventory", u"Black Stand", None))
        self.Location_comboBox.setItemText(4, QCoreApplication.translate("My_House_Inventory", u"Wall", None))

        self.Location_comboBox.setCurrentText(QCoreApplication.translate("My_House_Inventory", u"Fridge", None))
        self.Location_comboBox.setPlaceholderText("")
    # retranslateUi

