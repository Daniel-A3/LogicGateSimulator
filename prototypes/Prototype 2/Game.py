# GAME CLASS
# --------------------------------------------------------------------------------------------
import pygame
import LogicGates
from LogicGates import logicGateSprites
import dragAndDrop

WIDTH, HEIGHT = 1332, 802
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

class Game:
    def __init__(self, WIDTH, HEIGHT):
        pass

    def drawWindow():
        SCREEN.fill(WHITE)
        SCREEN.blit(BACKGROUND, (256,0))
        logicGateSprites.draw(SCREEN)
        pygame.display.update()

    # The main game loop
    def gameLoop():
        for event in pygame.event.get():
            # Quits the game if it is exited
            if event.type == pygame.QUIT:
                run = False
        for component in logicGateSprites:
            print(component)
            dragAndDrop(component)