# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Bukva
# Purpose: Изучение рукв алфавита Буквица
#
# Authors:      Марков Сергей, Артём Вишногор, Анастасия Вишногорская
#
# Created:     22.02.2017
# Copyright:   (c) Сергей 2017
# Licence:     Open Source
#-------------------------------------------------------------------------------

# pyuic5.bat AzbukaWidget.ui -o ui_AzbukaWidget.py

from Bukovica import *

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QSize

app = QtWidgets.QApplication(sys.argv)  # Создаем объект приложения
window = QtWidgets.QWidget()  # Создаем объект окна
window.setWindowTitle("Буквы азбуки Буквица")
ico = QIcon('icon.png')
window.setWindowIcon(ico) # Значок окна
app.setWindowIcon(ico)    # Значок приложения
window.resize(300, 900)   # Задаем минимальные размеры (клиентской области) окна (ширина и высота)

pal = window.palette()
pal.setColor(QtGui.QPalette.Normal,   QtGui.QPalette.Window, QtGui.QColor("#618760"))
pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QColor("#618760"))
window.setPalette(pal)

азбука = Азбука()

numButton = 0 # Номер активной кнопки

# Названия кнопок
names = ['Азъ', 'Боги', 'Веди', 'Глаголи', 'Добро', 'Есть', 'Есмь',
         'Жизнь', 'Дзело', 'Земля', 'Иже', 'Ижеи', 'Инить', 'Гервь',
         'Како', 'Людие', 'Мыслете', 'Наш', 'Оно', 'Покои', 'Реци',
         'Слово', 'Твердо', 'Ук', 'Оук', 'Ферт', 'Хиер', 'От',
         'Ци', 'Червль', 'Ша', 'Шта', 'Еръ', 'Еры', 'Ерь',
         'Ять', 'Юнь', 'Арь', 'Эдо', 'Ом', 'Енъ', 'Оде',
         'Ёта', 'Ота', 'Кси', 'Пси', 'Фита', 'Ижица', 'Ижа']

folderNamr = 'images/'

# Считывем имена файлов изображений шрифтов в список
fileName = folderNamr + 'picture_font.txt'
listPictureFont = []
with open(fileName, 'r', encoding='utf-8') as file_object:
    for line in file_object:
        listPictureFont.append(line.rstrip())

pixmap = QPixmap(folderNamr + listPictureFont[numButton])
lblPicture = QtWidgets.QLabel()
lblPicture.setPixmap(pixmap)
lblPicture.setMargin(10)

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

textBrowser = QtWidgets.QTextBrowser()
# textBrowser.setTextBackgroundColor(QtGui.QColor("yellow"))
textBrowser.setStyleSheet("background-color: #E6C6XB;")
textBrowser.setAutoFillBackground(True)
textBrowser.setTextColor(QtGui.QColor("blue"))
textBrowser.setText(dict[numButton])

class ClassButtonClick():
    def __init__(self, num = 0):
        self.num = num
    def __call__(self):
        numButton = self.num
        if numButton < len(dict):
            textBrowser.setText(dict[numButton])
        lblGuide.setText('Что мы знаем о букве "' + names[numButton] + '"?')
        pixmap = QPixmap(folderNamr + listPictureFont[numButton])
        lblPicture.setPixmap(pixmap)

# Матрица кнопок
grid = QtWidgets.QGridLayout()

# Создаём список позиций для сетки
positions = [(i,j) for i in range(7) for j in range(7)]

# Создаем и добавляем кнопки в матрицу кнопок
p = -1
for position, name in zip(positions, names):
    # button = QtWidgets.QPushButton(name)
    button = QtWidgets.QPushButton()
    p += 1
    # s = str(p)
    # button.objectName = s
    button.setIcon(QIcon(folderNamr + listPictureFont[p]))
    button.setIconSize(QSize(40,40))
    button.setCheckable(True)
    button.setToolTip(name)
    button.clicked.connect(ClassButtonClick(p))
    grid.addWidget(button, *position)

def SetColorFon():
    color = QtWidgets.QColorDialog.getColor(
        initial=QtGui.QColor("#ff0000"),
        parent=window, title="Выберите фон окна приложения",
        options=QtWidgets.QColorDialog.ShowAlphaChannel)
    if color.isValid():
        pal = window.palette()
        pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, color)
        pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window, color)
        window.setPalette(pal)

def SetColorText():
    color = QtWidgets.QColorDialog.getColor(
        initial=QtGui.QColor("#ff0000"),
        parent=window, title="Выберите цвет текста",
        options=QtWidgets.QColorDialog.ShowAlphaChannel)
    if color.isValid():
        textBrowser.setTextColor(color)
        textBrowser.setText(dict[numButton])

def SetFont():
    (font, ok) = QtWidgets.QFontDialog.getFont(
        QtGui.QFont("Tahoma", 16), parent=window, caption="Выберите шрифт для текста")
    if ok:
        textBrowser.setFont(font)
        # print(font.family(), font.pointSize(), font.weight(),
        #       font.italic(), font.underline())

labTitle = QtWidgets.QLabel("<center>Буквы азбуки Буквица")
lblGuide = QtWidgets.QLabel("Что мы знаем о букве?")
lblGuide.setAlignment(QtCore.Qt.AlignCenter)
btnColor = QtWidgets.QPushButton("Цвет текста")
btnColor.setToolTip('Устававливаем <b>цвет</b> текста с помощью диалогового окна')
btnColor.clicked.connect(SetColorText)
btnFont = QtWidgets.QPushButton("Шрифт")
btnFont.setToolTip('Устававливаем <b>шрифт</b> текста с помощью диалогового окна')
btnFont.clicked.connect(SetFont)

btnFonColor = QtWidgets.QPushButton("Цвет фона")
btnFonColor.setToolTip('Устававливаем  цвет <b>фона</b> с помощью диалогового окна')
btnFonColor.clicked.connect(SetColorFon)

gridFix = QtWidgets.QHBoxLayout()
gridFix.addLayout(grid)
gridFix.addStretch(0)

gridAndBukva = QtWidgets.QHBoxLayout()
gridAndBukva.addLayout(gridFix)
gridAndBukva.addWidget(lblPicture)
gridAndBukva.addStretch(0)

boxGiudeButton = QtWidgets.QHBoxLayout()
boxGiudeButton.addStretch(0)
boxGiudeButton.addWidget(btnColor)
boxGiudeButton.addWidget(btnFont)

boxGiudeTitle = QtWidgets.QHBoxLayout()
boxGiudeTitle.addWidget(lblGuide)
boxGiudeTitle.addLayout(boxGiudeButton)

boxTitleButton = QtWidgets.QHBoxLayout()
boxTitleButton.addStretch(0)
boxTitleButton.addWidget(btnFonColor)

boxTitle = QtWidgets.QHBoxLayout()
boxTitle.addWidget(labTitle)
boxTitle.addLayout(boxTitleButton)

vbox = QtWidgets.QVBoxLayout()
vbox.addLayout(boxTitle)
vbox.addLayout(gridAndBukva)
vbox.addLayout(boxGiudeTitle)
vbox.addWidget(textBrowser)
window.setLayout(vbox)

window.show()

sys.exit(app.exec_())