import pygame
import color
import button
import sys
import chess
import chess.pgn
import piece_rect
from abc import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def open_game():
    root = Tk()
    root.withdraw()
    filename = askopenfilename(initialdir=sys.path[0]+"\\Games", title="Select file", filetypes=(("PGN", "*.pgn"), ("all files", "*.*")))
    if not filename:
        print("Select again.")
        return
    with open(filename, 'r') as pgn:
        game = chess.pgn.read_game(pgn)
    return game


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
        image_button.resize_by_scale(0.2)
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
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                done = True

            # Screen filling
            screen.fill(color.WHITE)
            if image_button.draw(screen, mouse_position, clicked) == 2:
                game = open_game()
                self.scene_manager.next_scene = GameScene(self.scene_manager, game)
                done = True
            pygame.display.flip()
            clicked = False


class GameScene(Scene):
    def __init__(self, scene_manager, game):
        super().__init__(scene_manager)
        self.game = game
        self.moves = self.game.mainline_moves()

    # CORRECTION:
    # chess.pgn.Mainline which returns from the method mainline_moves() is an iterable, it is not subscriptable.
    # Use a generator to iterate in moves.
    # It does not support backward moves.
    # Has to be modified.
    def get_move(self):
        moves = self.moves
        for move in moves:
            yield move

    def run(self):
        print(self.game)
        game = self.game.board()
        moves = self.game.mainline_moves()
        move = self.get_move()
        game_iter = 0
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
        pieces = piece_rect.Piece()
        pieces.resize_all_by_pixel([int(size[0]/8),int(size[1]/8)])

        done = False
        mouse_position = pygame.mouse.get_pos()

        screen.fill(color.WHITE)
        screen.blit(board, board_rect)
        while not done:
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.scene_manager.next_scene = Menu(self.scene_manager)
                done = True
            elif keys[pygame.K_RIGHT]:
                screen.fill(color.WHITE)
                screen.blit(board, board_rect)
                game.push(next(move))
                game_iter += 1
                game_list = [i.split(' ') for i in str(game).split('\n')]
                for i, rank in enumerate(game_list):
                    for j, square in enumerate(rank):
                        if square == '.':
                            pass
                        else:
                            screen.blit(pieces.piece_dict[square], ((j*2)/2*size[0]/8, (i*2)/2*size[1]/8))
            pygame.display.flip()