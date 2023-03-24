import pygame, os
import Game

pygame.init()
pygame.display.set_caption("OneOrZero")

WIDTH, HEIGHT = 1332, 802
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OneOrZero")

BACKGROUND = pygame.image.load(os.path.join("Assets", "backgroundGrid.png"))

def main():
    # Creates an instance of the Game class
    game = Game(WIDTH, HEIGHT, BACKGROUND)

    # Main game loop
    while game.run == True:
        game.processEvents()
        game.drawWindow()

    pygame.quit()

if __name__ == "__main__":
    main()