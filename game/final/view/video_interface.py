# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 23:29
# @Author  : Junzhou Liu
# @FileName: video_interface.py
# @Software: PyCharm


class VideoInterface:

    def close_window(self):
        raise NotImplementedError("not implemented in base class")

    def clear_buffer(self):
        raise NotImplementedError("not implemented in base class")

    def draw_actor(self, actor):
        raise NotImplementedError("not implemented in base class")

    def draw_actors(self, actors):
        raise NotImplementedError("not implemented in base class")

    def flush_buffer(self):
        raise NotImplementedError("not implemented in base class")
    def get_cell_size(self):
        raise NotImplementedError("not implemented in base class")

    def get_height(self):
        raise NotImplementedError("not implemented in base class")

    def get_width(self):
        raise NotImplementedError("not implemented in base class")

    def is_window_open(self):
        raise NotImplementedError("not implemented in base class")

    def open_window(self):
        raise NotImplementedError("not implemented in base class")

    def _draw_grid(self):
        raise NotImplementedError("not implemented in base class")
