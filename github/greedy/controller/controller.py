# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 19:34
# @Author  : Junzhou Liu
# @FileName: controller.py
# @Software: PyCharm
from greedy.controller.game import Game


class Controller:
    # main controller for the game
    def __init__(self, keyboard_service, video_service):
        self.game = Game(keyboard_service, video_service)

    def start_game(self):
        self.game.start()
