import pygame
import color
import button
from abc import *


class SceneManager:
    def __init__(self):
        self.next_scene = None

    def run(self):
        while self.next_scene:
            self.next_scene.run()


class Scene(metaclass=ABCMeta):
    def __init__(self, scene_manager: SceneManager):
        self.scene_manager = scene_manager

    @abstractmethod
    def run(self):
        pass


class Menu(Scene):
    def run(self):
        self.scene_manager.next_scene = None
        pygame.init()
        size = [512, 512]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("-PGN VIEWER-")
        clock = pygame.time.Clock()
        done = False
        clicked = False
        font = pygame.font.Font(pygame.font.get_default_font(), 10)
        image_button = button.ImageButton((size[0] / 2, size[1] / 2), "Sprites\\select_file.png",
                                          "Sprites\\select_file_over.png", "Sprites\\select_file_clicked.png")
        image_button.resize((100, 30))
        # Main Loop
        while not done:
            clock.tick(10)
            mouse_position = pygame.mouse.get_pos()

            # Event Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True

            # Screen filling
            screen.fill(color.WHITE)
            if image_button.draw(screen, mouse_position, clicked) == 2:
                self.scene_manager.next_scene = GameScene(self.scene_manager)
                done = True
            pygame.display.flip()
            clicked = False


class GameScene(Scene):
    def run(self):
        self.scene_manager.next_scene = None
        pygame.init()
        size = [512, 512]
        screen = pygame.display.set_mode(size)
        # To be title of the game.
        pygame.display.set_caption("-PGN VIEWER-")
        clock = pygame.time.Clock()

        board = pygame.image.load(r'Sprites/board.png')
        board = pygame.transform.scale(board, size)
        board_rect = board.get_rect()
        done = False
        mouse_position = pygame.mouse.get_pos()
        while not done:
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            keys =  pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.scene_manager.next_scene = Menu(self.scene_manager)
                done = True

            screen.fill(color.WHITE)
            screen.blit(board, board_rect)
            pygame.display.flip()