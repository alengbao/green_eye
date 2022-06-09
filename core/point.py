from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QTransform
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem, \
    QGraphicsSceneMouseEvent
import typing

from core.line import Line


class Point(QtWidgets.QGraphicsItem):
    def __init__(self, name, point_type, parent=None):
        super().__init__(parent)
        self.name = name
        self.point_type = point_type
        self.st_lines = []
        self.ed_lines = []
        self.tem_line = None

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0, 0, 20, 20)

    def paint(self, painter: QtGui.QPainter, option: QStyleOptionGraphicsItem,
              widget: typing.Optional[QWidget] = ...) -> None:
        painter.setBrush(QtGui.QColor(255, 0, 0))
        painter.setPen(QtGui.QColor(255, 0, 0))
        painter.drawPie(0, 0, 12, 12, 0 * 16, 360 * 16)
        painter.setPen(QtGui.QColor(0, 0, 0))
        painter.drawText(20, 12, self.name)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if self.point_type == 'input':
            l = Line(event.scenePos().x(), event.scenePos().y(), self.scenePos().x()+6, self.scenePos().y()+6)
            self.tem_line = l
        else:
            l = Line(self.scenePos().x()+6, self.scenePos().y()+6, event.scenePos().x(), event.scenePos().y())
            self.tem_line = l
        self.scene().add_line(l)
        self.scene().update()

    def mouseMoveEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        print(event.scenePos().x(), event.scenePos().y())
        if self.point_type == 'input':
            self.tem_line.set_st(event.scenePos().x(), event.scenePos().y())
        else:
            self.tem_line.set_ed(event.scenePos().x(), event.scenePos().y())
        self.scene().update()

    def mouseReleaseEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        if self.tem_line is not None:
            self.scene().remove_line(self.tem_line)
            self.tem_line = None
        self.scene().update()
