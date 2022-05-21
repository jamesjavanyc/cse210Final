# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 18:46
# @Author  : Junzhou Liu
# @FileName: keyboard.py
# @Software: PyCharm
import pyray

from greedy.infra.point import Point


class KeyboardService:
    """
    keyboard service, detect the key that player input
    """
    def __init__(self, cell_size=1):
        # cell size in display grid
        self.cell_size = cell_size

    def get_dir(self):
        # get the direction
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
            # print("left")

        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1
            # print("right")

        """if pyray.is_key_down(pyray.KEY_UP):
            dy = -1

        if pyray.is_key_down(pyray.KEY_DOWN):
            dy = 1"""

        direction = Point(dx, dy)
        direction = direction.scale(self.cell_size)

        return direction
