from class_project import * 
from PySide6.QtWidgets import QApplication
from widget import Widget
import sys

#class Apple(InputReq):
    #pass
def create_item_class(item_name: str, location: str, quantity: int, date: str) -> None:
    class_builder = f"""
        class {item_name}(InputReq):
            def __init__(self, location, quantity, date)
                super().__init__(location, quantity, date)"""

def insert_items_into_House():
    ...


def slot_functions():
    ...


def main():
    my_house = House()

    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()

    app.exec()

if __name__ == "__main__":
    main()