# ALL CLASSES FOR LOGIC GATES
# --------------------------------------------------------------------------------------------
import pygame

# Superclass for all logic gates
class LogicGate(pygame.sprite.Sprite):
    def __init__(self, image, name, x, y):
        # Inherits from the sprite class
        pygame.sprite.Sprite.__init__(self)
        # Resizes the image and uses a smooth scaling algorithm for better quality
        self.image = pygame.transform.smoothscale(image, (128, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
    
    count = 0

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