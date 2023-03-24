import pygame, os
import LogicGates
from LogicGates import logicGateSprites
from LogicGates import ANDGate
from LogicGates import ORGate
import Game

pygame.init()

pygame.display.set_caption("OneOrZero")
WHITE = (255, 255, 255)

BACKGROUND = pygame.image.load(os.path.join("Assets", "backgroundGrid.png"))

FPS = 60

#SWITCH_IMAGE = pygame.image.load(os.path.join("Assets", "Switch.png")).convert_alpha()
#SWITCH = pygame.transform.smoothscale(SWITCH_IMAGE, (128, 64))

componentList = ["ANDGate", "ORGate", "NOTGate", "NANDGate", "NORGate", "XORGate", "Switch"]

def main():

    game = Game(1332, 802)

    # The main game loop
    run = True
    while run:
        game.drawWindow()
        game.gameLoop()
    
    andGate = ANDGate(0,0)
    orGate = ORGate(128,0)

    logicGateSprites.add(andGate)
    logicGateSprites.add(orGate)
    pygame.quit()

if __name__ == "__main__":
    main()