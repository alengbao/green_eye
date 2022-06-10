# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\workspace.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QGraphicsView, QAbstractItemView, QGraphicsProxyWidget

from core.lines import Lines
from core.my_canvas import MyCanvas
from core.my_list import MyList
from core.my_scene import MyScene
from core.node_view import NodeView
from core.line import Line
import os
from core.code_block import CodeBlock


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.length = 1024
        self.height = 1024
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # tab
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")

        # tab_list
        self.tab_list = []
        code_path = 'D:\\Mine\\py\\src\\green_eye\\resource\\codes'
        qdir = QDir(code_path)
        qdir.setFilter(QDir.Dirs)
        for f in qdir.entryInfoList():
            print(1)
            if f.fileName() != '.' and f.fileName() != '..':
                tab = MyList()
                tab.setDragEnabled(True)
                tab.setDragDropMode(QAbstractItemView.DragOnly)
                tab.setObjectName(f.fileName())
                self.tab_list.append(tab)
                self.tabWidget.addTab(tab, '')
                cdir = QDir(code_path + '\\' + f.fileName())
                cdir.setFilter(QDir.Files)
                clist = cdir.entryInfoList()
                for file in clist:
                    with open(file.path() + '\\' + file.fileName(), encoding='utf-8') as code_file:
                        block = CodeBlock(code_file.read(), file.fileName()[:-3])
                        tab.addItem(block)


        self.horizontalLayout.addWidget(self.tabWidget)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setAcceptDrops(True)
        self.graphicsView.scene = MyScene(0, 0, self.length, self.height)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.graphicsView.setScene(self.graphicsView.scene)
        self.canvas = MyCanvas(self.length, self.height)
        self.graphicsView.scene.addItem(self.canvas)
        NodeView(300, 300, '''
def 开始():
    ...

call = 开始
        ''', self.canvas, 0)
        self.ls = Lines(self.length, self.height)
        self.graphicsView.scene.add_lines(self.ls)
        self.horizontalLayout.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "green_eye"))
        for t in self.tab_list:
            self.tabWidget.setTabText(self.tabWidget.indexOf(t), _translate('MainWindow', t.objectName()))
