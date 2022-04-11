GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (130, 130, 130)


class LandingPage:
    def __init__(self, game):
        self.sound = game.sound
        self.screen = game.screen
        self.landing_page_finished = False
        self.highscore = game.stats.get_highscore()

        headingFont = pg.font.SysFont(None, 192)
        subheadingFont = pg.font.SysFont(None, 122)
        font = pg.font.SysFont(None, 48)

        strings = [('SPACE', WHITE, headingFont), ('INVADERS', GREEN, subheadingFont),
                   ('= 10 PTS', GREY, font), ('= 20 PTS', GREY, font),
                   ('= 40 PTS', GREY, font), ('= ???', GREY, font),
                   # ('PLAY GAME', GREEN, font),
                   (f'HIGH SCORE = {self.highscore:,}', GREY, font)]

        self.texts = [self.get_text(msg=s[0], color=s[1], font=s[2]) for s in strings]

        self.posns = [150, 230]
        alien = [65 * x + 350 for x in range(4)]
        # play_high = [x for x in range(650, 760, 80)]
        # play_high = 730
        self.posns.extend(alien)
        self.posns.append(730)

        centerx = self.screen.get_rect().centerx

        def get_text(self, font, msg, color):
            return font.render(msg, True, color, BLACK)

        def get_text_rect(self, text, centerx, centery):
            rect = text.get_rect()
            rect.centerx = centerx
            rect.centery = centery
            return rect

        def mouse_on_button(self):
            mouse_x, mouse_y = pg.mouse.get_pos()
            return self.play_button.rect.collidepoint(mouse_x, mouse_y)

        def check_events(self):
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    sys.exit()
                if e.type == pg.KEYUP and e.key == pg.K_p:  # pretend PLAY BUTTON pressed
                    self.landing_page_finished = True
                elif e.type == pg.MOUSEBUTTONDOWN:
                    if self.mouse_on_button():
                        self.landing_page_finished = True
                elif e.type == pg.MOUSEMOTION:
                    if self.mouse_on_button() and not self.hover:
                        self.play_button.toggle_colors()
                        self.hover = True
                    elif not self.mouse_on_button() and self.hover:
                        self.play_button.toggle_colors()
                        self.hover = False