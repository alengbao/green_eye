from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainterPath
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem
import typing


class Line:
    def __init__(self, stx, sty, edx, edy):
        super().__init__()
        self.stx = stx
        self.sty = sty
        self.edx = edx
        self.edy = edy

    def set_st(self, x, y):
        self.stx = x
        self.sty = y

    def set_ed(self, x, y):
        self.edx = x
        self.edy = y
