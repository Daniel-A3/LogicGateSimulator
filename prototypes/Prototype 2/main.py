import pygame, os
from Game import Game
from MouseCursor import MouseCursor
from LogicGates import ANDGate, ORGate, NOTGate, NANDGate, NORGate, XORGate

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
# Creates a new copy of the sprites each time one is dragged away from the sidebar menu
sidebarSprites = pygame.sprite.Group()
# Makes sure the sprites that were drag and dropped before are not deleted when
# a new instance of the same component is dragged.
placedSprites = pygame.sprite.Group()

# DRAG AND DROP FUNCTION
# --------------------------------------------------------------------------------------------
def dragAndDrop(logicGateSprites, mouse, classDict, imageDict):

    if pygame.mouse.get_pressed()[0]:
        # Checks if any of the components were clicked
        for component in logicGateSprites:
            if component.rect.collidepoint(mouse.xPos, mouse.yPos):
                image = imageDict[component.name]
                newClass = classDict[component.name]
                newInstance = newClass(image, component.name)
                print(newInstance)
                # Makes sure that only 1 component can be dragged at a time
                if len(draggedGroup.sprites()) == 0:
                    draggedGroup.add(component)
                else:
                    draggedGroup.empty()
                    draggedGroup.add(component)
        # Updates the position of the dragged component to the mouse position
        draggedGroup.sprites()[0].rect.center = mouse.xPos, mouse.yPos
        placedSprites.add(draggedGroup.sprites()[0])
        print(placedSprites.sprites())

def main():
    # Creates an instance of the Game class - represents the current game running
    game = Game(WIDTH, HEIGHT, BACKGROUND, SCREEN)
    # Creates an instance of the MouseCursor class - represents the users mouse
    mouse = MouseCursor()
    
    # Creates an instance of all logic gates
    andGate = ANDGate(AND_GATE_IMAGE, "ANDGate")
    orGate = ORGate(OR_GATE_IMAGE, "ORGate")
    notGate = NOTGate(NOT_GATE_IMAGE, "NOTGate")
    nandGate = NANDGate(NAND_GATE_IMAGE, "NANDGate")
    norGate = NORGate(NOR_GATE_IMAGE, "NORGate")
    xorGate = XORGate(XOR_GATE_IMAGE, "XORGate")
    
    # Creates instances of gates that will replace ones that are dragged
    andGateOriginal = ANDGate(AND_GATE_IMAGE, "ANDGate")
    orGateOriginal = ORGate(OR_GATE_IMAGE, "ORGate")
    notGateOriginal = NOTGate(NOT_GATE_IMAGE, "NOTGate")
    nandGateOriginal = NANDGate(NAND_GATE_IMAGE, "NANDGate")
    norGateOriginal = NORGate(NOR_GATE_IMAGE, "NORGate")
    xorGateOriginal = XORGate(XOR_GATE_IMAGE, "XORGate")

    classDict = {"ANDGate" : ANDGate, "ORGate" : ORGate, "NOTGate" : NOTGate, 
                 "NANDGate" : NANDGate, "NORGate" : NORGate, "XORGate" : XORGate}
    
    imageDict = {"ANDGate" : AND_GATE_IMAGE, "ORGate" :  OR_GATE_IMAGE, "NOTGate" : NOT_GATE_IMAGE,
                  "NANDGate" : NAND_GATE_IMAGE, "NORGate" : NOR_GATE_IMAGE, "XORGate" : XOR_GATE_IMAGE}

    componentList = [andGate, orGate, notGate, nandGate, norGate, xorGate]

    sidebarList = [andGateOriginal, orGateOriginal, notGateOriginal, 
                   nandGateOriginal, norGateOriginal, xorGateOriginal]

    # Adds all logic gate instances to the sprite group
    
    for component in componentList:
        logicGateSprites.add(component)
    
    for component in sidebarList:
        sidebarSprites.add(component)

    # Draws the sprites onto the screen
    sidebarSprites.draw(SCREEN)

    # Main game loop
    while game.run == True:
        # Checks if the program was quit
        game.processEvents()
        
        mouse.update()
        # Tests mouse rect
        # pygame.draw.rect(SCREEN, (255, 0, 0), mouse.cursor)
        game.drawWindow()
        # Runs the drag and drop function
        # Allows the user to drag gates from the sidebar menu and drop 
        # them onto the workspace.
        dragAndDrop(logicGateSprites, mouse, classDict, imageDict)
        # Regenerate all components in the sidebar menu.
        # This is so that if they are drag and dropped, a new instance appears
        # in its original place.
        sidebarSprites.draw(SCREEN)
        logicGateSprites.draw(SCREEN)
        placedSprites.draw(SCREEN)

        # Update the display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()