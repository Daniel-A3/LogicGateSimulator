import pygame, os
from Game import Game
from MouseCursor import MouseCursor

#General setup
pygame.init()
clock = pygame.time.Clock()

# Sets the caption of the program
pygame.display.set_caption("OneOrZero")

# Sets the width and height of the program
WIDTH, HEIGHT = 1332, 802

#Create the display surface
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Loads the background
BACKGROUND = pygame.image.load(os.path.join("Assets", "backgroundGrid.png"))

# Loads all of the images
AND_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "ANDGate.png"))
OR_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "ORGate.png"))
NOT_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "NOTGate.png"))
NAND_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "NANDGate.png"))
NOR_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "NORGate.png"))
XOR_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "XORGate.png"))

def main():
    # Creates an instance of the Game class - represents the current game running
    game = Game(WIDTH, HEIGHT, BACKGROUND, SCREEN)
    # Creates an instance of the MouseCursor class - represents the users mouse
    mouse = MouseCursor()

    game.drawWindow()
    # Main game loop
    while game.run == True:
        game.processEvents()
        game.drawGates(AND_GATE_IMAGE, OR_GATE_IMAGE, NOT_GATE_IMAGE, 
                       NAND_GATE_IMAGE, NOR_GATE_IMAGE, XOR_GATE_IMAGE)
        mouse.update()
        clock.tick(60)

if __name__ == "__main__":
    main()