import random
import os
import game_config as gc
from pygame import display, event
from pygame import image, transform
from time import sleep
animals_count = dict((a, 0) for a in gc.ASSET_FILES)  ##dictionary
##print(animals_count)
screen = display.set_mode((512,512))
def available_animals():
    return [animal for animal, count in animals_count.items() if count < 2]

class Animal:
    def __init__(self, index):
        self.index = index  #index of the animal
        self.name = random.choice(available_animals())  #random name
        ##print(self.name)
        self.image_path = os.path.join(gc.ASSET_DIR, self.name)  #join root for self.name feom ASSET_DIR
        self.row = index // gc.NUM_TILES_SIDE   #row
        self.col = index % gc.NUM_TILES_SIDE    #column
        self.skip = False
        self.image = image.load(self.image_path)    #load image in app

        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN)) #
        #reduce pixel by gc.IMAGE_SIZE - 2*gc.MARGIN from all side
        ##print(self.image)

        self.box = self.image.copy()    #copy of image
        self.box.fill((200, 200, 200))

        animals_count[self.name] += 1
##Animal(0)