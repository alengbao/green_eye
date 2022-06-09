from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter, QTransform
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem, \
    QGraphicsSceneMouseEvent, QGraphicsView
import typing

from core.line import Line
from core.node import Node


def get_point(pos: QPointF, scene: QtWidgets.QGraphicsScene):
    for i in scene.items(pos):
        if isinstance(i, Point):
            return i
    return None


class Point(QtWidgets.QGraphicsItem):
    cnt = 0

    def __init__(self, name, point_type, parent=None):
        super().__init__(parent)
        self.id = Point.cnt
        Point.cnt += 1
        self.name = name
        self.point_type = point_type
        self.st_lines = []
        self.ed_lines = []
        self.tem_line = None

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0, 0, 20, 20)

    def paint(self, painter: QtGui.QPainter, option: QStyleOptionGraphicsItem,
              widget: typing.Optional[QWidget] = ...) -> None:
        for l in self.st_lines:
            l.set_st(self.scenePos().x()+6, self.scenePos().y()+6)
        for l in self.ed_lines:
            l.set_ed(self.scenePos().x()+6, self.scenePos().y()+6)

        painter.setBrush(QtGui.QColor(255, 0, 0))
        painter.setPen(QtGui.QColor(255, 0, 0))
        if self.point_type == 'input':
            painter.drawPie(0, 0, 12, 12, 0 * 16, 360 * 16)
            painter.setPen(QtGui.QColor(0, 0, 0))
            painter.drawText(20, 12, self.name)
        else:
            painter.drawPie(0, 0, 12, 12, 0 * 16, 360 * 16)
            painter.setPen(QtGui.QColor(0, 0, 0))
            painter.drawText(-65, 12, self.name)
        self.scene().update()

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if self.point_type == 'input':
            l = Line(event.scenePos().x(), event.scenePos().y(), self.scenePos().x() + 6, self.scenePos().y() + 6)
            self.tem_line = l
        else:
            l = Line(self.scenePos().x() + 6, self.scenePos().y() + 6, event.scenePos().x(), event.scenePos().y())
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
            p = get_point(event.scenePos(), self.scene())
            if p is None or p.parentItem() is self.parentItem() or p.point_type == self.point_type or \
                    (p.point_type == 'input' and len(p.ed_lines) > 0) or \
                    (self.point_type == 'input' and len(self.ed_lines) > 0):
                self.scene().remove_line(self.tem_line)
            else:
                if p.point_type == 'input':
                    p.ed_lines.append(self.tem_line)
                    self.st_lines.append(self.tem_line)
                    p.parentItem().add_connected(self.parentItem(), p.name, self.name)
                else:
                    p.st_lines.append(self.tem_line)
                    self.ed_lines.append(self.tem_line)
                    self.parentItem().add_connected(p.parentItem(), self.name, p.name)
            self.tem_line = None
            self.scene().update()

