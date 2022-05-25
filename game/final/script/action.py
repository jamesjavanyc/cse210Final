# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 23:38
# @Author  : Junzhou Liu
# @FileName: action.py
# @Software: PyCharm
class Action:
    def execute(self, cast, script):
        raise NotImplementedError("execute not implemented in base class")