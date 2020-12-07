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
    # CORRECTION: The variable 'position' has to store a center coordination of the button.
    #             Because the blit function requires a top left of the surface, we need to calculate again.
    #             However, it is more clear way to store a position of the button.
    #             Especially when it becomes ImageButton.
    #             IsMouseOver already changed.
    def __init__(self, width=100, height=30, position=(0, 0), default_color=color.LIGHT_GREY,
                 mouse_over_color=color.GREY, clicked_color=color.DARK_GREY, string=""):
        self.width = width
        self.height = height
        self.position = position
        self.default_color = default_color
        self.mouse_over_color = mouse_over_color
        self.clicked_color = clicked_color
        self.xywh = [position[0], position[1], width, height]
        self.string = string
        self.rect = pygame.Rect(self.xywh)

    def is_mouse_over(self, mouse_position: List):
        if (self.position[0] - self.width/2 <= mouse_position[0] <= self.position[0] + self.width/2
                and self.position[1] - self.height/2 <= mouse_position[1] <= self.position[1] + self.height/2):
            return True
        else:
            return False

    def __str__(self):
        return self.string


class ImageButton(Button):
    def __init__(self, position=(0, 0), default_image="", mouse_over_image="", clicked_image=""):
        self.position = position
        if default_image and mouse_over_image and clicked_image:
            self.default_image = pygame.image.load(default_image).convert_alpha()
            self.mouse_over_image = pygame.image.load(mouse_over_image).convert_alpha()
            self.clicked_image = pygame.image.load(clicked_image).convert_alpha()
        else:
            raise ValueError("Image Path is not passed when creating a ImageButton.")
        self.width = self.default_image.get_width()
        self.height = self.default_image.get_height()

    def resize(self, size):
        self.default_image = pygame.transform.scale(self.default_image, size)
        self.mouse_over_image = pygame.transform.scale(self.mouse_over_image, size)
        self.clicked_image = pygame.transform.scale(self.clicked_image, size)
        self.width = self.default_image.get_width()
        self.height = self.default_image.get_height()

    def draw(self, screen: pygame.Surface, mouse_position,clicked: bool):
        if self.is_mouse_over(mouse_position):
            if clicked:
                image = self.clicked_image
            else:
                image = self.mouse_over_image
        else:
            image = self.default_image
        screen.blit(image, (self.position[0] - image.get_width()/2, self.position[1] - image.get_height()/2))