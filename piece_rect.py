import pygame


class Piece:
    def __init__(self):
        self.piece_dict = {"p": pygame.image.load("Sprites\\bp.png").convert_alpha(),
                           "r": pygame.image.load("Sprites\\br.png").convert_alpha(),
                           "n": pygame.image.load("Sprites\\bn.png").convert_alpha(),
                           "b": pygame.image.load("Sprites\\bb.png").convert_alpha(),
                           "q": pygame.image.load("Sprites\\bq.png").convert_alpha(),
                           "k": pygame.image.load("Sprites\\bk.png").convert_alpha(),
                           "P": pygame.image.load("Sprites\\wp.png").convert_alpha(),
                           "R": pygame.image.load("Sprites\\wr.png").convert_alpha(),
                           "N": pygame.image.load("Sprites\\wn.png").convert_alpha(),
                           "B": pygame.image.load("Sprites\\wb.png").convert_alpha(),
                           "Q": pygame.image.load("Sprites\\wq.png").convert_alpha(),
                           "K": pygame.image.load("Sprites\\wk.png").convert_alpha()}

    def resize_all_by_scale(self, scale: float):
        for item in self.piece_dict.items():
            size = (int(item[1].get_width() * scale), int(item[1].get_height() * scale))
            self.piece_dict[item[0]] = pygame.transform.scale(item[1], size)

    def resize_all_by_pixel(self, size):
        for item in self.piece_dict.items():
            self.piece_dict[item[0]] = pygame.transform.scale(item[1], size)