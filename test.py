# TEST
# The purpose of this test is in order to succesfully implement the drag and drop function,
# whilst also having instances reappear in the sidebar menu after they are dragged, allowing
# for multiple instances of the same gate to be dragged onto the workspace.
import pygame

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1332, 802
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

def dragAndDrop():
    pass

allSprites = pygame.sprite.Group()
sidebarSprites = pygame.sprite.Group()

class Rectangle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([128,64])
        self.image.fill([128,128,128])
        self.rect = self.image.get_rect()

run = True
# Main game loop
while run == True:
    # Checks if the game was quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Draws the screen every game loop
    SCREEN.fill((255, 255, 255))

    rec1 = Rectangle()
    rec2 = Rectangle()
    rec3 = Rectangle()

    sidebarSprites.add(rec1)
    sidebarSprites.add(rec2)
    sidebarSprites.add(rec3)

    sidebarSprites.draw(SCREEN)

    dragAndDrop()
