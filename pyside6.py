#note: had to install "sudo apt-get install -y libxcb-cursor-dev" for pyside6 to run. 

#import the components we need
from PySide6.QtWidgets import QApplication, QWidget

#the sys module is responsible for processing command line arguments 
import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

#start the event loop
app.exec()
