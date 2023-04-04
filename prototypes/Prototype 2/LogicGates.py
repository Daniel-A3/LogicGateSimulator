# ALL CLASSES FOR LOGIC GATES
# --------------------------------------------------------------------------------------------
import pygame

# Superclass for all logic gates
class LogicGate(pygame.sprite.Sprite):
    def __init__(self, image, name):
        # Inherits from the sprite class
        pygame.sprite.Sprite.__init__(self)
        # Resizes the image and uses a smooth scaling algorithm for better quality
        self.image = pygame.transform.smoothscale(image, (128, 64))
        self.rect = self.image.get_rect()
        self.name = name
    
    count = 0

# Binary gates have two inputs
class BinaryGate(LogicGate):
    def __init__(self, image, name):
        LogicGate.__init__(self, image, name)
        super().__init__(image, name)

# Unary gates have one input - NOT gate
class UnaryGate(LogicGate):
    def __init__(self, image, name):
        LogicGate.__init__(self, image, name)
        super().__init__(image, name)

class ANDGate(BinaryGate):
    def __init__(self, image, name):
        LogicGate.__init__(self, image, name)
        super().__init__(image, name)
        self.rect.x = 0
        self.rect.y = 125
        

class ORGate(BinaryGate):
    def __init__(self, image, name):
        LogicGate.__init__(self, image, name)
        super().__init__(image, name)
        self.rect.x = 128
        self.rect.y = 125
        

class NOTGate(UnaryGate):
    def __init__(self, image, name):
        UnaryGate.__init__(self, image, name)
        super().__init__(image, name)
        self.rect.x = 0
        self.rect.y = 250
        

class NANDGate(BinaryGate):
    def __init__(self, image, name):
        LogicGate.__init__(self, image, name)
        super().__init__(image, name)
        self.rect.x = 128
        self.rect.y = 250
        

class NORGate(BinaryGate):
    def __init__(self, image, name):
        LogicGate.__init__(self, image, name)
        super().__init__(image, name)
        self.rect.x = 0
        self.rect.y = 375
        

class XORGate(BinaryGate):
    def __init__(self, image, name):
        LogicGate.__init__(self, image, name)
        super().__init__(image, name)
        self.rect.x = 128
        self.rect.y = 375