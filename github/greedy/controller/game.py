# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 19:35
# @Author  : Junzhou Liu
# @FileName: game.py
# @Software: PyCharm
import os

from github.greedy.infra.color import Color
from github.greedy.infra.point import Point
from github.greedy.model.actor import Actor
from github.greedy.model.cage import Cage
from github.greedy.model.player import Player


class Game:
    # integration the attribute of the game
    def __init__(self, keyboard_service, video_service):
        self.video_service = video_service
        self.keyboard_service = keyboard_service
        self.cage = Cage().get_cage()
        self.player = Player(self)
        self.banner = Actor()
        self.banner.set_font_size(15)
        self.banner.set_color(Color(255, 255, 255))
        self.banner.set_position(Point(15, 0))

    def start(self):
        self.video_service.open_window()
        while self.video_service.is_window_open():
            self._get_inputs()
            self._do_outputs()
            self._do_updates()
        self.video_service.close_window()

    def stop(self):
        # Exceeding
        self.banner.set_text("Game Over")
        self.banner.set_font_size(55)
        self.banner.set_color(Color(255, 255, 255))
        self.banner.set_position(Point(250, 250))
        self._do_outputs()
        os.system("pause")
        self.video_service.close_window()

    def _get_inputs(self):
        velocity = self.keyboard_service.get_dir()
        self.player.set_velocity(velocity)
        self.player.move_next(900, 600)
        # print(self.player.get_position().get_x(), self.player.get_position().get_y())

    def _do_outputs(self):
        # screen output
        self.video_service.clear_buffer()
        for _ in self.cage:
            self.video_service.draw_actors(self.cage)
        self.video_service.draw_actor(self.banner)
        self.video_service.draw_actor(self.player)
        self.video_service.flush_buffer()

    def _do_updates(self):
        banner = self.banner
        banner.set_text(f"Score: {self.player.get_score()}")

        max_x = self.video_service.get_width()
        max_y = self.video_service.get_height()

        all_robot = list()
        for i in self.cage.get("*"):
            all_robot.append(i)
        for i in self.cage.get("o"):
            all_robot.append(i)
        for item in all_robot:
            item.move_next(max_x, max_y)
            if self.player.get_position().equals(item.get_position()):
                if item.get_text() == "*":
                    self.player.add_score()
                else:
                    self.player.deduct_score()
