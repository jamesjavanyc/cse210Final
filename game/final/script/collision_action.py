# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 23:39
# @Author  : Junzhou Liu
# @FileName: collision_action.py
# @Software: PyCharm
import random

from final.infra.point import Point
from final.model.alies import Alies
from final.model.enemy import Enemy
from final.script.action import Action


class CollisionAction(Action):
    """handle aircraft crush"""
    def execute(self, cast, script):
        game = cast.get("game")
        banner_score = game.banner_score
        banner_score.set_text(f"Score: {game.player.get_score()}")
        banner_life = game.banner_life
        banner_life.set_text(f"Life: {game.player.life}")
        max_x = game.video_service.get_width()
        max_y = game.video_service.get_height()
        all_robot = list()
        for i in game.cast.get("*"):
            all_robot.append(i)
        for i in game.cast.get("o"):
            all_robot.append(i)
        for i in game.cast.get("bullet"):
            if i.get_position().get_x() > 900 or i.get_position().get_x() <0 or i.get_position().get_y() > 600 or i.get_position().get_y() <0:
                game.cast.get("bullet").remove(i)
                continue
            for rob in all_robot:
                if i.get_position().hit(rob.get_position()):
                    cast[rob.get_text()].remove(rob)
                    if i in game.cast.get("bullet"):
                        game.cast.get("bullet").remove(i)
                    game.player.add_score()
                i.move_next(max_x, max_y)
        # collision with flight
        for item in all_robot:
            item.move_next(max_x, max_y)
            if game.player.get_position().equals(item.get_position()):
                if item.get_text() == "*":
                    game.player.add_score()
                    if item in cast["*"]:
                        cast["*"].remove(item)
                    alies = Alies()
                    alies.set_position(Point(random.randint(0, 900), 0))
                    cast["*"].append(alies)
                    game.player.deduct_life()
                else:
                    game.player.deduct_score()
                    banner_score.set_text(item.get_message())
                    if item in cast["o"]:
                        cast["o"].remove(item)
                    enemy = Enemy()
                    enemy.set_position(Point(random.randint(0, 900), 0))
                    cast["o"].append(enemy)
                    game.player.deduct_life()


