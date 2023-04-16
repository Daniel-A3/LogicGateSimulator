# PROTOTYPE 4 OF THE LOGIC GATE SIMULATOR
# THIS PROTOTYPE ADDES SOCKETS AND WIRE CONNECTIVITY FUNCTIONALITY

import pygame, os
from LogicGates import ANDGate, ORGate, NOTGate, NANDGate, NORGate, XORGate

# General setup
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

# This sprite group holds all of the logic gates
sidebarSprites = pygame.sprite.Group()
# This sprite group holds all of the sockets of each logic gate
allSocketSprites = pygame.sprite.Group()
# This sprite group holds all connected wires
allWireSprites = pygame.sprite.Group()


# WIRE CLASS
# --------------------------------------------------------------------------------------------
#
class Wire(pygame.sprite.Sprite):
    def __init__(self, start, end):
        pygame.sprite.Sprite.__init__(self)
        self.start = start
        self.end = end
        self.color = (0, 0, 0)
        self.width = 4

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.start, self.end, self.width)


# MOUSE CURSOR CLASS
# --------------------------------------------------------------------------------------------
#
class MouseCursor(pygame.sprite.Sprite):
    carryList = []
    sourceSocketList = []
    endSocketList = []

    sourceSocket = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #self.screen = screen

        # Creates a rect object for the mouse cursor
        self.rect = pygame.Rect(0, 0, 20, 20)


    # Updates the position of the mouse and any object it is dragging
    def update(self):
        #sourceSocket = None
        
        # x and y position of the mouse cursor
        self.xPos, self.yPos = pygame.mouse.get_pos()

        # Finds the offset of how much the mouse was moved
        offsetX = self.rect.x - self.xPos
        offsetY = self.rect.y - self.yPos

        # DRAG WIRE FROM SOURCE SOCKET
        # In this case it stops the component from moving, this lets the user drag out a wire from the socket.
        if self.sourceSocketList != []:
            # Drag and dropping, and connecting new wires
            for socket in self.sourceSocketList:
                self.sourceSocket = socket
                # Creates a wire and sets the end of the wire to the mouse position
                socket.connectedWire = Wire([socket.rect.x + 8, socket.rect.y + 8], [self.xPos, self.yPos])
                socket.connectedWire.draw(SCREEN)
                # This break is necessary so that you can drag a wire from one component at a time.
                break

        # CREATE THE FINAL CONNECTED WIRE
        # Creates a new instance of the final connected wire that is added to a sprite group and then drawn
        # every game loop.
        elif self.endSocketList != []:
            for endSocket in self.endSocketList:
                endSocket.connectedWire = Wire([self.sourceSocket.rect.x + 8, self.sourceSocket.rect.y + 8], [self.xPos, self.yPos])
                allWireSprites.add(endSocket.connectedWire)
                # This break is necessary so that you can only create one wire at a time.
                break

        # DRAG AND DROP COMPONENTS
        # If the sourceSocketList and endSocketList is empty, the user isnt trying to make a new wire, 
        # so it lets them drag the actual component.
        else:
            # Drag and dropping logic gates + sockets
            for component in self.carryList:
                # Moves the logic gate with the mouse
                component.rect.x -= offsetX
                component.rect.y -= offsetY

                # Moves the socket outputs with the mouse
                component.output.rect.x -= offsetX
                component.output.rect.y -= offsetY

                # Moves the socket inputs with the mouse
                for input in component.inputList:
                    input.rect.x -= offsetX
                    input.rect.y -= offsetY
                # This break is necessary so that you can only pick up one component at a time.
                break
            
        self.rect.x, self.rect.y = self.xPos, self.yPos


# SIDEBAR MENU CLASS
# --------------------------------------------------------------------------------------------
#
class SidebarMenu:
    dragging = False
    def __init__(self):
        self.border = 256

    # This makes sure that the logic gates aren't needlessly instantiated every game loop,
    # new instances are made when the user drags a component from the sidebar menu.
    def instantiate(self):
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
            allSocketSprites.add(component.output)
            # Input list is required so that both NOT gate and other gates sockets can be drawn at once.
            # This is because NOT gate only requires one input socket while the others require two.
            for input in component.inputList:
                allSocketSprites.add(input)

    def drawSprites(self):
        # Draws all of the logic gates
        sidebarSprites.draw(SCREEN)
        # Draws all of the sockets
        allSocketSprites.draw(SCREEN)
        # Draws all of the wires
        for wire in allWireSprites:
            wire.draw(SCREEN)


# MAIN FUNCTION
# --------------------------------------------------------------------------------------------
# This includes the main game loop which repeats every game cycle
def main():
    run = True
    # Creates an instance of the sidebarMenu class
    sidebar = SidebarMenu()
    # Creates an instance of the MouseCursor class - represents the users mouse
    mouse = MouseCursor()

    sidebar.instantiate()
    
    # Main game loop
    while run == True:

        for event in pygame.event.get():

            # Checks if pygame was quit
            if event.type == pygame.QUIT:
                run = False

            # Checks if the mouse button is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse.endSocketList = []
                sidebar.dragging = True
                # Adds all collided sprites to the carryList
                mouse.carryList = pygame.sprite.spritecollide(mouse, sidebarSprites, False)
                # Check if any socket sprites collide with mouse position, if true then add to sourceSocketList
                mouse.sourceSocketList = pygame.sprite.spritecollide(mouse, allSocketSprites, False)
    
            # Checks if the mouse button was released
            elif event.type == pygame.MOUSEBUTTONUP:
                # Lets the user connect a wire coming out of one socket to another socket
                # Checks if the user is currently dragging a wire
                if mouse.sourceSocketList != []:
                    mouse.endSocketList = pygame.sprite.spritecollide(mouse, allSocketSprites, False)
                # When you let go off clicking the mouse the carryList is emptied
                mouse.carryList = []
                mouse.sourceSocketList = []

        # Fills the screen with the colour white
        SCREEN.fill((255, 255, 255))
        # Draws the background onto the screen
        SCREEN.blit(BACKGROUND, (256,0))
    
        # Regenerate all components in the sidebar menu.
        # This is so that if they are drag and dropped, a new instance appears
        # in its original place.
        if mouse.carryList != [] and sidebar.dragging == True:
            sidebar.instantiate()
            # This makes sure that only ONE instance is made of each logic gate, this minimises
            # the performance impact.
            sidebar.dragging = False

        # Draws the logic gates, sockets and wires.
        sidebar.drawSprites()

        mouse.update()

        # Update the display
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()

if __name__ == "__main__":
    main()



"""
PLAN FOR IMPLEMENTING WIRE CONNECTIVITY:

1. If dragging wire, and mouse button is released, add all collided socket sprites to a list.
2. For the first sprite in the list, labelled endSocket, instantiate an instance of the Wire class 
with the start and end coordinates as startSockets, endSockets rect.x,y values respectively.
3. Add the new instance to a sprite group containing all wires.
4. Draw all of the final connected wires once every game loop.


MANAGING CONDITIONS FOR WIRE CONNECTIVITY AND INVALID CONNECTIONS
This will make sure that wires do not come out of a socket and connect to the same socket, 
a socket of the same component, or a socket that already has a wire connected to it.

1. 

"""