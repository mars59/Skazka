# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Bukva
# Purpose:
#
# Authors:      Марков Сергей, Артём Вишногор, Анастасия Вишногорская
#
# Created:     22.02.2017
# Copyright:   (c) Сергей 2017
# Licence:     Open Source
#-------------------------------------------------------------------------------

from Bukovica import *

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QSize
app = QtWidgets.QApplication(sys.argv)  # Создаем объект приложения
window = QtWidgets.QWidget()  # Создаем объект окна
window.setWindowTitle("Изучает буквы азбуки Буквица")
window.resize(600, 900)  # Задаем минимальные размеры (клиентской области) окна (ширина и высота)

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
        if s == '':
            pass
        elif '***' in s:
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
        lblGuide.setText('Что мы знаем о букве "' + names[self.num] + '"?')

grid1 = QtWidgets.QVBoxLayout()
grid2 = QtWidgets.QVBoxLayout()
grid3 = QtWidgets.QVBoxLayout()

# Считывем имена фвйлов изображений шрифтов в список
# Обычно если Windows, то слеш \, если Linux, то слеш /
fileName = 'images/picture_font.txt'
listPictureFont = []
with open(fileName) as file_object:
    for line in file_object:
        listPictureFont.append(line.rstrip())

# Создаем и добавляем кнопки в макет
p = -1
for name in names:
    p += 1
    button = QtWidgets.QPushButton()
    button.objectName = str(p)
    button.setIcon(QIcon('images/'+listPictureFont[p]))
    button.setIconSize(QSize(20,20))
    button.setCheckable(True)
    button.setToolTip(name)
    button.clicked.connect(ClassButtonClick(p))
    if p < 18:
        grid1.addWidget(button)
    elif p < 35:
        grid2.addWidget(button)
    else:
        grid3.addWidget(button)

grid1.addStretch(0)
grid2.addStretch(0)
grid3.addStretch(0)

grid = QtWidgets.QHBoxLayout()
grid.addLayout(grid1)
grid.addLayout(grid2)
grid.addLayout(grid3)

btnQuit = QtWidgets.QPushButton("&Закрыть окно", window)  # Создаем объект кнопки; Alt+З - горячая клавиша
labTitle = QtWidgets.QLabel("<center>Изображение буквы")
pixmap = QPixmap('images/'+'1.png')
lblPicture = QtWidgets.QLabel()
lblPicture.setPixmap(pixmap)
lblGuide = QtWidgets.QLabel("Что мы знаем о букве?")
lblGuide.setAlignment(QtCore.Qt.AlignCenter)
textBrowser = QtWidgets.QTextBrowser()

DefLayout1 = QtWidgets.QVBoxLayout()
DefLayout1.addWidget(labTitle)
DefLayout1.addWidget(lblPicture, stretch=0, alignment=QtCore.Qt.AlignJustify)

DefLayout2 = QtWidgets.QVBoxLayout()
DefLayout2.addWidget(lblGuide)
DefLayout2.addWidget(textBrowser)

DefLayout = QtWidgets.QVBoxLayout()
DefLayout.addLayout(DefLayout1)
DefLayout.addLayout(DefLayout2)

workLayout = QtWidgets.QHBoxLayout()
workLayout.addLayout(grid)
workLayout.addLayout(DefLayout)

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(btnQuit)
vbox.addLayout(workLayout)

window.setLayout(vbox)

btnQuit.clicked.connect(app.quit)  # Завершение выполнения программы

window.show()

sys.exit(app.exec_())