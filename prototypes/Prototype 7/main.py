# PROTOTYPE 7
# THIS PROTOTYPE IMPLEMENTS THE BIN, INFORMATION MENU AND MENU SCREEN.
# THE BIN LETS THE USER DELETE LOGIC GATES AND CONNECTED WIRES.
# THE INFORMATION MENU TELLS THE USER HOW TO USE THE PROGRAM AND HAS EDUCATIONAL INFORMATION ON EACH LOGIC GATE.

import pygame, os
from LogicGates import ANDGate, ORGate, NOTGate, NANDGate, NORGate, XORGate, Switch, Bulb

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

# Loads each components image, then uses a smoothscale algorithm to transform its size
# This is so that all of the images are the same and right size, while also retaining its image quality.
# .convert_alpha is used for performance reasons.
AND_GATE_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "ANDGate.png")).convert_alpha(), (128, 64))
OR_GATE_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "ORGate.png")).convert_alpha(), (128, 64))
NOT_GATE_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "NOTGate.png")).convert_alpha(), (128, 64))
NAND_GATE_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "NANDGate.png")).convert_alpha(), (128, 64))
NOR_GATE_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "NORGate.png")).convert_alpha(), (128, 64))
XOR_GATE_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "XORGate.png")).convert_alpha(), (128, 64))

ON_SWITCH_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "onSwitch.png")).convert_alpha(), (90, 45))
OFF_SWITCH_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "offSwitch.png")).convert_alpha(), (90, 45))

ON_BULB_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "onBulb.png")).convert_alpha(), (75, 75))
OFF_BULB_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "offBulb.png")).convert_alpha(), (75, 75))

INFORMATION_MENU_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "informationMenu.png")).convert_alpha(), (90,90))
INFORMATION_MENU_HOVER_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "informationMenuOnHover.png")).convert_alpha(), (90,90))

LOGO_IMAGE = pygame.transform.smoothscale(pygame.image.load(os.path.join("Assets", "logo.png")).convert_alpha(), (260, 150))

# This sprite group holds all of the components
sidebarSprites = pygame.sprite.Group()
# This sprite group holds all of the logic gates
allLogicGateSprites = pygame.sprite.Group()
# This sprite group holds all of the sockets of each logic gate
allSocketSprites = pygame.sprite.Group()
# This sprite group holds all connected wires
allWireSprites = pygame.sprite.Group()
allLogicGatesList = []


# INFORMATION MENU CLASS
# --------------------------------------------------------------------------------------------
# Represents the information menu, displays information on how to use the logic gate simulator,
# and how each component works.
class InformationMenu(pygame.sprite.Sprite):
    clicked = False
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = "menu"
    
    # Expands the menu
    def show(self):
        pass

# WIRE CLASS
# --------------------------------------------------------------------------------------------
# Represents the wires that connect different logic gate components together
class Wire(pygame.sprite.Sprite):
    def __init__(self, start, end):
        pygame.sprite.Sprite.__init__(self)
        self.start = start
        self.end = end
        self.color = (0, 0, 0)
        self.width = 4

        self.startSocket = None
        self.endSocket = None

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.start, self.end, self.width)


# MOUSE CURSOR CLASS
# --------------------------------------------------------------------------------------------
# Represents the users mouse cursor.
# Carries out the drag and drop functionality, and updates the position of the dragged logic 
# gate and its corresponding input,output sockets and input,output wires. This allows wires 
# and sockets to stick to their components.
# Also handles the creation of new wires, and prevents invalid wire connections.
class MouseCursor(pygame.sprite.Sprite):
    carryList = []
    sourceSocketList = []
    endSocketList = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sourceSocket = None

        # Creates a rect object for the mouse cursor
        self.rect = pygame.Rect(0, 0, 5, 5)
        self.offsetX = 0
        self.offsetY = 0

    # Updates the position of the mouse and any object it is dragging
    def update(self):
        
        # x and y position of the mouse cursor
        self.xPos, self.yPos = pygame.mouse.get_pos()

        # Finds the offset of how much the mouse was moved
        self.offsetX = self.rect.x - self.xPos
        self.offsetY = self.rect.y - self.yPos

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
        # Creates a new instance of the final connected wire that is added to a sprite group and then draws it every game loop.
        # Also checks and prevents invalid wire connections.
        elif self.endSocketList != []:

            validConnection = True

            # Checks if the wire is connected to the same gate.
            if self.endSocketList[0].gate == self.sourceSocket.gate:
                validConnection = False

            # Checks if an input socket already has a wire connected. (Can't have multiple inputs)
            elif self.endSocketList[0].connected:
                validConnection = False

            # Checks if theyre both input sockets. (Can't connect an input to an input)
            elif self.endSocketList[0].isInput and self.sourceSocket.isInput:
                validConnection = False
            
            # Checks if theyre both output sockets. (Can't connect an output to an output)
            elif (not self.endSocketList[0].isInput) and (not self.sourceSocket.isInput):
                validConnection = False
            
            elif validConnection:
                # Creates a new instance of the wire class
                wire = Wire([self.sourceSocket.rect.x + 8, self.sourceSocket.rect.y + 8], [self.xPos, self.yPos])
                self.sourceSocket.outputWires.append(wire)
                self.sourceSocket.connected = True

                # These two lines link the wires to their respective start and end sockets.
                wire.startSocket = self.sourceSocket
                wire.endSocket = self.endSocketList[0]
        
                for wire in self.sourceSocket.outputWires:
                    allWireSprites.add(wire)

                for endSocket in self.endSocketList:
                    # This is necesary as an output socket can have multiple wires
                    endSocket.inputWire = self.sourceSocket.outputWires[-1]
                    endSocket.connected = True
                    # This break is necessary so that you can only create one input wire at a time.
                    break

        # DRAG AND DROP COMPONENTS
        # If the sourceSocketList and endSocketList is empty, the user isnt trying to make a new wire, 
        # so it lets them drag the actual component.
        # Also makes sure wires to stick to the end of sockets and move with their respective logic gate component when dragged.
        else:
            # Drag and dropping logic gates + moves wires and sockets with its corresponding component
            for component in self.carryList:
                # The information menu cannot be drag and dropped, it is a button that doesnt move.
                if component.name == "menu":
                    break
                
                # Moves the logic gate component with the mouse
                component.rect.x -= self.offsetX
                component.rect.y -= self.offsetY


                if component.name == "switch":
                    # Moves the socket outputs with the mouse
                    component.output.rect.x -= self.offsetX
                    component.output.rect.y -= self.offsetY

                    # Moves any wires connected to the components output socket with the component when dragged.
                    if component.output.connected:
                        for wire in component.output.outputWires:
                            wire.start[0] -= self.offsetX
                            wire.start[1] -= self.offsetY

                elif component.name == "bulb":
                    # Moves the socket inputs with the mouse
                    component.input.rect.x -= self.offsetX
                    component.input.rect.y -= self.offsetY

                    # Moves any wires connected to the components input sockets with the component when dragged.
                    if component.input.connected:
                        component.input.inputWire.end[0] -= self.offsetX
                        component.input.inputWire.end[1] -= self.offsetY

                else:
                    # Moves the socket outputs with the mouse
                    component.output.rect.x -= self.offsetX
                    component.output.rect.y -= self.offsetY
                    # Moves the socket inputs with the mouse
                    for input in component.inputList:
                        input.rect.x -= self.offsetX
                        input.rect.y -= self.offsetY

                    # Moves any wires connected to the components input sockets with the component when dragged.
                    for inputSocket in component.inputList:
                        if inputSocket.connected:
                            inputSocket.inputWire.end[0] -= self.offsetX
                            inputSocket.inputWire.end[1] -= self.offsetY
                    # Moves any wires connected to the components output socket with the component when dragged.
                    if component.output.connected:
                        for wire in component.output.outputWires:
                            wire.start[0] -= self.offsetX
                            wire.start[1] -= self.offsetY
                    
                    
                # This break is necessary so that you can only pick up one component at a time.
                break
            
        self.rect.x, self.rect.y = self.xPos, self.yPos


# SIDEBAR MENU CLASS
# --------------------------------------------------------------------------------------------
# Represents the sidebar menu on the left of the screen containing all the logic gate components.
# Also responsible for instantiating new instances of components and drawing them.
class SidebarMenu:
    clicked = False
    dragging = False
    def __init__(self):
        self.border = 256

    def instantiate(self):
        andGate = ANDGate(AND_GATE_IMAGE, "ANDGate", 0, 180)
        orGate = ORGate(OR_GATE_IMAGE, "ORGate", 128, 180)
        notGate = NOTGate(NOT_GATE_IMAGE, "NOTGate", 0, 280)
        nandGate = NANDGate(NAND_GATE_IMAGE, "NANDGate", 128, 280)
        norGate = NORGate(NOR_GATE_IMAGE, "NORGate", 0, 380)
        xorGate = XORGate(XOR_GATE_IMAGE, "XORGate", 128, 380)

        switch = Switch(OFF_SWITCH_IMAGE, 15, 480, "switch")
        bulb = Bulb(OFF_BULB_IMAGE, 150, 455, "bulb")

        componentList = [andGate, orGate, notGate, nandGate, norGate, xorGate, switch, bulb]

        # Adds the newly instantiated components to their respective sprite groups
        for component in componentList:
            sidebarSprites.add(component)
    
            if component.name == "switch":
                allSocketSprites.add(component.output)
            elif component.name == "bulb":
                allSocketSprites.add(component.input)
            else:
                allLogicGateSprites.add(component)
                allSocketSprites.add(component.output)
                # Input list is required so that both NOT gate and other gates sockets can be drawn at once.
                # This is because NOT gate only requires one input socket while the others require two.
                for input in component.inputList:
                    allSocketSprites.add(input)

    # This makes sure that the logic gates aren't needlessly instantiated every game loop,
    # new instances are made when the user drags a component from the sidebar menu.
    def instantiateOnClick(self, component, name):
        instantiatedObject = None
        if name == "menu":
            component.clicked = True
        elif name == "ANDGate":
            andGate = ANDGate(AND_GATE_IMAGE, "ANDGate", 0, 180)
            instantiatedObject = andGate
        elif name == "ORGate":
            orGate = ORGate(OR_GATE_IMAGE, "ORGate", 128, 180)
            instantiatedObject = orGate
        elif name == "NOTGate":
            notGate = NOTGate(NOT_GATE_IMAGE, "NOTGate", 0, 280)
            instantiatedObject = notGate
        elif name == "NANDGate":
            nandGate = NANDGate(NAND_GATE_IMAGE, "NANDGate", 128, 280)
            instantiatedObject = nandGate
        elif name == "NORGate":
            norGate = NORGate(NOR_GATE_IMAGE, "NORGate", 0, 380)
            instantiatedObject = norGate
        elif name == "XORGate":
            xorGate = XORGate(XOR_GATE_IMAGE, "XORGate", 128, 380)
            instantiatedObject = xorGate
        elif name == "switch":
            switch = Switch(OFF_SWITCH_IMAGE, 15, 480, "switch")
            instantiatedObject = switch
        elif name == "bulb":
            bulb = Bulb(OFF_BULB_IMAGE, 150, 455, "bulb")
            instantiatedObject = bulb

        # Adds the newly instantiated component to its respective sprite groups
        if instantiatedObject != None:
            sidebarSprites.add(instantiatedObject)
    
            if instantiatedObject.name == "switch":
                allSocketSprites.add(instantiatedObject.output)
            elif instantiatedObject.name == "bulb":
                allSocketSprites.add(instantiatedObject.input)
            else:
                allLogicGatesList.append(instantiatedObject)
                print(allLogicGatesList)

                allSocketSprites.add(instantiatedObject.output)
                # Input list is required so that both NOT gate and other gates sockets can be drawn at once.
                # This is because NOT gate only requires one input socket while the others require two.
                for input in instantiatedObject.inputList:
                    allSocketSprites.add(input)


    def drawSprites(self):
        # Draws all of the logic gates
        sidebarSprites.draw(SCREEN)
        # Draws all of the sockets
        allSocketSprites.draw(SCREEN)
        # Draws all of the wires
        for wire in allWireSprites:
            wire.draw(SCREEN)

        for component in sidebarSprites:
            if component.name == "switch":
                component.update(ON_SWITCH_IMAGE, OFF_SWITCH_IMAGE)
            elif component.name == "bulb":
                component.update(ON_BULB_IMAGE, OFF_BULB_IMAGE)


# TRANSMIT CURRENT FUNCTION
# --------------------------------------------------------------------------------------------
# Transmits current through the wires, sockets and components.
def transmitCurrent():
    for wire in allWireSprites:
        if wire.startSocket.current:
            wire.endSocket.current = True
            wire.color = (255, 0, 0)
        else:
            wire.endSocket.current = False
            wire.color = (0,0,0)

    for component in allLogicGatesList:
        component.performLogic()


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

    informationMenu = InformationMenu(INFORMATION_MENU_IMAGE, 80, 550)
    sidebarSprites.add(informationMenu)
    
    # Main game loop
    while run:
        mouse.endSocketList = []
        informationMenu.clicked = False
        for event in pygame.event.get():

            # Checks if pygame was quit
            if event.type == pygame.QUIT:
                run = False

            # Checks if the mouse button is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                sidebar.clicked = True
                sidebar.dragging = True
                mouse.endSocketList = []
                # Adds all collided sprites to the carryList
                mouse.carryList = pygame.sprite.spritecollide(mouse, sidebarSprites, False)
                # Check if any socket sprites collide with mouse position, if true then add to sourceSocketList
                mouse.sourceSocketList = pygame.sprite.spritecollide(mouse, allSocketSprites, False)

                if mouse.carryList != []:
                    # Switch is turned on when clicked
                    if mouse.carryList[0].name == "switch":
                        mouse.carryList[0].switchedOn = not mouse.carryList[0].switchedOn
                    # Changes colour of information menu when clicked and opens the menu
                    elif mouse.carryList[0].name == "menu":
                        informationMenu.image = INFORMATION_MENU_HOVER_IMAGE
                        informationMenu.show()
                
            # Checks if the mouse button was released
            elif event.type == pygame.MOUSEBUTTONUP:
                # Lets the user connect a wire coming out of one socket to another socket
                # Checks if the user is currently dragging a wire
                if mouse.sourceSocketList != []:
                    mouse.endSocketList = pygame.sprite.spritecollide(mouse, allSocketSprites, False)

                sidebar.dragging = False

                # When you let go off clicking the mouse the carryList is emptied
                mouse.carryList = []
                mouse.sourceSocketList = []
                informationMenu.image = INFORMATION_MENU_IMAGE

        # Fills the screen with the colour white
        SCREEN.fill((255, 255, 255))
        # Draws the background onto the screen
        SCREEN.blit(BACKGROUND, (256,0))

        if mouse.carryList != [] :
            # Regenerate all components in the sidebar menu.
            # This is so that if they are drag and dropped, a new instance appears
            # in its original place.
            if sidebar.clicked == True:
                sidebar.instantiateOnClick(mouse.carryList[0], mouse.carryList[0].name)
                # This makes sure that only ONE instance is made of each logic gate, this minimises
                # the performance impact.
                sidebar.clicked = False

        # Transmits current through the wires
        transmitCurrent()

        SCREEN.blit(LOGO_IMAGE,(0, 0))

        # Draws the logic gates, sockets and wires.
        sidebar.drawSprites()

        # Updates the mouse objects position, as well as any dragged logic gate components and their 
        # respective sockets and connected wires.
        mouse.update()

        # Update the display
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()

if __name__ == "__main__":
    main()


"""
MOVING CONNECTED WIRES WITH ITS CONNECTED COMPONONENT IF COMPONENT IS DRAGGED

To implement this, we must first make sure that each logic gate object is linked to its own socket objects, and each 
socket object is linked to its own wire objects (if connected). 
We must be able to differentiate between wires that carry outputs and wires that carry inputs.
If the socket is an input socket, then the connected wire is an output wire (as it is carrying the output of the previous component) 
and vice versa.
This will also allow the future implementation of logic as it will let the binary values(1 or 0) be transmitted through the wires
into or out of the logic gates, inside of which logic will be performed.

1. Make sure that when a connected wire is made, its respective input and output sockets have an attribute which links it to the 
corresponding wire.
2. When a logic gate component is dragged, the input and output sockets are checked for connected wires.
3. Any connected wires have their self.start or self.end values changed by the same x and y offset values as the components
self.rect.x,y values are changed. 
4. The wires are drawn anew.

"""
"""
MANAGING CONDITIONS FOR WIRE CONNECTIVITY AND INVALID CONNECTIONS
This will make sure that wires do not come out of a socket and connect to the same socket, 
a socket of the same component, or a socket that already has a wire connected to it.
Here are the four cases where a wire connection is not permitted :

1. If (endsocket.gate = startsocket.gate) : dont connect.
2. If (endsocket.connected): dont connect
3. If (endsocket.isInput AND startsocket.isInput) : dont connect.
4. If ((NOT endsocket.isInput) AND (NOT startsocket.isInput)) : dont connect

"""

"""
if self.sourceSocket.current == True:
                        endSocket.current = True
                    else:
                        endSocket.current = False
"""
