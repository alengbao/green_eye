import typing

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPainterPath
from PyQt5.QtWidgets import QGraphicsItem, QWidget, QStyleOptionGraphicsItem, \
    QGraphicsSceneDragDropEvent, QGraphicsSceneMouseEvent


from core.point import Point
from core.node import Node
from core.line import Line


class Lines(QGraphicsItem):
    def __init__(self, x, y):
        super().__init__()
        self.lines = []
        self.x = x
        self.y = y

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0, 0, self.x, self.y)

    def paint(self, painter: QtGui.QPainter, option: 'QStyleOptionGraphicsItem', widget: typing.Optional[QWidget] = ...) -> None:
        painter.setPen(QtGui.QColor(0, 0, 0))
        path = QPainterPath()
        for line in self.lines:
            path.moveTo(line.stx, line.sty)
            path.cubicTo(line.stx - (line.stx - line.edx) / 6, line.sty + (line.sty + line.edy) / 6,
                         line.edx + (line.stx - line.edx) / 6, line.edy - (line.sty + line.edy) / 6,
                         line.edx, line.edy)
            painter.drawPath(path)

    def add_line(self, line: Line):
        self.lines.append(line)

    def remove_line(self, line: Line):
        self.lines.remove(line)
