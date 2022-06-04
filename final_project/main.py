# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 18:38
# @Author  : Junzhou Liu
# @FileName: main.py
# @Software: PyCharm
import os

from final.controller.controller import Controller
from final.view.keyboard import KeyboardService
from final.view.video import VideoService


def main():
    # start the final_project
    controller = Controller(KeyboardService(15), VideoService("Final", 900, 600, 15, 12))
    print("success init controller")
    controller.start_game()


if __name__ == '__main__':
    main()
