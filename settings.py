"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the game settings that include the association of the
inputs with an their ids, constants of values to set up the game, sounds,
textures, frames, and fonts.
"""

import pathlib

import pygame

from gale import frames
from gale import input_handler

from src import loaders

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, "quit")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_p, "pause")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RETURN, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_KP_ENTER, "enter")

# Player 1
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_d, "move_right")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_a, "move_left")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_w, "move_up")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_s, "move_down")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_e, "attack")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_SPACE, "jump")


# Player 2
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_KP6, "move_right_p2")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_KP4, "move_left_p2")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_KP8, "move_up_p2")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_KP5, "move_down_p2")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_KP7, "attack_p2")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_KP0, "jump_p2")

# Size we want to emulate
VIRTUAL_WIDTH = 400
VIRTUAL_HEIGHT = 192

# Size of our actual window
WINDOW_WIDTH = VIRTUAL_WIDTH * 4
WINDOW_HEIGHT = VIRTUAL_HEIGHT * 4

PLAYER_SPEED = 80

GRAVITY = 980

NUM_LEVELS = 6

BASE_DIR = pathlib.Path(__file__).parent

# player direction
RIGHT = 0
LEFT = 1

LevelLoader = loaders.TmxLevelLoader

TEXTURES = {
    "tiles": pygame.image.load(BASE_DIR / "assets" / "textures" / "tileset.png"),
    "steamMan": pygame.image.load(BASE_DIR / "assets" / "textures" / "SteamMan.png"),
    "robber": pygame.image.load(BASE_DIR / "assets" / "textures" / "GraveRobber.png"),
    "creatures": pygame.image.load(BASE_DIR / "assets" / "textures" / "creatures.png"),
    "girl": pygame.image.load(BASE_DIR / "assets" / "textures" / "Girl_Idle.png"),
    "key-gold": pygame.image.load(BASE_DIR / "assets" / "textures" / "key-gold.png"),
    "jungle_bg": pygame.image.load(BASE_DIR / "assets" / "textures" / "Background.png"),
    "game_over_bg": pygame.image.load(BASE_DIR / "assets" / "textures" / "game_over_bg.png"),
    "blue_bg": pygame.image.load(BASE_DIR / "assets" / "textures" / "Blue_bg.png"),
}

FRAMES = {
    "tiles": frames.generate_frames(TEXTURES["tiles"], 32, 32),
    "steamMan": frames.generate_frames(TEXTURES["steamMan"], 31, 37),
    "robber": frames.generate_frames(TEXTURES["robber"], 28, 43),
    "creatures": frames.generate_frames(TEXTURES["creatures"], 48, 33),
    "girl": frames.generate_frames(TEXTURES["girl"], 18, 33),
    "key-gold": frames.generate_frames(TEXTURES["key-gold"], 16, 16),
}

TILEMAPS = {
    i: BASE_DIR / "assets" / "tilemaps" / f"level{i}" for i in range(1, NUM_LEVELS + 1)
}

pygame.mixer.init()

SOUNDS = {
    "pickup_coin": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "pickup_coin.wav"),
    "jump": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "jump.wav"),
    "timer": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "timer.wav"),
    "count": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "count.wav"),
    "hit_bowie": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "hit_bowie.wav"),
    "bug_crash": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "bug_crash.wav"),
    "hyena_dead": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "hyena_dead.wav"),
    "man_dead_1": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "man_dead_1.wav"),
    "man_dead_2": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "man_dead_2.wav"),
    "snake_dead": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "snake_dead.wav"),
    "scorpion_dead": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "scorpion_dead.wav"),
    "kiss": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "kiss.wav"),
}

SOUNDS["pickup_coin"].set_volume(0.5)

pygame.font.init()

FONTS = {
    "small": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 8),
    "medium": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 16),
}
