import pygame

class Game:
    def __init__(self, width, height, background):
        self.width = width
        self.height = height
        self.background = background
        self.screen = pygame.display.set_mode(self.width, self.height)
        self.run = True

    # Checks if the game was quit
    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    # Draws the pygame window
    def drawWindow(self):
        self.screen.fill(255, 255, 255)
        self.screen.blit(self.background, (250,0))

        #self.screen.blit(AND_GATE, (0,0))
        
        pygame.display.flip()

    pygame.display.update()