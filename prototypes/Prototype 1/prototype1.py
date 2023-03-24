import pygame, os

pygame.init()

WIDTH, HEIGHT = 1332, 802
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OneOrZero")
WHITE = (255, 255, 255)

BACKGROUND = pygame.image.load(os.path.join("Assets", "backgroundGrid.png"))

FPS = 60
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

def drawWindow():
    SCREEN.fill(WHITE)
    SCREEN.blit(BACKGROUND, (250,0))

    SCREEN.blit(AND_GATE, (0,0))

    pygame.display.update()

def main():
    # The main game loop
    run = True
    while run:
        for event in pygame.event.get():
            # Quits the game if it is exited
            if event.type == pygame.QUIT:
                run = False
        drawWindow()

    pygame.quit()

if __name__ == "__main__":
    main()