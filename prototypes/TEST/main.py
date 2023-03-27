import pygame, os
from Game import Game
from MouseCursor import MouseCursor
from LogicGates import ANDGate, ORGate, NOTGate, NANDGate, NORGate, XORGate
from dragAndDrop import dragAndDrop

#General setup
pygame.init()
clock = pygame.time.Clock()

# Sets the caption of the program
pygame.display.set_caption("OneOrZero")

# Sets the width and height of the program
WIDTH, HEIGHT = 1332, 802

#Create the display surface
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Loads the background
BACKGROUND = pygame.image.load(os.path.join("Assets", "backgroundGrid.png"))

# Loads all of the images
AND_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "ANDGate.png"))
OR_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "ORGate.png"))
NOT_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "NOTGate.png"))
NAND_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "NANDGate.png"))
NOR_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "NORGate.png"))
XOR_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "XORGate.png"))

# Sprites for all logic gate components stored in this group
logicGateSprites = pygame.sprite.Group()
# Sprites that are drag and dropped onto the workspace join this group
draggedGroup = pygame.sprite.Group()

def main():
    # Creates an instance of the Game class - represents the current game running
    game = Game(WIDTH, HEIGHT, BACKGROUND, SCREEN)
    # Creates an instance of the MouseCursor class - represents the users mouse
    mouse = MouseCursor()

    # Creates an instance of all logic gates
    andGate = ANDGate(AND_GATE_IMAGE)
    orGate = ORGate(OR_GATE_IMAGE)
    notGate = NOTGate(NOT_GATE_IMAGE)
    nandGate = NANDGate(NAND_GATE_IMAGE)
    norGate = NORGate(NOR_GATE_IMAGE)
    xorGate = XORGate(XOR_GATE_IMAGE)

    componentList = [andGate, orGate, notGate, nandGate, norGate, xorGate]

    # Adds all logic gate instances to the sprite group
    for component in componentList:
        logicGateSprites.add(component)
    
    logicGateSprites.draw(SCREEN)
    
    game.drawWindow()

    # Main game loop
    while game.run == True:
        # Checks if the program was quit
        game.processEvents()
        
        mouse.update()
        pygame.draw.rect(SCREEN, (255, 0, 0), mouse.cursor)
        # Runs the drag and drop function
        # Allows the user to drag gates from the sidebar menu and drop 
        # them onto the workspace.
        dragAndDrop(draggedGroup, logicGateSprites, mouse)
        # Regenerate all components in the sidebar menu.
        # This is so that if they are drag and dropped, a new instance appears
        # in its original place.
        logicGateSprites.draw(SCREEN)

        # Update the display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()