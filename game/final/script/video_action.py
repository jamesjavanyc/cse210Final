# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 0:07
# @Author  : Junzhou Liu
# @FileName: video_action.py
# @Software: PyCharm
from final.script.action import Action


class VideoAction(Action):
    def execute(self, cast, script):
        # screen output
        game = cast.get("game")
        game.banner_bu.set_text(f"Bullet: {game.player.bullet}")
        game.video_service.clear_buffer()
        for _ in game.cast:
            game.video_service.draw_actors(game.cast)
        game.video_service.draw_actor(game.banner_score)
        game.video_service.draw_actor(game.banner_bu)
        game.video_service.draw_actor(game.banner_life)
        game.video_service.draw_actor(game.player)
        game.video_service.flush_buffer()