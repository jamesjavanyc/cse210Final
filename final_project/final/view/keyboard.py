# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 18:46
# @Author  : Junzhou Liu
# @FileName: keyboard.py
# @Software: PyCharm
import pyray

from final.infra.point import Point
from final.view.keyboard_interface import KeyboardInterface

from final.model.bullet import Bullet


class KeyboardService(KeyboardInterface):
    """
    keyboard service, detect the key that player input
    """
    def __init__(self, cell_size=1):
        # cell size in display grid
        self.cell_size = cell_size

    def get_dir(self, cast):
        # get the direction
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
            # print("left")

        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1
            # print("right")

        if pyray.is_key_down(pyray.KEY_UP):
            dy = -1

        if pyray.is_key_down(pyray.KEY_DOWN):
            dy = 1

        if pyray.is_key_down(pyray.KEY_W) and cast["final_project"].player.bullet >= 1:
            bullet = Bullet()
            bullet.set_text(".")
            bullet.set_position(Point(cast["final_project"].player.get_position().get_x(), cast["final_project"].player.get_position().get_y() + 20))
            cast["bullet"].append(bullet)
            cast["final_project"].player.bullet -= 1
            game = cast["final_project"]
            game.banner_bu.set_text(f"Bullet: {game.player.bullet}")
        direction = Point(dx, dy)
        direction = direction.scale(self.cell_size)

        return direction
