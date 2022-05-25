# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 19:11
# @Author  : Junzhou Liu
# @FileName: rock.py
# @Software: PyCharm
from final.model.actor import Actor
from final.infra.point import Point


class Enemy(Actor):
    def __init__(self):
        super().__init__()
        self.set_text("o")
        self.set_velocity(Point(0, -2))

    def get_message(self):
        return "You hit!"
