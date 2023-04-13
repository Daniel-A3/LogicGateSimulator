import pygame, os
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

logicGateSprites = pygame.sprite.Group()
sidebarSprites = pygame.sprite.Group()

dragging = False

# SIDEBAR MENU CLASS
# --------------------------------------------------------------------------------------------
class SidebarMenu():
    def __init__(self):
        self.border = 256

    # Draws new instances of the components each in their designated position in the sidebar
    def drawSprites(self):
        andGate = ANDGate(AND_GATE_IMAGE, "ANDGate", 0, 150)
        orGate = ORGate(OR_GATE_IMAGE, "ORGate", 128, 150)
        notGate = NOTGate(NOT_GATE_IMAGE, "NOTGate", 0, 250)
        nandGate = NANDGate(NAND_GATE_IMAGE, "NANDGate", 128, 250)
        norGate = NORGate(NOR_GATE_IMAGE, "NORGate", 0, 350)
        xorGate = XORGate(XOR_GATE_IMAGE, "XORGate", 128, 350)

        componentList = [andGate, orGate, notGate, nandGate, norGate, xorGate]

        for component in componentList:
            sidebarSprites.add(component)
            logicGateSprites.add(component)

        sidebarSprites.draw(SCREEN)

def main():
    run = True
    # Creates an instance of the sidebarMenu class
    sidebar = SidebarMenu()
    # Creates an instance of the MouseCursor class - represents the users mouse
    mouse = MouseCursor()
    
    # Main game loop
    while run == True:
        # Checks if the program was quit
        
        mouse.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Adds all collided sprites to the carryList
                mouse.carryList = pygame.sprite.spritecollide(mouse, logicGateSprites, False)
    
            elif event.type == pygame.MOUSEBUTTONUP:
                # When you let go off clicking the mouse the carryList is emptied
                mouse.carryList = []
        
        # Fills the screen with the colour white
        SCREEN.fill((255, 255, 255))
        # Draws the background onto the screen
        SCREEN.blit(BACKGROUND, (256,0))
        
        # Regenerate all components in the sidebar menu.
        # This is so that if they are drag and dropped, a new instance appears
        # in its original place.
        sidebar.drawSprites()
        # Draws all the other gates that have been dragged onto the workspace
        logicGateSprites.draw(SCREEN)

        # Update the display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()

"""
# Sprites for all logic gate components stored in this group
logicGateSprites = pygame.sprite.Group()
# Sprites that are drag and dropped onto the workspace join this group
draggedGroup = pygame.sprite.Group()
# Creates a new copy of the sprites each time one is dragged away from the sidebar menu
sidebarSprites = pygame.sprite.Group()
# Makes sure the sprites that were drag and dropped before are not deleted when
# a new instance of the same component is dragged.
placedSprites = pygame.sprite.Group()
"""
"""
def dragAndDrop(logicGateSprites, mouse, classDict, imageDict, dragging):

    if pygame.mouse.get_pressed()[0]:
        # Checks if any of the components were clicked
        for component in logicGateSprites:
            if dragging == False:
                if component.rect.collidepoint(mouse.xPos, mouse.yPos):
                    dragging = True

                    image = imageDict[component.name]
                    newClass = classDict[component.name]
                    newInstance = newClass(image, component.name)
                    
                    placedSprites.add(newInstance)
                    # Makes sure that only 1 component can be dragged at a time
                    if len(draggedGroup.sprites()) == 0:
                        draggedGroup.add(newInstance)
                    else:
                        draggedGroup.empty()
                        draggedGroup.add(newInstance)
        # Updates the position of the dragged component to the mouse position
        draggedGroup.sprites()[0].rect.center = mouse.xPos, mouse.yPos
        
        print(placedSprites.sprites())
    else:
        dragging = False
"""
"""
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

    sidebarList = [andGateOriginal, orGateOriginal, notGateOriginal, 
                   nandGateOriginal, norGateOriginal, xorGateOriginal]

    # Adds all logic gate instances to the sprite group
    
    for component in componentList:
        logicGateSprites.add(component)
    
    for component in sidebarList:
        sidebarSprites.add(component)
    """