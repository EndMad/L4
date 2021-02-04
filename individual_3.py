#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дана строка. Удалить из нее все пробелы.

if __name__ == '__main__':
    s = input("Введите предложение ")
    s = ''.join(s.split())
    print(s)
