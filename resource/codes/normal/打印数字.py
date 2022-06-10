from PyQt5.QtWidgets import QMessageBox


def 打印数字(number: int, called=None):
    print(number)
    box = QMessageBox()
    box.setIcon(1)
    box.setWindowTitle("结果")
    box.setText('%d' % number)
    # 添加按钮，可用中文
    yes = box.addButton('确定', QMessageBox.YesRole)
    no = box.addButton('取消', QMessageBox.NoRole)
    # 设置消息框中内容前面的图标
    box.setIcon(1)
    box.exec_()
    return number


call = 打印数字
