from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QGraphicsSceneDragDropEvent

from core.line import Line
from core.lines import Lines
from core.node import Node


class MyScene(QtWidgets.QGraphicsScene):
    def __init__(self, x, y, w, z):
        super().__init__(x, y, w, z)
        self.lines = None

    def add_lines(self, lines: Lines):
        self.lines = lines
        self.addItem(lines)

    def add_line(self, line: Line):
        self.lines.add_line(line)

    def remove_line(self, line: Line):
        self.lines.remove_line(line)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key_R:
            Node.dic[0].processor(True)

    def dragEnterEvent(self, event: QGraphicsSceneDragDropEvent) -> None:
        event.accept()
        # if event.mimeData().hasFormat('text/plain'):
        #     event.accept()
        # else:
        #     event.ignore()
