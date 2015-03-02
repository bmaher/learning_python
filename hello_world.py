import sys

from PySide.QtCore import *
from PySide.QtGui import *

qt_app = QApplication(sys.argv)

class HelloWorldApp(QLabel):
  '''A Qt application that displays the text "Hello, world!"'''
  def __init__(self):
    QLabel.__init__(self, "Hello, world!")

    self.setMinimumSize(QSize(800, 600))
    self.setAlignment(Qt.AlignCenter)
    self.setWindowTitle('Hello, world!')

  def run(self):
    '''Show the application window and start the main loop.'''
    self.show()
    qt_app.exec_()

HelloWorldApp().run()

