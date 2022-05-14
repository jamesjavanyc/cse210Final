# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 19:12
# @Author  : Junzhou Liu
# @FileName: player.py
# @Software: PyCharm
from github.greedy.infra.color import Color
from github.greedy.infra.point import Point
from github.greedy.model.actor import Actor


class Player(Actor):
    def __init__(self, game):
        super().__init__()
        self._score = 0
        self.set_text("#")
        self.set_position(Point(450, 585))
        self.set_color(Color(255, 255, 255))
        # observer
        self.observer = game

    def get_score(self):
        return self._score

    def add_score(self):
        self._score += 1

    def deduct_score(self):
        self._score -= 1
        # observer mode
        if self._score < 0:
            self.observer.stop()
