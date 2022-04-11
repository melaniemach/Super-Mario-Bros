import pygame as pg
from pygame.sprite import Group


class Scoreboard:
    def __init__(self, game):
        self.game = game
        self.stats = game.stats
        screen = game.screen
        sr = screen.get_rect()
        self.bg_color = game.bg_color
        font = pg.font.SysFont(None, 48)