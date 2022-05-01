# -*- coding:utf-8 -*-
import PyQt5.QtCore as QtCore
from PyQt5.QtCore import QDateTime, Qt, QTimer
import PyQt5.QtWidgets as QtWidgets
import workspace

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = workspace.Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
