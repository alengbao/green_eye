from PyQt5 import QtWidgets


class CodeBlock(QtWidgets.QListWidgetItem):
    def __init__(self, code, name):
        QtWidgets.QListWidgetItem.__init__(self)
        self.code = code
        self.name = name
        self.setText(self.name)
