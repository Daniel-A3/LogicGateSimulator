# TEST
import pygame

testGroup = pygame.sprite.Group()

class foo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "test"

instance1 = foo()
instance2 = foo()
instance2.name = "test2"

testGroup.add(instance1)
testGroup.add(instance2)
print(testGroup.sprites())