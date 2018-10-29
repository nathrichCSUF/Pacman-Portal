import pygame
import sys


class EventLoop:
    def __init__(self, finished):
        self.finished = finished
        self.game_active = False

    def __str__(self):
        return 'eventloop,finished= ' + str(self.finished) + ')'

    def check_events(self, pacman):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event, pacman)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event, pacman)

    @staticmethod
    def check_keydown_events(event, pacman):
        if event.key == pygame.K_UP:
            pacman.movingUp = True
        if event.key == pygame.K_DOWN:
            pacman.movingDown = True
        if event.key == pygame.K_RIGHT:
            pacman.movingRight = True
        if event.key == pygame.K_LEFT:
            pacman.movingLeft = True

    @staticmethod
    def check_keyup_events(event, pacman):
        if event.key == pygame.K_UP:
            pacman.movingUp = False
        if event.key == pygame.K_DOWN:
            pacman.movingDown = False
        if event.key == pygame.K_RIGHT:
            pacman.movingRight = False
        if event.key == pygame.K_LEFT:
            pacman.movingLeft = False


# def click_play(self, mouse_x, mouse_y):
# pygame.mouse.set_visible(False)
# button_clicked = self.menu.play_button.collidepoint(mouse_x, mouse_y)
# if button_clicked and not self.game_active:
# Wself.game_active = True
'''            
elif event.type == pygame.MOUSEBUTTONDOWN:
mouse_x, mouse_y = pygame.mouse.get_pos()
self.click_play(mouse_x, mouse_y)
'''
