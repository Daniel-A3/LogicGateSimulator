# ALL CLASSES FOR LOGIC GATES
# --------------------------------------------------------------------------------------------
import pygame

pygame.init()

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

# Binary gates have two inputs
class BinaryGate(LogicGate):
    def __init__(self, image, name, x, y):
        LogicGate.__init__(self, image, name, x, y)
        super().__init__(image, name, x, y)
        #self.topSocket = 


# Unary gates have one input - NOT gate
class UnaryGate(LogicGate):
    def __init__(self, image, name, x, y):
        LogicGate.__init__(self, image, name, x, y)
        super().__init__(image, name, x, y)

class ANDGate(BinaryGate):
    def __init__(self, image, name, x, y):
        LogicGate.__init__(self, image, name, x, y)
        super().__init__(image, name, x, y)
        

class ORGate(BinaryGate):
    def __init__(self, image, name, x, y):
        LogicGate.__init__(self, image, name, x, y)
        super().__init__(image, name, x, y)
        

class NOTGate(UnaryGate):
    def __init__(self, image, name, x, y):
        UnaryGate.__init__(self, image, name, x, y)
        super().__init__(image, name, x, y)
        

class NANDGate(BinaryGate):
    def __init__(self, image, name, x, y):
        LogicGate.__init__(self, image, name, x, y)
        super().__init__(image, name, x, y)
        

class NORGate(BinaryGate):
    def __init__(self, image, name, x, y):
        LogicGate.__init__(self, image, name, x, y)
        super().__init__(image, name, x, y)
        

class XORGate(BinaryGate):
    def __init__(self, image, name, x, y):
        LogicGate.__init__(self, image, name, x, y)
        super().__init__(image, name, x, y)


# Socket Class for connecting components
class Socket(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, gate, index, is_input):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.gate = gate
        self.index = index
        self.is_input = is_input
        self.color = (0, 0, 0) # default color of socket
        self.is_connected = False
        self.connected_wire = None

    def update(self):
        # draw socket on the screen
        pygame.draw.rect(self.image, self.color, [0, 0, self.rect.width, self.rect.height])

    def connect_wire(self, wire):
        # connect wire to the socket
        self.is_connected = True
        self.connected_wire = wire
        self.color = (255, 0, 0) # set color to red when connected