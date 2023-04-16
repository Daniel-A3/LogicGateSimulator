# LOGIC GATE MODULE
# --------------------------------------------------------------------------------------------
# This module contains the Socket class and logic gate classes for all different types, 
# as well as the LogicGate superclass.
import pygame

pygame.init()


# SOCKET CLASS
# --------------------------------------------------------------------------------------------
# Represents sockets, the input and outputs of components. This allows connectivity.
# Each logic gate has input socket/s, and an output socket, each can be connected to a wire
# object of the Wire Class.
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
        self.connected = False

        self.inputWire = None
        self.outputWire = None


# LOGIC GATE CLASS
# --------------------------------------------------------------------------------------------
# Superclass for all types of logic gates.
# Defines its x and y position, as well as input and output sockets.
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
            self.input = Socket(x, (y + 25), 15, 15, self, True)
            self.inputList = [self.input]
        else:
            self.inputA = Socket(x, (y + 11), 15, 15, self, True)
            self.inputB = Socket(x, (y + 38), 15, 15, self, True)
            self.inputList = [self.inputA, self.inputB]
        
        self.output = Socket((x + 108), (y + 25), 15, 15, self, False)

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
