from pygame.sprite import Sprite, Group
import pygame


class Level:
    def __init__(self, screen, sound, dashboard):
        self.sprites = Group()
        self.dashboard = dashboard
        self.sound = sound
        self.screen = screen
        self.level = None
        self.levelLength = 0 #223?
        self.entities = []
        self.level_name = 'level_loc.txt'

    def generate_level(self, level_name):
        f = open(level_name, 'r')
        unknowns = 0
        for line in f:
            for symbol in line:
                if symbol == 'X':
                    print('Surface Brick')
                elif symbol == 'A':
                    print('Underground Breakable Brick')
                elif symbol == 'N':
                    print('Underground Brick')
                elif symbol == 'C':
                    print('Coin')
                elif symbol == 'B':
                    print('Surface Breakable Brick')
                elif symbol == '?':
                    print('Random Block')
                elif symbol == 'R':
                    print('Stair Block')
                elif symbol == 'K':
                    print('Koopa')
                elif symbol == 'G':
                    print('Goomba')
                elif symbol == 'M':
                    print('Mushroom')
                elif symbol == 'L':
                    print('Coin Block')
                elif symbol == 'S':
                    print('Star')
                elif symbol == 'I':
                    print('Invisible Block')
                elif symbol == '\n':
                    pass
                elif symbol == ' ':
                    pass  # print('Air')
                else:
                    unknowns += 1
                    print(symbol)
        print(unknowns)

    def draw(self):
        self.screen.fill(bg_color)


windowSize = (1200, 800)
bg_color = (135, 206, 235)


def main():
    print('Generate Level Test from file')
    pygame.init()
    screen = pygame.display.set_mode(windowSize)

    screen.fill(bg_color)
    dashboard = 'filler'
    sound = 'filler'  # Sound()
    level = Level(screen, sound, dashboard)
    level.generate_level('./images/level_loc.txt')
    finished = False
    while not finished:
        level.draw()



if __name__ == "__main__":
    main()