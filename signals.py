import sys

from PySide.QtCore import *
from PySide.QtGui import *

class Form(QDialog):

	def __init__(self, parent=None):
		super(Form, self).__init__(parent)

		dial = QDial()
		dial.setNotchesVisibile(True)

		spinbox = QSpinBox()

		layou = QHBoxLayout()
		layout.addWidget(dial)
		layout.addWidget(spinbox)
		self.setLayout(layout)

		self.connect(dial, SIGNAL("valueChanged(int)"), spinbox.setValue)
		self.connect(spinbox, SIGNAL("valueChanged(int)"), dial.setValue)
