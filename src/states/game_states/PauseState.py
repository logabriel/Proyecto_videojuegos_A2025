"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class PauseState.
"""

from typing import Dict, Any

import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text
from src.Player import Player
from gale.timer import Timer

import settings


class PauseState(BaseState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.level = enter_params["level"]
        self.camera = enter_params["camera"]
        self.game_level = enter_params["game_level"]
        self.tilemap = self.game_level.tilemap
        self.players = enter_params["players"]
        self.clock = enter_params["clock"]
        pygame.mixer.music.pause()

    def exit(self) -> None:
        pygame.mixer.music.unpause()

    def render(self, surface: pygame.Surface) -> None:
        world_surface = pygame.Surface((self.tilemap.width, self.tilemap.height))
        self.game_level.render(world_surface)
        
        for player in self.players:
            if player != None:
                player.render(world_surface)

        surface.blit(world_surface, (-self.camera.x, -self.camera.y))

        render_text(
            surface,
            f"Girl save: {Player.girl_save}",
            settings.FONTS["small"],
            5,
            5,
            (255, 255, 255),
            shadowed=True,
        )

        render_text(
            surface,
            f"Time: {self.clock.time}",
            settings.FONTS["small"],
            settings.VIRTUAL_WIDTH - 60,
            5,
            (255, 255, 255),
            shadowed=True,
        )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "pause" and input_data.pressed:
            self.state_machine.change(
                "play",
                level=self.level,
                camera=self.camera,
                game_level=self.game_level,
                players=self.players,
                clock=self.clock,
            )
