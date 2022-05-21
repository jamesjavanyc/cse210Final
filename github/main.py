# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 18:38
# @Author  : Junzhou Liu
# @FileName: main.py
# @Software: PyCharm
from greedy.controller.controller import Controller
from greedy.view.keyboard import KeyboardService
from greedy.view.video import VideoService

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40


def main():
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService("Greedy", MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    controller = Controller(keyboard_service, video_service)
    controller.start_game()


if __name__ == '__main__':
    main()
