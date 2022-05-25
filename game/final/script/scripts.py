# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 0:31
# @Author  : Junzhou Liu
# @FileName: scripts.py
# @Software: PyCharm
from final.script.script import Script


class Scripts(Script):
    # extending script
    def __init__(self):
        self.ordered_group = []
        super().__init__()

    def add_action(self, group, action):
        self.ordered_group.append(group)
        super().add_action(group, action)

    # nullable
    def get_actions(self, group):
        results = []
        for group in self.ordered_group:
            if group in self._actions.keys():
                for action in self._actions[group]:
                    results.append(action)
        return results