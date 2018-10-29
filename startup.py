import pygame

class Startup:
    def __init__(self,screen,startfile,playfile):
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.titlepath=startfile
        self.playpath=playfile

        self.title=pygame.image.load_extended(self.titlepath)
        self.play_button = pygame.image.load_extended(self.playpath)

        self.titlerect=self.title.get_rect()
        self.playrect=self.play_button.get_rect()

        self.titlerect.center=self.screen_rect.center
        self.titlerect.top = self.screen_rect.top

        self.playrect.center=self.screen_rect.center

    def draw_menu(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.title,self.titlerect)
        self.screen.blit(self.play_button, self.playrect)



