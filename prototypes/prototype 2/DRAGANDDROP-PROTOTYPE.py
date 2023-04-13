# PROTOTYPE
# THE AIM OF THIS PROTOTYPE IS IN ORDER TO EASE THE IMPLEMENTATION OF THE DRAG AND DROP FUNCTION
# IN THE MAIN PROGRAM

import pygame

# Initialize Pygame
pygame.init()

spriteGroup = pygame.sprite.Group()
sidebarSprites = pygame.sprite.Group()

# Set the height and width of the screen
WIDTH, HEIGHT = 1332, 802
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])

# Represents the rectangular blocks used in this prototype

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([80, 60])
        self.image.fill([80, 80, 80])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
class MouseCursor(pygame.sprite.Sprite):
    carryList = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Creates a rect object for the mouse cursor
        self.rect = pygame.Rect(0, 0, 20, 20)

    # Updates the position of the mouse and any blocks it is dragging
    def update(self):
        self.xPos, self.yPos = pygame.mouse.get_pos()
        self.rect.center = self.xPos, self.yPos

        for block in self.carryList:
            block.rect.center = self.rect.center
            break

# Represents the sidebar menu
class sidebarMenu():
    def __init__(self):
        self.border = 256

    # Draws new instances of the components in their original position - in the sidebar
    def drawSprites(self):
        block1 = Block(0,0)
        sidebarSprites.add(block1)
        spriteGroup.add(block1)

        block2 = Block(0, 100)
        sidebarSprites.add(block2)
        spriteGroup.add(block2)

        sidebarSprites.draw(SCREEN)

# Creates Instance of the sidebarMenu class
sidebar = sidebarMenu()

# Creates Instance of the MouseCursor class
mouse = MouseCursor()
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Adds all collided sprites to the carryList
            mouse.carryList = pygame.sprite.spritecollide(mouse, spriteGroup, False)
 
        elif event.type == pygame.MOUSEBUTTONUP:
            # When you let go on the mouse the carryList is emptied
            mouse.carryList = []
 
    mouse.update()
 
    # Draws the white background
    SCREEN.fill([255,255,255])
 
    # Draw all the spites
    spriteGroup.draw(SCREEN)
    sidebar.drawSprites()
 
    clock.tick(60)

    pygame.display.flip()
 
pygame.quit()