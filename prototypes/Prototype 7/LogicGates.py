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

        self.image.fill([153, 204, 255])

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.gate = gate
        self.isInput = isInput
        self.connected = False

        self.inputWire = None
        self.outputWires = []
        self.current = False


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
    
    # POLYMORPHISM
    # Every logic gate uses this function, and overrides it to suit its own logical function.
    # The default logic chosen is the OR gate logic since it is the most simple and is useful
    # during testing to show current flow freely through logic gates.
    def performLogic(self):
        if self.inputA.current or self.inputB.current:
            self.output.current = True
        else:
            self.output.current = False

# INHERITANCE
# Each different logic gate inherits from the Logic Gate superclass
class ANDGate(LogicGate):
    def __init__(self, image, name, x, y):
        super().__init__(image, name, x, y) 

    def performLogic(self):
        if self.inputA.current and self.inputB.current:
            self.output.current = True
        else:
            self.output.current = False  

class ORGate(LogicGate):
    def __init__(self, image, name, x, y):
        super().__init__(image, name, x, y)
    
    def performLogic(self):
        if self.inputA.current or self.inputB.current:
            self.output.current = True
        else:
            self.output.current = False  
        
class NOTGate(LogicGate):
    def __init__(self, image, name, x, y):
        super().__init__(image, name, x, y)  

    def performLogic(self):
        if self.input.current:
            self.output.current = False
        else:
            self.output.current = True  

class NANDGate(LogicGate):
    def __init__(self, image, name, x, y):
        super().__init__(image, name, x, y)
    
    def performLogic(self):
        if not (self.inputA.current and self.inputB.current):
            self.output.current = True
        else:
            self.output.current = False  
        
class NORGate(LogicGate):
    def __init__(self, image, name, x, y):
        super().__init__(image, name, x, y)
    
    def performLogic(self):
        if not self.inputA.current and not self.inputB.current:
            self.output.current = True
        else:
            self.output.current = False  
        
class XORGate(LogicGate):
    def __init__(self, image, name, x, y):
        super().__init__(image, name, x, y)
    
    def performLogic(self):
        if (self.inputA.current or self.inputB.current) and (not self.inputA.current or not self.inputB.current):
            self.output.current = True
        else:
            self.output.current = False  


# SWITCH CLASS
# --------------------------------------------------------------------------------------------
# Represents the switch that turns current on or off to the logic circuit

class Switch(pygame.sprite.Sprite):
    def __init__(self, image, x, y, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.clicked = False

        self.switchedOn = False

        self.output = Socket((x + 84), (y + 15), 15, 15, self, False)
    
    def update(self, onImage, offImage):
        if self.switchedOn == True:
            self.image = onImage
            self.output.current = True
        else:
            self.image = offImage
            self.output.current = False

# LIGHT BULB CLASS
# --------------------------------------------------------------------------------------------
# Represents the wires that connect different logic gate components together
class Bulb(pygame.sprite.Sprite):
    def __init__(self, image, x, y, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name

        self.input = Socket((x + 31), (y + 56), 15, 15, self, True)
    
    def update(self, onImage, offImage):
        if self.input.current == True:
            self.image = onImage
        else:
            self.image = offImage
        