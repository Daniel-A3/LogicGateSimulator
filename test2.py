import pygame
import random

class Block(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill([80, 80, 80])
        self.rect = self.image.get_rect()
 
class MouseCursor(pygame.sprite.Sprite):
    carryList = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Creates a rect object for the mouse cursor
        self.rect = pygame.Rect(0, 0, 20, 20)

    def update(self):
        self.xPos, self.yPos = pygame.mouse.get_pos()
        self.rect.center = self.xPos, self.yPos

        for block in self.carryList:
            block.rect.center = self.rect.center
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
WIDTH, HEIGHT = 1332, 802
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
rectList = pygame.sprite.Group()
 
# This is a list of every sprite.
# All blocks and the player block as well.
allSpritesGroup = pygame.sprite.Group()
 
for i in range(50):
    # This represents a block
    block = Block(80, 60)
 
    # Set a random location for the block
    block.rect.x, block.rect.y = (0,0)
 
    # Add the block to the list of objects
    rectList.add(block)
    allSpritesGroup.add(block)
 
# Create a RED player block
mouse = MouseCursor()
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # When the mouse button is pressed, see if we are in contact with
            # other sprites:
            print("test")
            rectHitList = pygame.sprite.spritecollide(mouse, rectList, False)
 
            # Set the list of blocks we are in contact with as the list of
            # blocks being carried.
            mouse.carryList = rectHitList
 
        elif event.type == pygame.MOUSEBUTTONUP:
            print("test2")
            # When we let up on the mouse, set the list of blocks we are
            # carrying as empty.
            mouse.carryList = []
 
    allSpritesGroup.update()
 
    # Draws the white background
    SCREEN.fill([255,255,255])
 
    # Draw all the spites
    rectList.draw(SCREEN)
 
    clock.tick(60)

    pygame.display.flip()
 
pygame.quit()