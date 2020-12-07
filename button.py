import color
import pygame
from instance_adt import *
from instance_manager import *
from typing import *

# A Button Manager that remembers the screen that buttons lie, automatically position the buttons.
# class ButtonManager:
#     def __init__(self):
#         self.button_dict = {}
#     def create_new_button(self):

# font = pygame.font.Font(pygame.font.get_default_font(), 30)


class Button(Instance):
    def __init__(self, width=100, height=30, upper_left=(0,0), default_color=color.LIGHT_GREY,
                 mouse_over_color=color.GREY, clicked_color=color.DARK_GREY, string=""):
        self.width = width
        self.height = height
        self.position = upper_left
        self.default_color = default_color
        self.mouse_over_color = mouse_over_color
        self.clicked_color = clicked_color
        self.xywh = [upper_left[0], upper_left[1], width, height]
        self.string = string
        self.rect = pygame.Rect(self.xywh)


    def is_mouse_over(self, mouse_position: List):
        if (self.position[0] <= mouse_position[0] <= self.position[0] + self.width
                and self.position[1] <= mouse_position[1] <= self.position[1] + self.height):
            return True
        else:
            return False

    def __str__(self):
        return self.string
