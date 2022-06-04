# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 0:23
# @Author  : Junzhou Liu
# @FileName: end_action.py
# @Software: PyCharm
import os

from final.infra.color import Color
from final.infra.point import Point
from final.script.action import Action


class EndAction(Action):
    def execute(self, cast, script):
        game = cast["final_project"]
        if game.player.get_score() < 0 or game.player.life <= 0:
            # Exceeding observer
            game.banner_score.set_text("Game Over")
            game.banner_score.set_font_size(55)
            game.banner_score.set_color(Color(255, 255, 255))
            game.banner_score.set_position(Point(250, 250))
            game.is_on = False
