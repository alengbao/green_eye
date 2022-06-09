import typing

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QGraphicsItem, QWidget, QStyleOptionGraphicsItem, \
    QGraphicsSceneDragDropEvent, QGraphicsSceneMouseEvent


from core.point import Point
from core.node import Node
from core.line import Line


class NodeView(Node, QGraphicsItem):
    def __init__(self, x: int, y: int,
                 code: str = '', parent=None, node_id: int = None):
        Node.__init__(self, code, node_id)
        QGraphicsItem.__init__(self, parent)
        self.setPos(x, y)
        self.length = 210
        self.height = max(35+len(self.inputs)*30, 35+len(self.outputs)*30)
        self.input_points = []
        self.output_points = []
        self.setFlag(QGraphicsItem.ItemIsMovable)

        for i in self.inputs:
            p = Point(i, 'input', self)
            p.setPos(10, self.inputs.index(i)*30+35)
            self.input_points.append(p)

        for i in self.outputs:
            p = Point(i, 'output', self)
            p.setPos(190, self.outputs.index(i)*30+35)
            self.output_points.append(p)

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0, 0, self.length, self.height)

    def paint(self, painter: QtGui.QPainter, option: QStyleOptionGraphicsItem,
              widget: typing.Optional[QWidget] = ...) -> None:
        first_line_height = 25
        painter.setBrush(QtGui.QColor(187, 255, 255))
        painter.drawRect(0, 0, self.length, first_line_height)
        painter.setBrush(QtGui.QColor(255, 235, 205))
        painter.drawRect(0, first_line_height, self.length, self.height-first_line_height)
        painter.setPen(QtGui.QColor(0, 0, 0))
        painter.drawText(15, 20, self.name)

