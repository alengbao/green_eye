from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMimeData, Qt
from PyQt5.QtGui import QDrag


class CodeBlock(QtWidgets.QListWidgetItem):
    def __init__(self, code, name):
        QtWidgets.QListWidgetItem.__init__(self)
        self.code = code
        self.name = name
        self.setText(self.name)
