import pygame
import constants
import color
import button
import chess
import chess.pgn
import scene

SAMPLEGAME = "Games\\sample_game.pgn"


def import_game(gameroute: str = SAMPLEGAME):
    with open(gameroute, 'r') as pgn:
        game = chess.pgn.read_game(pgn)
    print(game)


if __name__ == '__main__':
    scene_manager = scene.SceneManager()
    first_scene = scene.Menu(scene_manager)
    scene_manager.next_scene = first_scene
    scene_manager.run()
