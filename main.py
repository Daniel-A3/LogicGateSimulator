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

#SWITCH_IMAGE = pygame.image.load(os.path.join("Assets", "XORGate.png"))
#SWITCH = pygame.transform.smoothscale(XOR_GATE_IMAGE, (128, 64))

componentDict = {"AND" : "AND_GATE", "OR" : "OR_GATE", "NOT" : "NOT_GATE", "NAND" : "NAND_GATE",
                  "NOR" : "NOR_GATE", "XOR" : "XOR_GATE", "SWITCH" : "SWITCH"}

# LOGIC GATES
# --------------------------------------------------------------------------------------------

class LogicGate(pygame.sprite.Sprite):
    def __init__(self, gate):
        pygame.sprite.Sprite.__init__(self)
        self.output = 0
        self.gateType = gate
        self.image = componentDict[self.gateType]
    
    def draw(self):
        SCREEN.blit(self.image, (self.x, self.y))

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
    def __init__(self):
        super().__init__()
        self.image = AND_GATE_IMAGE
        self.x = 0
        self.y = 0

def drawWindow():
    SCREEN.fill(WHITE)
    SCREEN.blit(BACKGROUND, (250,0))
    andGate = ANDGate()
    andGate.draw()
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