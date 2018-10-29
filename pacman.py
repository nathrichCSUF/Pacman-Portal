import pygame


class Pacman:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load_extended("pacman.png")
        pygame.transform.scale(self.image, (15, 15))
        self.pac_rect = self.image.get_rect()
        self.pac_rect.x = 330
        self.pac_rect.y = 445
        self.movingUp = False
        self.movingDown = False
        self.movingRight = False
        self.movingLeft = False

        self.speed = float(2.5)

    def update(self):
        if self.movingUp:
            self.pac_rect.y -= self.speed
        if self.movingDown:
            self.pac_rect.y += self.speed
        if self.movingRight:
            self.pac_rect.x += self.speed
        if self.movingLeft:
            self.pac_rect.x -= self.speed

    def blit_pac(self):
        self.screen.blit(self.image, self.pac_rect)
