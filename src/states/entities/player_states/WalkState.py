"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class WalkState for player.
"""

from gale.input_handler import InputData

import settings
from src.states.entities.BaseEntityState import BaseEntityState


class WalkState(BaseEntityState):
    def enter(self, direction: str) -> None:
        self.entity.flipped = direction == "left"
        self.entity.vx = settings.PLAYER_SPEED
        if self.entity.flipped:
            self.entity.vx *= -1
        self.entity.change_animation("walk")

    def update(self, dt: float) -> None:
        if not self.entity.check_floor():
            self.entity.change_state("fall")

        # If there is a collision on the right, correct x. Else, correct x if there is collision on the left.
        self.entity.handle_tilemap_collision_on_right() or self.entity.handle_tilemap_collision_on_left()

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if self.entity.player_type == 1:
            if input_id == "move_left":
                if input_data.pressed:
                    self.entity.vx = -settings.PLAYER_SPEED
                    self.entity.flipped = True
                    self.entity.direcction = settings.LEFT 
                elif input_data.released and self.entity.vx <= 0:
                    self.entity.change_state("idle")
            elif input_id == "move_right":
                if input_data.pressed:
                    self.entity.vx = settings.PLAYER_SPEED
                    self.entity.flipped = False
                    self.entity.direcction = settings.RIGHT 
                elif input_data.released and self.entity.vx >= 0:
                    self.entity.change_state("idle")
            elif input_id == "jump" and input_data.pressed:
                self.entity.change_state("jump")
            elif input_id == "attack":
                if self.entity.direcction == settings.RIGHT:
                    self.entity.change_state("attack", "right")
                else :
                    self.entity.change_state("attack", "left")
        else :
            if input_id == "move_left_p2":
                if input_data.pressed:
                    self.entity.vx = -settings.PLAYER_SPEED
                    self.entity.flipped = True
                    self.entity.direcction = settings.LEFT 
                elif input_data.released and self.entity.vx <= 0:
                    self.entity.change_state("idle")

            elif input_id == "move_right_p2":
                if input_data.pressed:
                    self.entity.vx = settings.PLAYER_SPEED
                    self.entity.flipped = False
                    self.entity.direcction = settings.RIGHT 
                elif input_data.released and self.entity.vx >= 0:
                    self.entity.change_state("idle")
            elif input_id == "jump_p2" and input_data.pressed:
                self.entity.change_state("jump")
            elif input_id == "attack_p2":
                if self.entity.direcction == settings.RIGHT:
                    self.entity.change_state("attack", "right")
                else :
                    self.entity.change_state("attack", "left")
