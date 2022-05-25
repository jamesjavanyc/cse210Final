# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 19:12
# @Author  : Junzhou Liu
# @FileName: player.py
# @Software: PyCharm
from final.infra.color import Color
from final.infra.point import Point
from final.model.actor import Actor


class Player(Actor):
    def __init__(self, game):
        super().__init__()
        self._score = 0
        self.set_text("#")
        self.set_position(Point(450, 570))
        self.set_color(Color(255, 255, 255))
        # observer
        self.observer = game
        self.life = 5
        self.bullet = 10

    def deduct_life(self):
        self.life -= 1

    def get_score(self):
        return self._score

    def add_score(self):
        self.bullet += 10
        self._score += 1

    def deduct_score(self):
        self._score -= 1

    def move_next(self, max_x, max_y):
        x = (self._position.get_x() + self._velocity.get_x())
        y = (self._position.get_y() + self._velocity.get_y())
        if x >= max_x - 15:
            x = max_x -15
        if x < 15:
            x = 15
        if y >= max_y - 15:
            y = max_y - 15
        if y < 15:
            y = 15
        self._position = Point(x, y)
