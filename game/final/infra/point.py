# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 19:14
# @Author  : Junzhou Liu
# @FileName: point.py
# @Software: PyCharm
class Point:
    # point on the screen, object to save the information

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def add(self, other):
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        if other.get_x() + 45 > self.get_x() > other.get_x() - 45 and other.get_y() + 45 > self.get_y() > other.get_y() -45:
            return True
        else:
            return False

    def hit(self, other):
        if other.get_x() + 60 > self.get_x() > other.get_x() -60 and other.get_y() + 100 > self.get_y() > other.get_y() - 600:
            return True
        else:
            return False

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def scale(self, factor):
        return Point(self._x * factor, self._y * factor)

