from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem
import typing

from core.line import Line


class Point(QtWidgets.QGraphicsItem):
    def __init__(self, name, point_type, parent=None):
        super().__init__(parent)
        self.name = name
        self.point_type = point_type

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0, 0, 20, 20)

    def paint(self, painter: QtGui.QPainter, option: QStyleOptionGraphicsItem,
              widget: typing.Optional[QWidget] = ...) -> None:
        painter.setBrush(QtGui.QColor(255, 0, 0))
        painter.setPen(QtGui.QColor(255, 0, 0))
        painter.drawPie(0, 0, 12, 12, 0*16, 360*16)
        painter.setPen(QtGui.QColor(0, 0, 0))
        painter.drawText(20, 12, self.name)

    def add_line(self, line: Line):
        ...
