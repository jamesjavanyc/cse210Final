# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 18:56
# @Author  : Junzhou Liu
# @FileName: video.py
# @Software: PyCharm
import os
import pathlib

import pyray
from final.view.video_interface import VideoInterface


class VideoService(VideoInterface):
    def __init__(self, caption, width, height, cell_size, frame_rate, debug=False):
        self._caption = caption
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._frame_rate = frame_rate
        self._debug = debug

    def close_window(self):
        pyray.close_window()

    def clear_buffer(self):
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()

    def draw_actor(self, actor):
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()
        if text == "o":
            pyray.draw_text("|", x, y, font_size, color)
            pyray.draw_text("-", x - 5, y, font_size, color)
            pyray.draw_text("-", x + 5, y, font_size, color)
            pyray.draw_text("-", x - 15, y, font_size, color)
            pyray.draw_text("-", x + 15, y, font_size, color)
            pyray.draw_text("|", x, y - 5, font_size, color)
            pyray.draw_text("|", x, y + 5, font_size, color)
            pyray.draw_text("|", x, y + 10, font_size, color)
            pyray.draw_text("-", x - 5, y + 13, font_size, color)
            pyray.draw_text("-", x + 5, y + 13, font_size, color)
        elif text == "*":
            pyray.draw_text(text, x, y, font_size, color)
            pyray.draw_text(text, x - 5, y, font_size, color)
            pyray.draw_text(text, x + 5, y, font_size, color)
            pyray.draw_text(text, x - 10, y, font_size, color)
            pyray.draw_text(text, x + 10, y, font_size, color)
            pyray.draw_text(text, x, y - 5, font_size, color)
            pyray.draw_text(text, x, y + 5, font_size, color)
            pyray.draw_text(text, x, y - 10, font_size, color)
            pyray.draw_text(text, x - 5, y - 10, font_size, color)
            pyray.draw_text(text, x + 5, y - 10, font_size, color)
        elif text == "#":
            text = "o"
            pyray.draw_text(text, x, y, font_size, color)
            pyray.draw_text(text, x - 5, y, font_size, color)
            pyray.draw_text(text, x + 5, y, font_size, color)
            pyray.draw_text(text, x - 10, y, font_size, color)
            pyray.draw_text(text, x + 10, y, font_size, color)
            pyray.draw_text(text, x, y - 5, font_size, color)
            pyray.draw_text(text, x, y + 5, font_size, color)
            pyray.draw_text(text, x, y + 10, font_size, color)
            pyray.draw_text(text, x - 5, y + 10, font_size, color)
            pyray.draw_text(text, x + 5, y + 10, font_size, color)
        elif text == ".":
            for i in range(0, 400, 40):
                pyray.draw_text(text, x, y-i, font_size, color)
        else:
            pyray.draw_text(text, x, y, font_size, color)

    def draw_actors(self, actors):
        for en in actors:
            if en == "game":
                continue
            actor_list = actors[en]
            # print("actors")
            # print(actors)
            for actor in actor_list:
                self.draw_actor(actor)

    def flush_buffer(self):
        pyray.end_drawing()

    def get_cell_size(self):
        return self._cell_size

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def is_window_open(self):
        return not pyray.window_should_close()

    def open_window(self):
        pyray.init_window(self._width, self._height, self._caption)
        pyray.set_target_fps(self._frame_rate)

    def _draw_grid(self):
        for y in range(0, self._height, self._cell_size):
            pyray.draw_line(0, y, self._width, y, pyray.GRAY)
        for x in range(0, self._width, self._cell_size):
            pyray.draw_line(x, 0, x, self._height, pyray.GRAY)
