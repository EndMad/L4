#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Определить порядковые номера
# первой пары одинаковых соседних символов.
# Если таких символов нет,
# то должно быть напечатано соответствующее сообщение.

if __name__ == '__main__':
    line = input("Введите предложение ")
    for ind in range(len(line) - 1):
        if line[ind] == line[ind + 1]:
            print(ind + 1, ind + 2)
            break
        else:
            print('Таких нет')
