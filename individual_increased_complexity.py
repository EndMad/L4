#!/usr/bin/env python3
# -*- coding: utf-8 -*-

word = input("Введите три слова ")

while word:
    if word.count(word[0]) == 1:
        print(word[0], ':', word.count(word[0]))
    word = word.replace(word[0], '')
