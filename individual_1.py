#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Вывести «столбиком» все его буквы и,
# стоящие на четных местах.

print("Введите предложение")
print(
    *(letter for i,
        letter in enumerate(input()) if letter == "и" and not i % 2),
    sep="\n"
)
