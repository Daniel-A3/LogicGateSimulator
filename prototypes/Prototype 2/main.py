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

#SWITCH_IMAGE = pygame.image.load(os.path.join("Assets", "Switch.png")).convert_alpha()
#SWITCH = pygame.transform.smoothscale(SWITCH_IMAGE, (128, 64))

componentList = {"ANDGate", "ORGate", "NOTGate", "NANDGate",
                  "NORGate", "XORGate", "Switch"}

logicGates = pygame.sprite.Group()

# LOGIC GATES
# --------------------------------------------------------------------------------------------

class LogicGate(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.output = 0
        self.dragging = False
    
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
        pygame.sprite.Sprite.__init__(self, logicGates)
        self.image = AND_GATE
        #self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        pygame.draw.rect(SCREEN, (255,0,0), self.rect)

class ORGate(BinaryGate):
    def __init__(self, x, y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self, logicGates)
        self.image = OR_GATE
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        pygame.draw.rect(SCREEN, (255,0,0), self.rect)


def drawWindow():
    SCREEN.fill(WHITE)
    SCREEN.blit(BACKGROUND, (256,0))
    logicGates.draw(SCREEN)
    pygame.display.update()

def dragAndDrop(component):
    #mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # Checks if the mouse is clicked above a component
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Checks if its the right mouse button that is clicked
            if event.button == 1:
                if component.rect.collidepoint(event.pos):
                    component.dragging = True
                    mouseX, mouseY = event.pos
                    offsetX = component.rect.x - mouseX
                    offsetY = component.rect.y - mouseY

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Checks if it is the right mouse button that is released
            if event.button == 1:
                component.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if component.dragging == True:
                mouseX, mouseY = event.pos
                component.rect.x = mouseX + offsetX
                component.rect.y = mouseY + offsetY
                print("test")


def main():
    # The main game loop
    run = True
    while run:
        for event in pygame.event.get():
            # Quits the game if it is exited
            if event.type == pygame.QUIT:
                run = False
        for component in logicGates:
            print(component)
            dragAndDrop(component)

        drawWindow()
    
    logicGates.add(ANDGate(0,0))
    logicGates.add(ORGate(128,0))
    pygame.quit()

if __name__ == "__main__":
    main()