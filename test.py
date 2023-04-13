# TEST
# The purpose of this test is in order to succesfully implement the drag and drop function,
# whilst also having instances reappear in the sidebar menu after they are dragged, allowing
# for multiple instances of the same gate to be dragged onto the workspace.
import pygame

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1332, 802
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

allSprites = pygame.sprite.Group()

class Rectangle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([80, 60])
        self.image.fill([100, 100, 100])
        self.rect = self.image.get_rect()

def main():
    run = True

    rec1 = Rectangle()
    rec2 = Rectangle()
    rec3 = Rectangle()

    allSprites.add(rec1)
    allSprites.add(rec2)
    allSprites.add(rec3)
    
    # Main game loop
    while run:
        # Checks if the game was quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Draws the screen every game loop
        SCREEN.fill((255, 255, 255))

        allSprites.draw(SCREEN)

        pygame.display.update()

    pygame.quit()

main()
