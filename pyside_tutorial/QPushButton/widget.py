from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):
    def __int__(self):
        super().__init__()

        self.setWindowTitle("Custom MainWindow")

        button = QPushButton("Click")
        button.