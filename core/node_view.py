import typing

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QGraphicsItem, QWidget, QStyleOptionGraphicsItem, \
    QGraphicsSceneDragDropEvent, QGraphicsSceneMouseEvent


from core.point import Point
from core.node import Node


class NodeView(Node, QGraphicsItem):
    def __init__(self, x: int, y: int,
                 code: str = '', node_id: int = None):
        Node.__init__(self, code, node_id)
        QGraphicsItem.__init__(self)
        self.setPos(x, y)
        self.length = 200
        self.height = 150
        self.input_points = []
        self.output_points = []
        self.setFlag(QGraphicsItem.ItemIsMovable)

        for i in self.inputs:
            p = Point(i, self)
            p.setPos(10, self.inputs.index(i)*30+30)
            self.input_points.append(p)

        for i in self.outputs:
            p = Point(i, self)
            p.setPos(100, self.outputs.index(i)*30+30)
            self.output_points.append(p)

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0, 0, self.length, self.height)

    def paint(self, painter: QtGui.QPainter, option: QStyleOptionGraphicsItem,
              widget: typing.Optional[QWidget] = ...) -> None:
        painter.setBrush(QtGui.QColor(123, 0, 124))
        painter.drawRect(0, 0, self.length, self.height)
        painter.setPen(QtGui.QColor(0, 0, 0))
        painter.drawText(10, 20, self.name)
