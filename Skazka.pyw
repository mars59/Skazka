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

import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

app = QtWidgets.QApplication(sys.argv)  # Создаем объект приложения
window = QtWidgets.QWidget()  # Создаем объект окна
window.setWindowTitle("Макет программы Сказка. Навигация.")
window.resize(300, 500)  # Задаем минимальные размеры (клиентской области) окна (ширина и высота)

btnQuit = QtWidgets.QPushButton("&Закрыть окно")  # Создаем объект кнопки; Alt+З - горячая клавиша

btnQuit.clicked.connect(app.quit)  # Завершение выполнения программы

pixmap1 = QPixmap('Азбука.png')
lblPicture1 = QtWidgets.QLabel()
lblPicture1.setPixmap(pixmap1)

pixmap2 = QPixmap('Буквы.png')
lblPicture2 = QtWidgets.QLabel()
lblPicture2.setPixmap(pixmap2)

tab = QtWidgets.QTabWidget()
tab.addTab(lblPicture1, "Азбука")
tab.addTab(lblPicture2, "Буквы")
tab.addTab(QtWidgets.QLabel("<center>Здесь будут создаваться слова с помощью клавиатуры"), "Клавиатура")
tab.addTab(QtWidgets.QLabel("<center>Здесь будут создаваться и настраиваться персонажи"), "Персонажи")
tab.addTab(QtWidgets.QLabel("<center>Здесь персонажи будут взаимодействовать в смысловом поле"), "Сказка")
tab.addTab(QtWidgets.QLabel("<center>Здесь будет какая-нибудь мини игра"), "Мини игра")
tab.setCurrentIndex(0)

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(btnQuit)
vbox.addWidget(tab)

window.setLayout(vbox)

window.show()

sys.exit(app.exec_())