# ALL CLASSES FOR LOGIC GATES
# --------------------------------------------------------------------------------------------
import pygame

class LogicGate(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

    def test(self):
        print(self.groups)

class ANDGate(LogicGate):
    def __init__(self, group):
        super().__init__(group)
    
    def test(self):
        print(self.groups)