import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import main_state
import world_build_state

name = "RankingState"

ranking_board = []

def enter():
    pass

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(main_state)


def update():
    pass

def draw():
    pass
