# MOUSE CURSOR CLASS
# --------------------------------------------------------------------------------------------
import pygame

pygame.init()

class MouseCursor(pygame.sprite.Sprite):
    carryList = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Creates a rect object for the mouse cursor
        self.rect = pygame.Rect(0, 0, 20, 20)

    # Updates the position of the mouse and any object it is dragging
    def update(self):
        # x and y position of the mouse cursor
        self.xPos, self.yPos = pygame.mouse.get_pos()
        self.rect.center = self.xPos, self.yPos

        for block in self.carryList:
            block.rect.center = self.rect.center
            # This break is necessary so that you can only pick up one component at a time.
            break
