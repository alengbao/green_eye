import typing

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QGraphicsItem, QWidget, QStyleOptionGraphicsItem, \
    QGraphicsSceneDragDropEvent

from core.node_view import NodeView


class MyCanvas(QGraphicsItem):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.setPos(0, 0)
        self.setAcceptDrops(True)

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0, 0, self.x, self.y)

    def paint(self, painter: QtGui.QPainter, option: QStyleOptionGraphicsItem,
              widget: typing.Optional[QWidget] = ...) -> None:
        ...

    def dragEnterEvent(self, event: QGraphicsSceneDragDropEvent) -> None:
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QGraphicsSceneDragDropEvent) -> None:
        pos = event.pos()
        print('adding')
        self.add_node(event.mimeData().text(), pos.x(), pos.y())
        print('add success')

    def add_node(self, code, x, y):
        NodeView(x, y, code, self)
        self.scene().update()
