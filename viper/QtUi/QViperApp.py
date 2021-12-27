import sys
from PySide6 import QtWidgets
from viper.QtUi.QViperWindow import QViperWindow

class QViperApp():
   def __init__(self) -> None:
      self.window = QViperWindow()
   
   @classmethod
   def start(cls):
    app = QtWidgets.QApplication([])

    widget = cls()
    widget.window.resize(800, 600)
    widget.window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
   QViperApp.start()
