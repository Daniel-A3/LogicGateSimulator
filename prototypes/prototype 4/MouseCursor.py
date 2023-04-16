# MOUSE CURSOR CLASS
# --------------------------------------------------------------------------------------------
import pygame

pygame.init()

class Wire(pygame.sprite.Sprite):
    def __init__(self, start, end):
        pygame.sprite.Sprite.__init__(self)
        self.start = start
        self.end = end
        self.color = (0, 0, 0)
        self.width = 4

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.start, self.end, self.width)

class MouseCursor(pygame.sprite.Sprite):
    carryList = []
    socketList = []
    connectedSocket = []

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        # Creates a rect object for the mouse cursor
        self.rect = pygame.Rect(0, 0, 20, 20)

    # Updates the position of the mouse and any object it is dragging
    def update(self):
        sourceSocket = None
        
        # x and y position of the mouse cursor
        self.xPos, self.yPos = pygame.mouse.get_pos()

        # Finds the offset of how much the mouse was moved
        offsetX = self.rect.x - self.xPos
        offsetY = self.rect.y - self.yPos

        # If the socketList is empty, the user isnt trying to make a new wire, so it lets them 
        # drag the actual component.
        if self.socketList == []:

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
        # In this case it stops the component from moving, this lets the user drag out a wire from the socket.
        else:
            # Drag and dropping, and connecting new wires
            for socket in self.socketList:
                sourceSocket = socket
                # Creates a wire and sets the end of the wire to the mouse position
                sourceSocket.connectedWire = Wire([sourceSocket.rect.x + 8, sourceSocket.rect.y + 8], [self.xPos, self.yPos])
                # This break is necessary so that you can only pick up one component at a time.
                break
        
        if self.connectedSocket != []:
            for endSocket in self.connectedSocket:
                sourceSocket = endSocket
                sourceSocket.connectedWire = Wire([sourceSocket.rect.x + 8, sourceSocket.rect.y + 8], [self.xPos, self.yPos])
            
            # Draws the wire
            sourceSocket.connectedWire.draw(self.screen)
            #endSocket.connectedWire.draw(self.screen)

        self.rect.x, self.rect.y = self.xPos, self.yPos
