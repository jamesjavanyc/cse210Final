title:Greedy
description:Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!
project structure: This project is in 4 parts, controller, infra, model, view
    The main.py is the client for customers
    controller package, including the controller of the game and the game.py which assumbled all the other parts in the game
    infra: the basic tool which organize the color and piont in the game
    model: it includes all the models for the game, like rock, player and star
    view, including the interaction between game and player, control the keyboard and video service.
exceeding: The class player use a simple observer that could control the game when the score is below 0, the object could inform the game to stop.
required software: Python 3, Raylib
developer: Junzhou Liu a3477075861@gmail.com
