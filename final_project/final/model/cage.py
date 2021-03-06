# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 20:18
# @Author  : Junzhou Liu
# @FileName: cage.py
# @Software: PyCharm
import random

from final.infra.color import Color
from final.infra.point import Point
from final.model.alies import Alies
from final.model.enemy import Enemy


class Cage:
    def __init__(self):
        self.cage = {"*": list(), "o": list()}
        for _ in range(20):
            text = random.choice(("o", "*"))

            x = random.randint(1, 60 - 1)
            y = random.randint(1, 40 - 1)
            position = Point(x, y)
            position = position.scale(15)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            obj = None
            if text == "o":
                obj = Enemy()
            else:
                obj = Alies()
            obj.set_text(text)
            obj.set_font_size(15)
            obj.set_color(color)
            obj.set_position(position)
            self.cage[text].append(obj)

    def get_cage(self):
        return self.cage
