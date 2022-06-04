# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 0:02
# @Author  : Junzhou Liu
# @FileName: keyboard_action.py
# @Software: PyCharm
from final.script.action import Action


class KeyboardAction(Action):
    # handle input
    def execute(self, cast, script):
        game = cast["final_project"]
        velocity = game.keyboard_service.get_dir(cast)
        game.player.set_velocity(velocity)
        game.player.move_next(900, 600)
        for bullet in cast["bullet"]:
            bullet.move_next(900, 600)