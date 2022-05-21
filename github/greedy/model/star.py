# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 19:12
# @Author  : Junzhou Liu
# @FileName: star.py
# @Software: PyCharm
from greedy.model.actor import Actor
from greedy.infra.point import Point


class Star(Actor):
    def __init__(self):
        super().__init__()
        self.set_text("*")
        self.set_velocity(Point(0, 1))
