from PySide6.QtWidgets import QMainWindow
from .QLibManagerWidget import QLibManagerWidget


class QViperWindow(QMainWindow):
   def __init__(self) -> None:
      super().__init__()
      self._create_central_widget()
      
   def _create_central_widget(self):
      self.setCentralWidget(QLibManagerWidget())
