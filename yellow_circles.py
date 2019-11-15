# https://github.com/panAlexey/Troitsk-Panarin/blob/master/yellow_circles.py
# 60998c9
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
# from PyQt5.Qt import QPainter
# from PyQt5.QtCore import QPainter
from PyQt5.QtGui import QPainter, QColor
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.cnt = 0
        self.Flag = False

    def run(self):
        self.label.setText("OK")
        self.cnt += 1
        cnt = int(self.lineEdit.text())
        self.cnt = cnt
        print('hi', cnt)
        self.Flag = True
        self.update()


    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        # self.drawBrushes(qp)
        self.drawCircles(qp)
        qp.end()


    def drawCircles(self, qp):
        self.label.setText('Draw' + str(self.cnt))
        if self.Flag:
            col = QColor(255, 255, 0)
            # qp.setPen(col)
            qp.setBrush(col)
            print(self.width(), self.height())
            for i in range(self.cnt):
                xcoor = random.randint(0, self.width() - 50)
                ycoor = random.randint(0, self.height() - 50)
                diametrMax = min(self.height() - ycoor - 30, self.width() - xcoor)

                diametr = random.randint(20, diametrMax)
                print(xcoor, ycoor, diametr)
                qp.drawEllipse(xcoor, ycoor, diametr, diametr)
            self.Flag = False

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())