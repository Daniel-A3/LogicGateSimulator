import pygame, os

pygame.init()

WIDTH, HEIGHT = 1332, 802
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OneOrZero")
WHITE = (255, 255, 255)

BACKGROUND = pygame.image.load(os.path.join("Assets", "backgroundGrid.png"))

FPS = 60
#  Ensures that all the icons are the same size.
AND_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "ANDGate.png")).convert_alpha()
AND_GATE = pygame.transform.smoothscale(AND_GATE_IMAGE, (128, 64))
OR_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "ORGate.png")).convert_alpha()
OR_GATE = pygame.transform.smoothscale(OR_GATE_IMAGE, (128, 64))
NOT_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "NOTGate.png")).convert_alpha()
NOT_GATE = pygame.transform.smoothscale(NOT_GATE_IMAGE, (128, 64))
NAND_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "NANDGate.png")).convert_alpha()
NAND_GATE = pygame.transform.smoothscale(NAND_GATE_IMAGE, (128, 64))
NOR_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "NORGate.png")).convert_alpha()
NOR_GATE = pygame.transform.smoothscale(NOR_GATE_IMAGE, (128, 64))
XOR_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "XORGate.png")).convert_alpha()
XOR_GATE = pygame.transform.smoothscale(XOR_GATE_IMAGE, (128, 64))

#SWITCH_IMAGE = pygame.image.load(os.path.join("Assets", "XORGate.png"))
#SWITCH = pygame.transform.smoothscale(XOR_GATE_IMAGE, (128, 64))

componentList = {"ANDGate", "ORGate", "NOTGate", "NANDGate",
                  "NORGate", "XORGate", "Switch"}

allSprites = pygame.sprite.Group()


# LOGIC GATES
# --------------------------------------------------------------------------------------------

class LogicGate(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.output = 0
    
    #def draw(self):
    #   SCREEN.blit(self.image, (self.x, self.y))

class BinaryGate(LogicGate):
    def __init__(self):
        super().__init__()
        self.inputA = False
        self.inputB = False

class UnaryGate(LogicGate):
    def __init__(self):
        super().__init__()
        self.input = False

class ANDGate(BinaryGate):
    def __init__(self, x, y):
        super().__init__()
        self.image = AND_GATE
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        pygame.draw.rect(SCREEN, (255,0,0), self.rect, 1)

class ORGate(BinaryGate):
    def __init__(self, x, y):
        super().__init__()
        self.image = OR_GATE
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


allSprites.add(ANDGate(0,0))
allSprites.add(ORGate(128,0))


def drawWindow():
    SCREEN.fill(WHITE)
    SCREEN.blit(BACKGROUND, (256,0))
    allSprites.draw(SCREEN)
    pygame.display.update()

def dragAndDrop():
    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Checks if the mouse is clicked above a component
            for component in componentList:
                if component.rect.collidepoint(mousePos):
                    component.dragging = True


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


# Creates buttons for all logic gates
#ANDGate = Button(pygame.image.load("andgate.png"))
#ANDGate.rect.x = 50
#ANDGate.rect.y = 20