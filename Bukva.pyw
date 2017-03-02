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
window.setWindowTitle("Буквы азбуки Буквица")
window.resize(300, 500)  # Задаем минимальные размеры (клиентской области) окна (ширина и высота)

азбука = Азбука()

# Названия кнопок
names = ['Азъ', 'Боги', 'Веди', 'Глаголи', 'Добро', 'Есть', 'Есмь',
         'Жизнь', 'Дзело', 'Земля', 'Иже', 'Ижеи', 'Инить', 'Гервь',
         'Како', 'Людие', 'Мыслете', 'Наш', 'Оно', 'Покои', 'Реци',
         'Слово', 'Твердо', 'Ук', 'Оук', 'Ферт', 'Хиер', 'От',
         'Ци', 'Червль', 'Ша', 'Шта', 'Еръ', 'Еры', 'Ерь',
         'Ять', 'Юнь', 'Арь', 'Эдо', 'Ом', 'Енъ', 'Оде',
         'Ёта', 'Ота', 'Кси', 'Пси', 'Фита', 'Ижица', 'Ижа']

dict = []
num = -1
with open('Znachenie_bukvits.txt', 'r', encoding='utf-8') as file_object:
    for line in file_object:
        s = line.rstrip()
        if '***' in s:
            num += 1
            dict.append('')
        else:
            if dict[num] == '':
                dict[num] = s
            else:
                dict[num] = dict[num] + '\n' + s

class ClassButtonClick():
    def __init__(self, num = 0):
        self.num = num
    def __call__(self):
        textBrowser.clear()
        if self.num < len(dict)-1:
            textBrowser.append(dict[self.num])

grid = QtWidgets.QGridLayout()

# Создаём список позиций для сетки
positions = [(i,j) for i in range(7) for j in range(7)]

# Создаем и добавляем кнопки в макет
obj = ClassButtonClick()
p = 0
for position, name in zip(positions, names):
    button = QtWidgets.QPushButton(name)
    p += 1
    s = str(p)
    button.objectName = s
    # button.icon()
    button.setCheckable(True)
    # button.resize(button.sizeHint()) # Метод sizeHint() дает рекомендуемый размер для кнопки.
    button.setToolTip(name)
    button.clicked.connect(ClassButtonClick(p))
    grid.addWidget(button, *position)

btnQuit = QtWidgets.QPushButton("&Закрыть окно", window)  # Создаем объект кнопки; Alt+З - горячая клавиша
labTitle = QtWidgets.QLabel("<center>Буквы азбуки Буквица")
pixmap = QPixmap(азбука.файл_c_изображением)
lblPicture = QtWidgets.QLabel()
lblPicture.setPixmap(pixmap)
lblGuide = QtWidgets.QLabel("<center>Что мы знаем о букве?")
textBrowser = QtWidgets.QTextBrowser()

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(btnQuit)
vbox.addWidget(labTitle)
vbox.addLayout(grid)
vbox.addWidget(lblGuide)
vbox.addWidget(textBrowser)
window.setLayout(vbox)

btnQuit.clicked.connect(app.quit)  # Завершение выполнения программы

window.show()

sys.exit(app.exec_())