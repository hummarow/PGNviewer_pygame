import pygame
import constants
import color
import button
import chess
import chess.pgn
import os

SAMPLEGAME = "Games\\sample_game.pgn"


def import_game(gameroute: str = SAMPLEGAME):
    with open(gameroute, 'r') as pgn:
        game = chess.pgn.read_game(pgn)
    print(game)


def start_screen():
    pygame.init()
    size = [512, 512]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("-PGN VIEWER-")
    clock = pygame.time.Clock()

    done = False
    clicked = False
    select_game_button = button.Button(100, 30, ((size[0]-100)/2,(size[1]-30)/2), string="Select PGN file")
    font = pygame.font.Font(pygame.font.get_default_font(), 10)

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
        text = font.render(select_game_button.string, True, (30,0,0))
        if select_game_button.is_mouse_over(mouse_position):
            if clicked:
                screen.fill(select_game_button.clicked_color, select_game_button.rect)
                clicked = False
            else:
                screen.fill(select_game_button.mouse_over_color, select_game_button.rect)
        else:
            screen.fill(select_game_button.default_color, select_game_button.rect)
        screen.blit(text, select_game_button.position)
        pygame.display.flip()


def game_screen():
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

        screen.fill(color.WHITE)
        screen.blit(board, board_rect)
        pygame.display.flip()


if __name__ == '__main__':
    start_screen()