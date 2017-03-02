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

# pyuic5.bat AzbukaWidget.ui -o ui_AzbukaWidget.py

from Bukovica   import *
# from Personazhi import *

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap

app = QtWidgets.QApplication(sys.argv)  # Создаем объект приложения
window = QtWidgets.QWidget()  # Создаем объект окна
window.setWindowTitle("Азбука Буквица")
window.resize(300, 300)  # Задаем минимальные размеры (клиентской области) окна (ширина и высота)

азбука = Азбука()

btnQuit = QtWidgets.QPushButton("&Закрыть окно", window)  # Создаем объект кнопки; Alt+З - горячая клавиша
labTitle = QtWidgets.QLabel("<center>Азбука Буквица")
pixmap = QPixmap(азбука.файл_c_изображением)
lblPicture = QtWidgets.QLabel()
lblPicture.setPixmap(pixmap)
lblGuide = QtWidgets.QLabel("<center>Что мы знаем об азбуке Буквица?")
textBrowser = QtWidgets.QTextBrowser()
textBrowser.append(азбука.описание)

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(btnQuit)
vbox.addWidget(labTitle)
vbox.addWidget(lblPicture)
vbox.addWidget(lblGuide)
vbox.addWidget(textBrowser)
window.setLayout(vbox)

btnQuit.clicked.connect(app.quit)  # Завершение выполнения программы

window.show()

sys.exit(app.exec_())