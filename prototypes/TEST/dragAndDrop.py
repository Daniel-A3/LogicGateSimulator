# DRAG AND DROP FUNCTION
# --------------------------------------------------------------------------------------------
import pygame
#from LogicGates import ANDGate, ORGate, NOTGate, NANDGate, NORGate, XORGate

def dragAndDrop(draggedGroup, logicGateSprites, mouse):
    allEvents = pygame.event.get()
    for event in allEvents:
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(1)
            draggedGroupList = pygame.sprite.spritecollide(mouse, logicGateSprites, True)

    for component in logicGateSprites:
        pass
    return draggedGroup