import pygame, os
from Game import Game

pygame.init()
pygame.display.set_caption("OneOrZero")

WIDTH, HEIGHT = 1332, 802

BACKGROUND = pygame.image.load(os.path.join("Assets", "backgroundGrid.png"))

#  Ensures that all the icons are the same size.
AND_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "ANDGate.png"))
AND_GATE = pygame.transform.smoothscale(AND_GATE_IMAGE, (128, 64))
OR_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "ORGate.png"))
OR_GATE = pygame.transform.smoothscale(OR_GATE_IMAGE, (128, 64))
NOT_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "NOTGate.png"))
NOT_GATE = pygame.transform.smoothscale(NOT_GATE_IMAGE, (128, 64))
NAND_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "NANDGate.png"))
NAND_GATE = pygame.transform.smoothscale(NAND_GATE_IMAGE, (128, 64))
NOR_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "NORGate.png"))
NOR_GATE = pygame.transform.smoothscale(NOR_GATE_IMAGE, (128, 64))
XOR_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "XORGate.png"))
XOR_GATE = pygame.transform.smoothscale(XOR_GATE_IMAGE, (128, 64))

def main():
    # Creates an instance of the Game class
    game = Game(WIDTH, HEIGHT, BACKGROUND)
    game.drawWindow()
    # Main game loop
    while game.run == True:
        game.processEvents()
        game.drawGates(AND_GATE, OR_GATE, NOT_GATE, NAND_GATE, NOR_GATE, XOR_GATE)

    pygame.quit()

if __name__ == "__main__":
    main()