# ALL LOGIC GATE CLASSES
# --------------------------------------------------------------------------------------------
#-----Importing Libraries--------------
'''
pygame - 
Game -
'''
import pygame                  
import Game
from Game import SCREEN, AND_GATE, OR_GATE

#Loading images to use as sprites. Each image is a logic gate (AND, OR, NOT, etc.)
AND_GATE_IMAGE  = pygame.image.load(os.path.join("Assets", "ANDGate.png")).convert_alpha()
OR_GATE_IMAGE   = pygame.image.load(os.path.join("Assets", "ORGate.png")).convert_alpha()
NOT_GATE_IMAGE  = pygame.image.load(os.path.join("Assets", "NOTGate.png")).convert_alpha()
NOT_GATE        = pygame.transform.smoothscale(NOT_GATE_IMAGE, (128, 64))
NAND_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "NANDGate.png")).convert_alpha()
NAND_GATE       = pygame.transform.smoothscale(NAND_GATE_IMAGE, (128, 64))
NOR_GATE_IMAGE  = pygame.image.load(os.path.join("Assets", "NORGate.png")).convert_alpha()
NOR_GATE        = pygame.transform.smoothscale(NOR_GATE_IMAGE, (128, 64))
XOR_GATE_IMAGE  = pygame.image.load(os.path.join("Assets", "XORGate.png")).convert_alpha()
XOR_GATE        = pygame.transform.smoothscale(XOR_GATE_IMAGE, (128, 64))

#Creating a group to control all objects on the screen.
logicGateSprites = pygame.sprite.Group()

#----- Class
class LogicGate(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, logicGateSprites)
        self.output = 0
        self.dragging = False 

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
        pygame.sprite.Sprite.__init__(self, logicGateSprites)
        self.image = pygame.transform.smoothscale(AND_GATE_IMAGE, (128, 64))
        #self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        pygame.draw.rect(SCREEN, (255,0,0), self.rect)

class ORGate(BinaryGate):
    def __init__(self, x, y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self, logicGateSprites)
        self.image = OR_GATE = pygame.transform.smoothscale(OR_GATE_IMAGE, (128, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        pygame.draw.rect(SCREEN, (255,0,0), self.rect)