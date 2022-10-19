import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui

class ProjectManagerApp():

    _MAIN_WINDOW = None

    @property
    @classmethod
    def main_window(cls):
        if cls._MAIN_WINDOW is None:
            cls._MAIN_WINDOW = QMainWindow()
        return cls._MAIN_WINDOW


class QCellSelectionWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.lib_listbox = QtWidgets.QListWidget()
        self.cell_listbox = QtWidgets.QListWidget()
        self.view_listbox = QtWidgets.QListWidget()

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.lib_listbox)
        self.layout.addWidget(self.cell_listbox)
        self.layout.addWidget(self.view_listbox)


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
