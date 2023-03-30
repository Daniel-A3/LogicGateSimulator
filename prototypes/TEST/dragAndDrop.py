# DRAG AND DROP FUNCTION
# --------------------------------------------------------------------------------------------
import pygame
#from LogicGates import ANDGate, ORGate, NOTGate, NANDGate, NORGate, XORGate

def dragAndDrop(draggedGroup, logicGateSprites, mouse, run):
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(1)
            draggedGroupList = pygame.sprite.spritecollide(mouse, logicGateSprites, True)
            draggedGroup.add(draggedGroupList)

            print(draggedGroup)
    for component in logicGateSprites:
        pass
    return draggedGroup, run