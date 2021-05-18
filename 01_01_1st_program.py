#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Импорт библиотек, необходимых для работы
# Для сложных математических расчетов:
import math
# Массивы и операции для работы с ними:
import numpy
# Графическое представление вычислений:
import matplotlib.pyplot as mpp

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':
    arguments = numpy.r_[0:200:0.1]  #точки от 0 до 200 с шагом 0.1
    mpp.plot(   #соединяет точки линией
        arguments,
        [math.cos(a) * math.tan(a/2.0) for a in arguments]  #функция
    )
    mpp.show()  #выводит график
