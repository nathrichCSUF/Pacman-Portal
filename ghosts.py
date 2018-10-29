import pygame
from pygame.sprite import Sprite



class Ghosts(Sprite):
    def __init__(self, screen):
        super(Ghosts, self).__init__()
        self.screen = screen
        self.blinky = pygame.image.load_extended('blinky.png')
        self.pinky = pygame.image.load_extended('pinky.png')
        self.inky = pygame.image.load_extended('inky.png')
        self.clyde = pygame.image.load_extended('clyde.png')

        pygame.transform.scale(self.blinky, (64,64))
        pygame.transform.scale(self.pinky, (64, 64))
        pygame.transform.scale(self.inky, (64, 64))
        pygame.transform.scale(self.clyde, (64, 64))

        self.b_rect=self.blinky.get_rect()
        self.p_rect=self.pinky.get_rect()
        self.i_rect=self.inky.get_rect()
        self.c_rect=self.clyde.get_rect()
        # build list of ghosts

        self.b_rect.x = 300
        self.b_rect.y = 225

        self.p_rect.x = 260
        self.p_rect.y = 300

        self.i_rect.x = 280
        self.i_rect.y = 300

        self.c_rect.x = 300
        self.c_rect.y = 300

        self.ghost_list=[]
        self.ghost_list.append(self.b_rect)
        self.ghost_list.append(self.p_rect)
        self.ghost_list.append(self.i_rect)
        self.ghost_list.append(self.c_rect)

        self.ghostimages=[]
        self.ghostimages.append(self.blinky)
        self.ghostimages.append(self.pinky)
        self.ghostimages.append(self.inky)
        self.ghostimages.append(self.clyde)


    def blit_ghost(self):
        for ghost in range(4):
            self.screen.blit(self.ghostimages[ghost], self.ghost_list[ghost])

