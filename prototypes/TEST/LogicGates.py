# ALL CLASSES FOR LOGIC GATES
# --------------------------------------------------------------------------------------------
import pygame

logicGateSprites = pygame.sprite.Group()

class LogicGate(pygame.sprite.Sprite):
    def __init__(self, *groups: logicGateSprites):
        super().__init__(*groups)