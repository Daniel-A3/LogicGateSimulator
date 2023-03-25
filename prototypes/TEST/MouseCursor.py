import pygame

class MouseCursor(pygame.sprite.Sprite):
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()
    def update(self):
        pass