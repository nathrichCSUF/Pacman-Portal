import pygame
from imagerect import ImageRect


class Maze:
    RED = (255, 0, 0)
    BRICK_SIZE = 13

    def __init__(self, screen, mazefile, brickfile, portalfile, shieldfile, powerfile, pointsfile, foodfile):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.bricks = []
        self.shields = []
        self.hportals = []
        self.vportals = []
        self.fruit = []
        self.points = []
        self.powerpills = []

        sz = Maze.BRICK_SIZE
        self.brick = ImageRect(screen, brickfile, sz, sz)
        self.shield = ImageRect(screen, shieldfile, sz, sz)
        self.cherry = ImageRect(screen, foodfile, 20, 20)
        self.point = ImageRect(screen, pointsfile, 20, 20)
        self.powerpill = ImageRect(screen, powerfile, 25, 25)
        self.vportal = ImageRect(screen, portalfile, 64, 32)
        self.hportal = ImageRect(screen, portalfile, 32, 64)

        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.build()

    def build(self):
        r = self.brick.rect
        w, h = r.width, r.height

        s_r = self.shield.rect
        sw, sh = s_r.width, s_r.height

        hportal_r = self.hportal.rect
        hpw, hph = hportal_r.width, hportal_r.height

        vportal_r = self.vportal.rect
        vpw, vph = vportal_r.width, vportal_r.height

        # for the fruit
        f_r = self.cherry.rect
        fw, fh = f_r.width, f_r.height

        # for the points
        point_r = self.point.rect
        pw, ph = point_r.width, point_r.height

        # for powerpills
        power_r = self.powerpill.rect
        pow_w, pow_h = power_r.width, power_r.height

        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'X':
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'o':
                    self.shields.append(pygame.Rect(ncol * dx, nrow * dy, sw, sh))
                elif col == 'v':
                    self.vportals.append(pygame.Rect(ncol * dx, nrow * dy, hpw, hph))
                elif col == 'h':
                    self.hportals.append(pygame.Rect(ncol * dx, nrow * dy, vpw, vph))
                elif col == 'C':
                    self.fruit.append(pygame.Rect(ncol * dx, nrow * dy, fw, fh))
                elif col == 'P':
                    self.powerpills.append(pygame.Rect(ncol * dx, nrow * dy, pow_w, pow_h))
                elif col == '.':
                    self.points.append(pygame.Rect(ncol * dx, nrow * dy, pw, ph))

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
        for rect in self.shields:
            self.screen.blit(self.shield.image, rect)
        for rect in self.hportals:
            self.screen.blit(self.hportal.image, rect)
        for rect in self.vportals:
            self.screen.blit(self.vportal.image, rect)
        for rect in self.fruit:
            self.screen.blit(self.cherry.image, rect)
        for rect in self.powerpills:
            self.screen.blit(self.powerpill.image, rect)
        for rect in self.points:
            self.screen.blit(self.point.image, rect)
