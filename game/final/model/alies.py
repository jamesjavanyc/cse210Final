# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 19:12
# @Author  : Junzhou Liu
# @FileName: alies.py
# @Software: PyCharm
from final.model.actor import Actor
from final.infra.point import Point


class Alies(Actor):
    def __init__(self):
        super().__init__()
        self.set_text("*")
        self.set_velocity(Point(0, 10))
