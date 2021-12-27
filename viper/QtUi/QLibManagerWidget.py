from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QListView
from PySide6.QtGui import QStandardItemModel
from typing import Optional

class QLibManagerWidget(QWidget):
   def __init__(self) -> None:
      super().__init__()
      self.lib_widget = QListView(parent = self)

class QLCVItemModel(QStandardItemModel):
   """A model of a library, cell, or view (LCV)"""
   
   def __init__(self, item) -> None:
       super().__init__()
       self.item = item
