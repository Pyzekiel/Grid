import pygame
import random

# Class Is TO make like the: <ClassName>.<blocks>
# You Can Even make a class inside of class so: <Classname>.<classname>.<block>()
class CreateAsset(pygame.sprite.Sprite):

    def __init__(self, x,y, size):
      # super make it link so you won't type __init__() instead: CreateAsset(<__init__ params>)
        super(CreateAsset, self).__init__()
        # Create a List Of Colors
        cl = [
            "red",
            "green",
            "blue"
        ]
        self.image = pygame.Surface((30, 30))
        #                                    Choose From The List:
        pygame.draw.rect(self.image, pygame.Color(random.choice(cl)), (0, 0, size,size))
        # Use Rect Only If You Make in a group (for me blitting is not working)
        # self is the self like: <ClassName>.rect = 10
        # It's like editing a variable in side a class without calling it
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
