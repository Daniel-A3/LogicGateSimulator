# PROTOTYPE 3 OF THE LOGIC GATE SIMULATOR

import pygame, os
from MouseCursor import MouseCursor
from LogicGates import ANDGate, ORGate, NOTGate, NANDGate, NORGate, XORGate, Socket

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

# Loads each logic gate image, then uses a smoothscale algorithm to transform its size
# This is so that all of the images are the same and right size, while also retaining its image quality.
AND_GATE_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "ANDGate.png")).convert_alpha(), (128, 64))
OR_GATE_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "ORGate.png")).convert_alpha(), (128, 64))
NOT_GATE_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "NOTGate.png")).convert_alpha(), (128, 64))
NAND_GATE_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "NANDGate.png")).convert_alpha(), (128, 64))
NOR_GATE_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "NORGate.png")).convert_alpha(), (128, 64))
XOR_GATE_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "XORGate.png")).convert_alpha(), (128, 64))

logicGateSprites = pygame.sprite.Group()
sidebarSprites = pygame.sprite.Group()

allSocketSprites = pygame.sprite.Group()

allWireSprites = pygame.sprite.Group()

# SIDEBAR MENU CLASS
# --------------------------------------------------------------------------------------------
class SidebarMenu:
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
        # Adds the newly instantiated components to their respective sprite groups
        for component in componentList:
            sidebarSprites.add(component)
            logicGateSprites.add(component)

        sidebarSprites.draw(SCREEN)

class Wire(pygame.sprite.Sprite):
    def __init__(self, start, end):
        pygame.sprite.Sprite.__init__(self)
        self.start = start
        self.end = end
        self.color = (0, 0, 0)
        self.width = 4

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.start, self.end, self.width)

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

            # Checks if pygame was quit
            if event.type == pygame.QUIT:
                run = False

            # Checks if the mouse button is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Adds all collided sprites to the carryList
                mouse.carryList = pygame.sprite.spritecollide(mouse, logicGateSprites, False)

            # Checks if the mouse button was released
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

        #newWire = Wire((400,100), (800,200))
        #newWire.draw(SCREEN)
        for component in logicGateSprites:
            for input in component.inputList:
                input.update()
        
        test = Socket(500, 100, 15, 15, "ANDGate", True)

        allSocketSprites.add(test)
        allSocketSprites.draw(SCREEN)

        # Update the display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()