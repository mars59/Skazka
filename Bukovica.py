# -*- coding: utf-8 -*-
# #-------------------------------------------------------------------------------
# Name:        Bukovica
# Purpose:
#
# Authors:      Марков Сергей, Артём Вишногор, Анастасия Вишногорская
#
# Created:     01.03.2017
# Copyright:   (c) Сергей 2017
# Licence:     Open Source
#-------------------------------------------------------------------------------

"""
Руский язык – изменение Буквицы
http://fizrazvitie.ru/2011/03/russkij-yazyk-izmenenie-bukvicy.html
Древлесловенская Буквица
http://derzhavarus.ru/bukvica-tablica.html
Древнеруский язык
http://derzhavarus.ru/drevneruskij-jazyk-soderzhanie
"""

class Азбука:
    """Описание азбуки"""

    изображение_азбуки = ""
    описание_азбуки = "" #"Здесь будет описание важности и нужности алфавита Буквицы для современного человека."
    файл_c_изображением = "bukvica_alfavit.jpg"
    файл_c_описанием = "BukvicaGuide.txt"

    def __init__(self):
        # Загружаем изображение из файла
        try:
            self.изображение_азбуки = open(self.файл_c_изображением, 'rb').read()
        except:
            print('Файл "' + self.файл_c_изображением + '" с избражением для Азбуки не найден!')

        try:
            self.описание_азбуки = open(self.файл_c_описанием, 'r', encoding='utf-8').read()
        except:
            print('Файл "' + self.файл_c_описанием + '" с описанием Азбуки не найден!')

        # print('Объект Азбука создан')

class Буквица:
    """Базвый класс для всех букв алфавита"""

    буква = ''
    цифра = None
    изображение = ''
    файл_c_изображением = ''
    описание = ''

    def __init__(self):
        # Загружаем изображение из файла
        try:
            self.изображение = open(self.файл_c_изображением, 'rb').read()
        except:
            print('Файл "' + self.файл_c_изображением + '" с избражением для буквы', self.буква, 'не найден!')

class Азъ(Буквица):
    """Описание буквицы Азъ"""

    файл_c_изображением = "Оук.png"

    def __init__(self):
        self.буква = 'Азъ'
        self.цифра = 1
        self.файл_c_изображением = '' # TODO Заполнить
        self.описание = ''            # TODO Заполнить
        Буквица.__init__(self)

class Боги(Буквица):
    """Описание буквицы Азъ"""

    def __init__(self):
        self.буква = 'Боги'
        self.цифра = None
        self.файл_c_изображением = '' # TODO Заполнить
        self.описание = ''            # TODO Заполнить
        Буквица.__init__(self)
