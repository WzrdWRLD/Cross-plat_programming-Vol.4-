#!/usr/bin/env python3
# coding=utf-8

import sys

from random import randint
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


# Основной класс программы
class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('Form.ui', self)  # Загрузка формы из файла

        # Задание заголовка окна
        self.setWindowTitle('Разработка кроссплатформенных приложений')

        self.pushButton_run.clicked.connect(self.run)
        self.pushButton_random.clicked.connect(self.random)


    def random(self):
        row = 0
        col = 0
        while row < self.tableWidget_array.rowCount():
            while col < self.tableWidget_array.columnCount():
                random_num = randint(0, 100)
                self.tableWidget_array.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0


    def run(self):
        fm = self.find_max()
        print(fm)
        if fm == None:
            self.label_max.setText('Введены некорректные данные!')
        else:
            s_col = self.my_sum()
            if s_col == None:
                self.label_max.setText('Введены некорректные данные!')
            else:
                self.label_max.setText(
                        'Максимальный элемент: ' + str(fm[0])  + '[1, '+ str(fm[1]) + ']')
                self.label_sum.setText(
                        'Сумма элементов второго столбца: ' + str(s_col))
                self.tableWidget_array.setItem(1, fm[1], QTableWidgetItem(str(s_col)))


    def find_max(self):
        pos_max = 0
        max_num = 0
        column = 0
        try:
            while column < self.tableWidget_array.columnCount():
                number = float(self.tableWidget_array.item(1, column).text())
                if number > max_num:
                    max_num = number
                    pos_max = column
                column += 1
            return [max_num, pos_max]
        except Exception:
            return None


    def my_sum(self):
        row = 0
        numb_sum = 0
        try:
            while row < self.tableWidget_array.rowCount():
                numb_sum += float(self.tableWidget_array.item(row, 1).text())
                row += 1
            return numb_sum
        except Exception:
            return None

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()