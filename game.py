import pygame

from maze import Maze
from eventloop import EventLoop
from pacman import Pacman
from startup import Startup
from ghosts import Ghosts


class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((680, 740))
        pygame.display.set_caption("Pacman Portal")

        self.maze = Maze(self.screen, mazefile='maze.txt', brickfile='square', portalfile='close_portal', shieldfile='shield',
                         powerfile='powerpil', pointsfile='points', foodfile='cherry')
        self.menu = Startup(self.screen, 'title.png', 'playbutton.png')
        self.pacman = Pacman(self.screen)
        self.ghosts = Ghosts(self.screen)

        self.eloop = EventLoop(finished=False)

    def __str__(self): return 'Game(Pacman Portal),maze='

    def play(self):
        while not self.eloop.finished:
            self.eloop.check_events(self.pacman)
            self.pacman.update()
            # if self.game_active:
            self.update_screen()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        self.maze.blitme()
        self.pacman.blit_pac()
        self.ghosts.blit_ghost()

        # if not self.eloop.game_active:
        # self.menu.draw_menu()
        pygame.display.flip()


game = Game()
game.play()
