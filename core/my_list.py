import typing

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QMimeData, Qt
from PyQt5.QtGui import QDrag


class MyList(QtWidgets.QListWidget):
    def __init__(self):
        super().__init__()

    def startDrag(self, supportedActions: typing.Union[QtCore.Qt.DropActions, QtCore.Qt.DropAction]) -> None:
        item = self.currentItem()
        mimeData = QMimeData()
        mimeData.setText(item.code)
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.exec_(Qt.MoveAction)
