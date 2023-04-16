# ALL CLASSES FOR LOGIC GATES
# --------------------------------------------------------------------------------------------
import pygame

pygame.init()

# Socket Class for connecting components
class Socket(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, gate, isInput):
        super().__init__()
        self.image = pygame.Surface([width, height])

        # FOR TESTING PURPOSES
        self.image.fill([153, 204, 255])

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.gate = gate
        self.isInput = isInput

        self.isConnected = False
        self.connectedWire = None

    def connect_wire(self, wire):
        # connect wire to the socket
        self.isConnected = True
        self.connectedWire = wire
        self.color = (255, 0, 0)

# Superclass for all logic gates
class LogicGate(pygame.sprite.Sprite):
    def __init__(self, image, name, x, y):
        # Inherits from the sprite class
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name

        if self.name == "NOTGate":
            self.input = Socket(x, (y + 25), 15, 15, name, True)
            self.inputList = [self.input]
        else:
            self.inputA = Socket(x, (y + 11), 15, 15, name, True)
            self.inputB = Socket(x, (y + 38), 15, 15, name, True)
            self.inputList = [self.inputA, self.inputB]
        
        self.output = Socket((x + 108), (y + 25), 15, 15, name, False)

class ANDGate(LogicGate):
    def __init__(self, image, name, x, y):
        super().__init__(image, name, x, y)      

class ORGate(LogicGate):
    def __init__(self, image, name, x, y):
        super().__init__(image, name, x, y)
        
class NOTGate(LogicGate):
    def __init__(self, image, name, x, y):
        super().__init__(image, name, x, y)     

class NANDGate(LogicGate):
    def __init__(self, image, name, x, y):
        super().__init__(image, name, x, y)
        
class NORGate(LogicGate):
    def __init__(self, image, name, x, y):
        super().__init__(image, name, x, y)
        
class XORGate(LogicGate):
    def __init__(self, image, name, x, y):
        super().__init__(image, name, x, y)

"""
# Binary gates have two inputs
class BinaryGate(LogicGate):
    def __init__(self, image, name, x, y):
        LogicGate.__init__(self, image, name, x, y)
        super().__init__(image, name, x, y)


# Unary gates have one input - NOT gate
class UnaryGate(LogicGate):
    def __init__(self, image, name, x, y):
        LogicGate.__init__(self, image, name, x, y)
        super().__init__(image, name, x, y)

        self.input = Socket(0, 0, 20, 20, self, i, True)
"""