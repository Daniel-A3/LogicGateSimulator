import pygame
import random

class Block(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill([0,0,0])
        self.rect = self.image.get_rect()
 
class MouseCursor(pygame.sprite.Sprite):
    carry_rectList = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Creates a rect object for the mouse cursor
        self.rect = pygame.Rect(0, 0, 20, 20)

    def update(self):
        pos = pygame.mouse.get_pos()
 
        # Now see how the mouse position is different from the current
        # player position. (How far did we move?)
        diff_x = self.rect.x - pos[0]
        diff_y = self.rect.y - pos[1]
 
        # Loop through each block that we are carrying and adjust
        # it by the amount we moved.
        for block in self.carry_rectList:
            block.rect.x -= diff_x
            block.rect.y -= diff_y
 
        # Now wet the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
WIDTH, HEIGHT = 1332, 802
screen = pygame.display.set_mode([WIDTH, HEIGHT])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
rectList = pygame.sprite.Group()
 
# This is a list of every sprite.
# All blocks and the player block as well.
allSpritesGroup = pygame.sprite.Group()
 
for i in range(50):
    # This represents a block
    block = Block(128, 64)
 
    # Set a random location for the block
    block.rect.x = random.randrange(WIDTH)
    block.rect.y = random.randrange(HEIGHT)
 
    # Add the block to the list of objects
    rectList.add(block)
    allSpritesGroup.add(block)
 
# Create a RED player block
mouse = MouseCursor()
allSpritesGroup.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(False)
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # When the mouse button is pressed, see if we are in contact with
            # other sprites:
            rectHitList = pygame.sprite.spritecollide(player, rectList, False)
 
            # Set the list of blocks we are in contact with as the list of
            # blocks being carried.
            player.carry_rectList = rectHitList
 
        elif event.type == pygame.MOUSEBUTTONUP:
            # When we let up on the mouse, set the list of blocks we are
            # carrying as empty.
            player.carry_rectList = []
 
    allSpritesGroup.update()
 
    # Draws the white background
    screen.fill([255,255,255])
 
    # Draw all the spites
    allSpritesGroup.draw(screen)
 
    clock.tick(60)

    pygame.display.flip()
 
pygame.quit()