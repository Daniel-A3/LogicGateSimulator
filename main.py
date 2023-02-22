import pygame, os

pygame.init()

WIDTH, HEIGHT = 960, 540
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OneOrZero")
WHITE = (255, 255, 255)

FPS = 60

AND_GATE_IMAGE = pygame.image.load(os.path.join("Assets", "ANDGate.png"))

def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(WHITE)
        pygame.display.update()

    pygame.quit()

    
# Creates buttons for all logic gates
#ANDGate = Button(pygame.image.load("andgate.png"))
#ANDGate.rect.x = 50
#ANDGate.rect.y = 20

if __name__ == "__main__":
    main()