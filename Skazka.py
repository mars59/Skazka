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
from Bukovica   import *
from Personazhi import *
from PyQt5 import QtCore

def main():
    print('Проект просто "Сказка"')
    print('PYQT_VERSION = ', QtCore.PYQT_VERSION_STR)
    print('QT_VERSION = ', QtCore.QT_VERSION_STR)
    # a = Азбука()
    # a.изображение = 'Сто'
    # print(a.изображение)
    # a = Азъ()
    # b = Боги()
    # k = Кащей()

if __name__ == '__main__':
    main()