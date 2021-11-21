import pygame
import math
import random


class Shot(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/shot.png")
        self.image = pygame.transform.scale(self.image, [10, 10])
        self.rect = self.image.get_rect()


        

        self.speed = 4


    def update(self, *args):
        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill()
            
