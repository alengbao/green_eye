from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainterPath
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem
import typing


class Line(QtWidgets.QGraphicsItem):
    def __init__(self, stx, sty, edx, edy):
        super().__init__()
        self.stx = stx
        self.sty = sty
        self.edx = edx
        self.edy = edy
        self.setPos(stx, sty)

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(min(self.stx, self.stx + (self.stx - self.edx) / 6, self.edx - (self.stx - self.edx) / 6,
                                 self.edx),
                             min(self.sty, self.sty + (self.sty + self.edy) / 6, self.edy - (self.sty + self.edy) / 6,
                                 self.edy),
                             max(self.stx, self.stx + (self.stx - self.edx) / 6, self.edx - (self.stx - self.edx) / 6,
                                 self.edx),
                             max(self.sty, self.sty + (self.sty + self.edy) / 6, self.edy - (self.sty + self.edy) / 6,
                                 self.edy),
                             )

    def set_st(self, x, y):
        self.stx = x
        self.sty = y
        self.setPos(x, y)

    def set_ed(self, x, y):
        self.edx = x
        self.edy = y

    def paint(self, painter: QtGui.QPainter, option: QStyleOptionGraphicsItem, widget: typing.Optional[QWidget] = ...) -> None:
        painter.setPen(QtGui.QColor(0, 0, 0))
        path = QPainterPath()
        path.moveTo(self.stx, self.sty)
        path.cubicTo(self.stx + (self.stx - self.edx) / 6, self.sty + (self.sty + self.edy) / 6,
                     self.edx - (self.stx - self.edx) / 6, self.edy - (self.sty + self.edy) / 6,
                     self.edx, self.edy)
        painter.drawPath(path)
