# MOUSE CURSOR CLASS
# --------------------------------------------------------------------------------------------
import pygame

class MouseCursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Creates a rect object for the mouse cursor
        self.rect = pygame.Rect(0, 0, 20, 20)
    def update(self):
        # x and y position of the mouse cursor
        self.xPos, self.yPos = pygame.mouse.get_pos()
        self.rect.center = self.xPos, self.yPos
