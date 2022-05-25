# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 1:00
# @Author  : Junzhou Liu
# @FileName: bullet.py
# @Software: PyCharm
from final.infra.point import Point
from final.model.actor import Actor


class Bullet(Actor):
    def __init__(self):
        super().__init__()
        self.set_text(".")
        self.set_velocity(Point(0, 15))

    def move_next(self, max_x, max_y):
        x = (self._position.get_x() + self._velocity.get_x())
        y = (self._position.get_y() + self._velocity.get_y())
        if x >= max_x or x <0:
            x = -100
        if y >= max_y or y < 0:
            y = -100
        self._position = Point(x, y)

