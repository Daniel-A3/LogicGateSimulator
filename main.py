import pygame, os

pygame.init()

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OneOrZero")
WHITE = (255, 255, 255)

FPS = 60

AND_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "ANDGate.png"))
AND_GATE = pygame.transform.scale(AND_GATE_IMAGE, (100,56))
OR_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "ORGate.png"))
OR_GATE = pygame.transform.scale(OR_GATE_IMAGE, (100,56))
NOT_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "NOTGate.png"))
NOT_GATE = pygame.transform.scale(NOT_GATE_IMAGE, (100,56))
NAND_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "NANDGate.png"))
NAND_GATE = pygame.transform.scale(NAND_GATE_IMAGE, (125,56))
NOR_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "NORGate.png"))
NOR_GATE = pygame.transform.scale(NOR_GATE_IMAGE, (100,56))
XOR_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "XORGate.png"))
XOR_GATE = pygame.transform.scale(XOR_GATE_IMAGE, (100,56))

def drawWindow():
    WIN.fill(WHITE)
    WIN.blit(AND_GATE, (0,0))
    WIN.blit(OR_GATE, (125,0))
    WIN.blit(NOT_GATE, (250,0))
    WIN.blit(NAND_GATE, (375,0))
    WIN.blit(NOR_GATE, (500,0))
    WIN.blit(XOR_GATE, (625,0))
    pygame.display.update()

def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        drawWindow()

    pygame.quit()

    
# Creates buttons for all logic gates
#ANDGate = Button(pygame.image.load("andgate.png"))
#ANDGate.rect.x = 50
#ANDGate.rect.y = 20

if __name__ == "__main__":
    main()