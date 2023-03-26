import pygame

class MouseCursor(pygame.sprite.Sprite):
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()
    def update(self):
        self.rect = pygame.Rect(self.x, self.y)
        print(self.rect.x)
        print(self.rect.y)
        