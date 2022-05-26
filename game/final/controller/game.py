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

from game.final.controller.game_manager import GameManager


class Game:

    # integration the attribute of the game
    def __init__(self, keyboard_service, video_service):
        self.game_manager = GameManager().init_game(self, keyboard_service, video_service)

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
        # os.system("pause")
        self.video_service.close_window()
