# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Skazka
# Purpose:
#
# Authors:      Марков Сергей, Артём Вишногор, Анастасия Вишногорская
#
# Created:     22.02.2017
# Copyright:   (c) Сергей 2017
# Licence:     Open Source
#-------------------------------------------------------------------------------
# import sys
# from PyQt5 import QtCore, QtWidgets
# from PyQt5.QtGui import QPainter, QColor, QFont
# from PyQt5.QtWidgets import QApplication, QWidget
# from Bukovica   import *
# from Personazhi import *

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import Qt

class Widget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.black)
        painter.drawRect(self.rect())
        painter.setPen(QColor(0xff, 0xff, 0xff))

def main():
    app = QApplication(sys.argv)
    w = Widget()
    w.resize(300, 300)
    w.move(300, 300)
    w.setWindowTitle('Квадрат Малевича')
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()