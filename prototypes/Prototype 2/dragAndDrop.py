# DRAG AND DROP FUNCTION
# --------------------------------------------------------------------------------------------
import pygame

def dragAndDrop(component):
    #mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # Checks if the mouse is clicked above a component
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Checks if its the right mouse button that is clicked
            if event.button == 1:
                if component.rect.collidepoint(event.pos):
                    component.dragging = True
                    mouseX, mouseY = event.pos
                    offsetX = component.rect.x - mouseX
                    offsetY = component.rect.y - mouseY

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Checks if it is the right mouse button that is released
            if event.button == 1:
                component.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if component.dragging == True:
                mouseX, mouseY = event.pos
                component.rect.x = mouseX + offsetX
                component.rect.y = mouseY + offsetY
                print("test")
