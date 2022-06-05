from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem
import typing


class Point(QtWidgets.QGraphicsItem):
    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.name = name

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0, 0, 20, 20)

    def paint(self, painter: QtGui.QPainter, option: QStyleOptionGraphicsItem,
              widget: typing.Optional[QWidget] = ...) -> None:
        painter.setBrush(QtGui.QColor(255, 0, 0))
        painter.setPen(QtGui.QColor(255, 0, 0))
        painter.drawPie(0, 0, 15, 15, 0*16, 360*16)
        painter.drawText(25, 10, self.name)
