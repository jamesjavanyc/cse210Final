# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 19:35
# @Author  : Junzhou Liu
# @FileName: game.py
# @Software: PyCharm
import os

from final.infra.color import Color
from final.infra.point import Point
from final.model.actor import Actor
from final.model.cage import Cage
from final.model.player import Player

from final.script.collision_action import CollisionAction
from final.script.end_action import EndAction
from final.script.keyboard_action import KeyboardAction
from final.script.scripts import Scripts
from final.script.video_action import VideoAction


class Game:
    # integration the attribute of the game
    def __init__(self, keyboard_service, video_service):
        self.is_on = True
        self.video_service = video_service
        self.keyboard_service = keyboard_service
        self.cast = Cage().get_cage()
        self.player = Player(self)
        self.banner_score = Actor()
        self.banner_score.set_font_size(15)
        self.banner_score.set_color(Color(255, 255, 255))
        self.banner_score.set_position(Point(15, 0))
        self.banner_life = Actor()
        self.banner_life.set_font_size(15)
        self.banner_life.set_color(Color(255, 255, 255))
        self.banner_life.set_position(Point(800, 0))
        self.banner_bu = Actor()
        self.banner_bu.set_font_size(15)
        self.banner_bu.set_color(Color(255, 255, 255))
        self.banner_bu.set_text(f"Bullet: {self.player.bullet}")
        self.banner_bu.set_position(Point(400, 0))
        self.cast["game"] = self
        self.cast["bullet"] = []
        self.scripts = Scripts()
        self.scripts.add_action("input", KeyboardAction())
        self.scripts.add_action("output", VideoAction())
        self.scripts.add_action("update", CollisionAction())
        self.scripts.add_action("end", EndAction())

    def start(self):
        self.video_service.open_window()
        while self.video_service.is_window_open():
            for action in self.scripts.get_actions(""):
                action.execute(self.cast, self.scripts)
            if not self.is_on:
                # for last output
                for action in self.scripts.get_actions(""):
                    action.execute(self.cast, self.scripts)
                break
        os.system("pause")
        self.video_service.close_window()
