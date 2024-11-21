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
    QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QTableView, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_My_House_Inventory(object):
    def setupUi(self, My_House_Inventory):
        if not My_House_Inventory.objectName():
            My_House_Inventory.setObjectName(u"My_House_Inventory")
        My_House_Inventory.setEnabled(True)
        My_House_Inventory.resize(760, 615)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(My_House_Inventory.sizePolicy().hasHeightForWidth())
        My_House_Inventory.setSizePolicy(sizePolicy)
        My_House_Inventory.setMinimumSize(QSize(760, 615))
        My_House_Inventory.setMaximumSize(QSize(760, 615))
        icon = QIcon()
        icon.addFile(u":/newPrefix/images/building.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        My_House_Inventory.setWindowIcon(icon)
        My_House_Inventory.setAutoFillBackground(False)
        self.layoutWidget = QWidget(My_House_Inventory)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(390, 580, 362, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Date_Time_Title = QLabel(self.layoutWidget)
        self.Date_Time_Title.setObjectName(u"Date_Time_Title")

        self.horizontalLayout_2.addWidget(self.Date_Time_Title)

        self.Date_Time_Title_Text = QLabel(self.layoutWidget)
        self.Date_Time_Title_Text.setObjectName(u"Date_Time_Title_Text")

        self.horizontalLayout_2.addWidget(self.Date_Time_Title_Text)

        self.dateTimeEdit = QDateTimeEdit(self.layoutWidget)
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
        self.MushroomHouse.setGeometry(QRect(650, 20, 91, 61))
        self.MushroomHouse.setPixmap(QPixmap(u":/newPrefix/images/mushroom.png"))
        self.MushroomHouse.setScaledContents(True)
        self.MushroomHouse.setWordWrap(False)
        self.CategoryTabWidget = QTabWidget(My_House_Inventory)
        self.CategoryTabWidget.setObjectName(u"CategoryTabWidget")
        self.CategoryTabWidget.setGeometry(QRect(20, 260, 711, 311))
        self.CategoryTabWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
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
        self.Create_Item_Group_Box.setGeometry(QRect(30, 20, 227, 201))
        self.Create_Item_Group_Box.setMinimumSize(QSize(0, 170))
        self.Create_Item_Group_Box.setAutoFillBackground(False)
        self.Create_Item_Group_Box.setFlat(True)
        self.Create_Item_Group_Box.setCheckable(False)
        self.layoutWidget1 = QWidget(self.Create_Item_Group_Box)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 16, 205, 172))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Create_An_Item_Button = QPushButton(self.layoutWidget1)
        self.Create_An_Item_Button.setObjectName(u"Create_An_Item_Button")
        self.Create_An_Item_Button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/images/optimization.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Create_An_Item_Button.setIcon(icon1)

        self.gridLayout_2.addWidget(self.Create_An_Item_Button, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_item_name = QLabel(self.layoutWidget1)
        self.label_item_name.setObjectName(u"label_item_name")

        self.gridLayout.addWidget(self.label_item_name, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Create_Item_Item_Name_Line_Edit = QLineEdit(self.layoutWidget1)
        self.Create_Item_Item_Name_Line_Edit.setObjectName(u"Create_Item_Item_Name_Line_Edit")

        self.verticalLayout_3.addWidget(self.Create_Item_Item_Name_Line_Edit)

        self.Create_Item_Quantity_Line_Edit = QLineEdit(self.layoutWidget1)
        self.Create_Item_Quantity_Line_Edit.setObjectName(u"Create_Item_Quantity_Line_Edit")

        self.verticalLayout_3.addWidget(self.Create_Item_Quantity_Line_Edit)

        self.Create_Item_Date_Line_Edit = QLineEdit(self.layoutWidget1)
        self.Create_Item_Date_Line_Edit.setObjectName(u"Create_Item_Date_Line_Edit")

        self.verticalLayout_3.addWidget(self.Create_Item_Date_Line_Edit)

        self.Location_comboBox = QComboBox(self.layoutWidget1)
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

        self.verticalLayout_3.addWidget(self.Location_comboBox)

        self.Category_comboBox = QComboBox(self.layoutWidget1)
        self.Category_comboBox.addItem("")
        self.Category_comboBox.addItem("")
        self.Category_comboBox.addItem("")
        self.Category_comboBox.addItem("")
        self.Category_comboBox.setObjectName(u"Category_comboBox")
        self.Category_comboBox.setEditable(True)

        self.verticalLayout_3.addWidget(self.Category_comboBox)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 5, 1)

        self.label_quantity = QLabel(self.layoutWidget1)
        self.label_quantity.setObjectName(u"label_quantity")

        self.gridLayout.addWidget(self.label_quantity, 1, 0, 1, 1)

        self.label_date = QLabel(self.layoutWidget1)
        self.label_date.setObjectName(u"label_date")

        self.gridLayout.addWidget(self.label_date, 2, 0, 1, 1)

        self.label_location = QLabel(self.layoutWidget1)
        self.label_location.setObjectName(u"label_location")

        self.gridLayout.addWidget(self.label_location, 3, 0, 1, 1)

        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.groupBox = QGroupBox(My_House_Inventory)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(490, 110, 227, 111))
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.Category_comboBox_2 = QComboBox(self.groupBox)
        self.Category_comboBox_2.addItem("")
        self.Category_comboBox_2.addItem("")
        self.Category_comboBox_2.addItem("")
        self.Category_comboBox_2.addItem("")
        self.Category_comboBox_2.setObjectName(u"Category_comboBox_2")
        self.Category_comboBox_2.setEditable(True)

        self.gridLayout_3.addWidget(self.Category_comboBox_2, 1, 1, 1, 1)

        self.label_item_name_2 = QLabel(self.groupBox)
        self.label_item_name_2.setObjectName(u"label_item_name_2")

        self.gridLayout_3.addWidget(self.label_item_name_2, 0, 0, 1, 1)

        self.Create_Item_Item_Name_Line_Edit_2 = QLineEdit(self.groupBox)
        self.Create_Item_Item_Name_Line_Edit_2.setObjectName(u"Create_Item_Item_Name_Line_Edit_2")

        self.gridLayout_3.addWidget(self.Create_Item_Item_Name_Line_Edit_2, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.Remove_Item_Button = QPushButton(self.groupBox)
        self.Remove_Item_Button.setObjectName(u"Remove_Item_Button")
        self.Remove_Item_Button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/images/subtract-of-shopping-cart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Remove_Item_Button.setIcon(icon2)

        self.gridLayout_4.addWidget(self.Remove_Item_Button, 0, 0, 1, 1)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.gridLayout_4)

        self.Create_Item_Group_Box_2 = QGroupBox(My_House_Inventory)
        self.Create_Item_Group_Box_2.setObjectName(u"Create_Item_Group_Box_2")
        self.Create_Item_Group_Box_2.setEnabled(True)
        self.Create_Item_Group_Box_2.setGeometry(QRect(260, 20, 227, 201))
        self.Create_Item_Group_Box_2.setMinimumSize(QSize(0, 170))
        self.Create_Item_Group_Box_2.setAutoFillBackground(False)
        self.Create_Item_Group_Box_2.setFlat(True)
        self.Create_Item_Group_Box_2.setCheckable(False)
        self.layoutWidget_2 = QWidget(self.Create_Item_Group_Box_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 16, 205, 172))
        self.gridLayout_5 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Adjust_Item_Button = QPushButton(self.layoutWidget_2)
        self.Adjust_Item_Button.setObjectName(u"Adjust_Item_Button")
        self.Adjust_Item_Button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/images/adjustment.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Adjust_Item_Button.setIcon(icon3)

        self.gridLayout_5.addWidget(self.Adjust_Item_Button, 0, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_item_name_3 = QLabel(self.layoutWidget_2)
        self.label_item_name_3.setObjectName(u"label_item_name_3")

        self.gridLayout_6.addWidget(self.label_item_name_3, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Create_Item_Item_Name_Line_Edit_3 = QLineEdit(self.layoutWidget_2)
        self.Create_Item_Item_Name_Line_Edit_3.setObjectName(u"Create_Item_Item_Name_Line_Edit_3")

        self.verticalLayout_4.addWidget(self.Create_Item_Item_Name_Line_Edit_3)

        self.Create_Item_Quantity_Line_Edit_2 = QLineEdit(self.layoutWidget_2)
        self.Create_Item_Quantity_Line_Edit_2.setObjectName(u"Create_Item_Quantity_Line_Edit_2")

        self.verticalLayout_4.addWidget(self.Create_Item_Quantity_Line_Edit_2)

        self.Create_Item_Date_Line_Edit_2 = QLineEdit(self.layoutWidget_2)
        self.Create_Item_Date_Line_Edit_2.setObjectName(u"Create_Item_Date_Line_Edit_2")

        self.verticalLayout_4.addWidget(self.Create_Item_Date_Line_Edit_2)

        self.Location_comboBox_2 = QComboBox(self.layoutWidget_2)
        self.Location_comboBox_2.addItem("")
        self.Location_comboBox_2.addItem("")
        self.Location_comboBox_2.addItem("")
        self.Location_comboBox_2.addItem("")
        self.Location_comboBox_2.addItem("")
        self.Location_comboBox_2.setObjectName(u"Location_comboBox_2")
        self.Location_comboBox_2.setEditable(True)
        self.Location_comboBox_2.setMaxVisibleItems(10)
        self.Location_comboBox_2.setMaxCount(2147483647)
        self.Location_comboBox_2.setMinimumContentsLength(1)
        self.Location_comboBox_2.setDuplicatesEnabled(False)

        self.verticalLayout_4.addWidget(self.Location_comboBox_2)

        self.Category_comboBox_3 = QComboBox(self.layoutWidget_2)
        self.Category_comboBox_3.addItem("")
        self.Category_comboBox_3.addItem("")
        self.Category_comboBox_3.addItem("")
        self.Category_comboBox_3.addItem("")
        self.Category_comboBox_3.setObjectName(u"Category_comboBox_3")
        self.Category_comboBox_3.setEditable(True)

        self.verticalLayout_4.addWidget(self.Category_comboBox_3)


        self.gridLayout_6.addLayout(self.verticalLayout_4, 0, 1, 5, 1)

        self.label_quantity_2 = QLabel(self.layoutWidget_2)
        self.label_quantity_2.setObjectName(u"label_quantity_2")

        self.gridLayout_6.addWidget(self.label_quantity_2, 1, 0, 1, 1)

        self.label_date_2 = QLabel(self.layoutWidget_2)
        self.label_date_2.setObjectName(u"label_date_2")

        self.gridLayout_6.addWidget(self.label_date_2, 2, 0, 1, 1)

        self.label_location_2 = QLabel(self.layoutWidget_2)
        self.label_location_2.setObjectName(u"label_location_2")

        self.gridLayout_6.addWidget(self.label_location_2, 3, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 4, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_6, 1, 0, 1, 1)


        self.retranslateUi(My_House_Inventory)

        self.CategoryTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(My_House_Inventory)
    # setupUi

    def retranslateUi(self, My_House_Inventory):
        My_House_Inventory.setWindowTitle(QCoreApplication.translate("My_House_Inventory", u"Form", None))
        self.Date_Time_Title.setText(QCoreApplication.translate("My_House_Inventory", u"Today's Date/Time :", None))
        self.Date_Time_Title_Text.setText(QCoreApplication.translate("My_House_Inventory", u"Today's Date/Time:", None))
        self.MushroomHouse.setText("")
        self.CategoryTabWidget.setTabText(self.CategoryTabWidget.indexOf(self.tab), QCoreApplication.translate("My_House_Inventory", u"Tab 1", None))
        self.CategoryTabWidget.setTabText(self.CategoryTabWidget.indexOf(self.tab_2), QCoreApplication.translate("My_House_Inventory", u"Tab 2", None))
        self.Create_Item_Group_Box.setTitle("")
        self.Create_An_Item_Button.setText(QCoreApplication.translate("My_House_Inventory", u"Create a new item", None))
        self.label_item_name.setText(QCoreApplication.translate("My_House_Inventory", u"Item Name:", None))
        self.Create_Item_Date_Line_Edit.setInputMask("")
        self.Create_Item_Date_Line_Edit.setText("")
        self.Location_comboBox.setItemText(0, QCoreApplication.translate("My_House_Inventory", u"Fridge", None))
        self.Location_comboBox.setItemText(1, QCoreApplication.translate("My_House_Inventory", u"Cabinet", None))
        self.Location_comboBox.setItemText(2, QCoreApplication.translate("My_House_Inventory", u"Yellow Box", None))
        self.Location_comboBox.setItemText(3, QCoreApplication.translate("My_House_Inventory", u"Black Stand", None))
        self.Location_comboBox.setItemText(4, QCoreApplication.translate("My_House_Inventory", u"Wall", None))

        self.Location_comboBox.setCurrentText(QCoreApplication.translate("My_House_Inventory", u"Fridge", None))
        self.Location_comboBox.setPlaceholderText("")
        self.Category_comboBox.setItemText(0, QCoreApplication.translate("My_House_Inventory", u"Fruits", None))
        self.Category_comboBox.setItemText(1, QCoreApplication.translate("My_House_Inventory", u"Ingredients", None))
        self.Category_comboBox.setItemText(2, QCoreApplication.translate("My_House_Inventory", u"Snow Gear", None))
        self.Category_comboBox.setItemText(3, QCoreApplication.translate("My_House_Inventory", u"Bathroom", None))

        self.label_quantity.setText(QCoreApplication.translate("My_House_Inventory", u"Quantity:", None))
        self.label_date.setText(QCoreApplication.translate("My_House_Inventory", u"Date:", None))
        self.label_location.setText(QCoreApplication.translate("My_House_Inventory", u"Location:", None))
        self.label.setText(QCoreApplication.translate("My_House_Inventory", u"Category:", None))
        self.groupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("My_House_Inventory", u"Category:", None))
        self.Category_comboBox_2.setItemText(0, QCoreApplication.translate("My_House_Inventory", u"Fruits", None))
        self.Category_comboBox_2.setItemText(1, QCoreApplication.translate("My_House_Inventory", u"Ingredients", None))
        self.Category_comboBox_2.setItemText(2, QCoreApplication.translate("My_House_Inventory", u"Snow Gear", None))
        self.Category_comboBox_2.setItemText(3, QCoreApplication.translate("My_House_Inventory", u"Bathroom", None))

        self.label_item_name_2.setText(QCoreApplication.translate("My_House_Inventory", u"Item Name:", None))
        self.Remove_Item_Button.setText(QCoreApplication.translate("My_House_Inventory", u"Remove item", None))
        self.Create_Item_Group_Box_2.setTitle("")
        self.Adjust_Item_Button.setText(QCoreApplication.translate("My_House_Inventory", u"Adjust item", None))
        self.label_item_name_3.setText(QCoreApplication.translate("My_House_Inventory", u"Item Name:", None))
        self.Create_Item_Date_Line_Edit_2.setInputMask("")
        self.Create_Item_Date_Line_Edit_2.setText("")
        self.Location_comboBox_2.setItemText(0, QCoreApplication.translate("My_House_Inventory", u"Fridge", None))
        self.Location_comboBox_2.setItemText(1, QCoreApplication.translate("My_House_Inventory", u"Cabinet", None))
        self.Location_comboBox_2.setItemText(2, QCoreApplication.translate("My_House_Inventory", u"Yellow Box", None))
        self.Location_comboBox_2.setItemText(3, QCoreApplication.translate("My_House_Inventory", u"Black Stand", None))
        self.Location_comboBox_2.setItemText(4, QCoreApplication.translate("My_House_Inventory", u"Wall", None))

        self.Location_comboBox_2.setCurrentText(QCoreApplication.translate("My_House_Inventory", u"Fridge", None))
        self.Location_comboBox_2.setPlaceholderText("")
        self.Category_comboBox_3.setItemText(0, QCoreApplication.translate("My_House_Inventory", u"Fruits", None))
        self.Category_comboBox_3.setItemText(1, QCoreApplication.translate("My_House_Inventory", u"Ingredients", None))
        self.Category_comboBox_3.setItemText(2, QCoreApplication.translate("My_House_Inventory", u"Snow Gear", None))
        self.Category_comboBox_3.setItemText(3, QCoreApplication.translate("My_House_Inventory", u"Bathroom", None))

        self.label_quantity_2.setText(QCoreApplication.translate("My_House_Inventory", u"Quantity:", None))
        self.label_date_2.setText(QCoreApplication.translate("My_House_Inventory", u"Date:", None))
        self.label_location_2.setText(QCoreApplication.translate("My_House_Inventory", u"Location:", None))
        self.label_3.setText(QCoreApplication.translate("My_House_Inventory", u"Category:", None))
    # retranslateUi

