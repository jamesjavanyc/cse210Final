# -*- coding: utf-8 -*-
# @Time    : 2022/5/26 18:42
# @Author  : Junzhou Liu
# @FileName: game_manager.py
# @Software: PyCharm
from final.infra.color import Color
from final.infra.point import Point
from final.model.actor import Actor
from final.model.cage import Cage
from final.model.player import Player
from final.script.action_callback import ActionCallback
from final.script.collision_action import CollisionAction
from final.script.end_action import EndAction
from final.script.keyboard_action import KeyboardAction
from final.script.scripts import Scripts
from final.script.video_action import VideoAction


class GameManager(ActionCallback):
    def init_game(self, game, keyboard_service, video_service ):
        game.is_on = True
        game.video_service = video_service
        game.keyboard_service = keyboard_service
        game.cast = Cage().get_cage()
        game.player = Player(game)
        game.banner_score = Actor()
        game.banner_score.set_font_size(15)
        game.banner_score.set_color(Color(255, 255, 255))
        game.banner_score.set_position(Point(15, 0))
        game.banner_life = Actor()
        game.banner_life.set_font_size(15)
        game.banner_life.set_color(Color(255, 255, 255))
        game.banner_life.set_position(Point(800, 0))
        game.banner_bu = Actor()
        game.banner_bu.set_font_size(15)
        game.banner_bu.set_color(Color(255, 255, 255))
        game.banner_bu.set_text(f"Bullet: {game.player.bullet}")
        game.banner_bu.set_position(Point(400, 0))
        game.cast["final_project"] = game
        game.cast["bullet"] = []
        game.scripts = Scripts()
        game.scripts.add_action("input", KeyboardAction())
        game.scripts.add_action("output", VideoAction())
        game.scripts.add_action("update", CollisionAction())
        game.scripts.add_action("end", EndAction())
