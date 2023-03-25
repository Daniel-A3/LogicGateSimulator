# THE GAME CLASS
# --------------------------------------------------------------------------------------------
import pygame

class Game:
    def __init__(self, width, height, background, screen):
        self.width = width
        self.height = height
        self.background = background
        self.screen = screen
        self.run = True

    # Checks if the game was quit
    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                pygame.quit()

    # Draws the pygame window
    def drawWindow(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (256,0))

    # Draws all the gates in the sidebar menu
    def drawGates(self, ANDGate, ORGate, NOTGate, NANDGate, NORGate, XORGate):
        # Resizes the images and uses a smooth scaling algorithm for better quality
        self.screen.blit(pygame.transform.smoothscale(ANDGate, (128, 64)), (0,100))
        self.screen.blit(pygame.transform.smoothscale(ORGate, (128, 64)), (128,100))
        self.screen.blit(pygame.transform.smoothscale(NOTGate, (128, 64)), (0,225))
        self.screen.blit(pygame.transform.smoothscale(NANDGate, (128, 64)), (128,225))
        self.screen.blit(pygame.transform.smoothscale(NORGate, (128, 64)), (0,350))
        self.screen.blit(pygame.transform.smoothscale(XORGate, (128, 64)), (128,350))

        pygame.display.flip()
