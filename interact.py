# -*- coding: utf-8 -*-

from core import translate

if __name__ == "__main__":
    while True:
        text = input('Text >>')
        lang = input('Target Lang >>')
        print(translate(text, lang))
