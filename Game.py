import pygame as pg
from Landing_Page import LandingPage
from sys import exit
import Game_Functions as gf
from Sound import Sound
from Scoreboard import Scoreboard
from Settings import Settings
from Stats import Stats


class Game:
    RED = (255, 0, 0)

    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.stats = Stats(game=self)
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        self.sound = Sound()
        self.sb = Scoreboard(game=self)
        pg.display.set_caption("Super Mario")

    def play(self):
        finished = False
        self.sound.play_bg()
        while not finished:
            self.update()
            self.draw()
            gf.check_events(game=self)  # exits game if QUIT pressed
        self.game_over()

    def game_over(self):
        self.sound.play_game_over()
        print('\nGAME OVER!\n\n')
        exit()    # can ask to replay here instead of exiting the game