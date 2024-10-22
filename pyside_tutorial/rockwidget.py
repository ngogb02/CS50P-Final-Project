from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class RocWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")

        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")

        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button1.clicked.connect(self.button1_clicked)
        button_layout.addWidget(button2)
        button2.clicked.connect(self.button2_clicked)

        self.setLayout(button_layout)

    def button1_clicked(self):
        print("Button1 clicked")

    def button2_clicked(self):
        print("Button2 clicked")


    