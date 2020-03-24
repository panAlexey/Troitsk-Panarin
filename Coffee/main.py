import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
# from PyQt5.Qt import QPainter
# from PyQt5.QtCore import QPainter
from PyQt5.QtGui import QPainter, QColor
import random
from ui_randomcircle import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        # super().__init__()
        super().__init__()
        uic.loadUi('coffee.ui', self)
        # self.pushButton.clicked.connect(self.run)
        self.cnt = 0
        self.Flag = False


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())