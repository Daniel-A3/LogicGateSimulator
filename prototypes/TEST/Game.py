import pygame

class Game:
    def __init__(self, width, height, background):
        self.width = width
        self.height = height
        self.background = background
        # Sets the width and height of the program.
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.run = True

    # Checks if the game was quit
    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    # Draws the pygame window
    def drawWindow(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (256,0))

        pygame.display.flip()

    # Draws all the gates in the sidebar menu
    def drawGates(self, ANDGate, ORGate, NOTGate, NANDGate, NORGate, XORGate):
        self.screen.blit(ANDGate, (0,0))
        self.screen.blit(ORGate, (128,0))
        self.screen.blit(NOTGate, (0,100))
        self.screen.blit(NANDGate, (128,100))
        self.screen.blit(NORGate, (0,200))
        self.screen.blit(XORGate, (128,200))

        pygame.display.flip()
