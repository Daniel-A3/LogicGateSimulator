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

        # Finds the offset of how much the mouse was moved
        offsetX = self.rect.x - self.xPos
        offsetY = self.rect.y - self.yPos

        for component in self.carryList:
            component.rect.x -= offsetX
            component.rect.y -= offsetY
            # This break is necessary so that you can only pick up one component at a time.
            break

        self.rect.x, self.rect.y = self.xPos, self.yPos
