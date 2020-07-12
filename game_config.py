import os

IMAGE_SIZE = 128        #Interanal image
SCREEN_SIZE = 512       #screensize 512*512
NUM_TILES_SIDE = 4      #number of tiles in a row or columb
NUM_TILES_TOTAL = 16    #total tiles
MARGIN = 8             #


ASSET_DIR = 'assets'
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']  # list of all animal in wce file
##print(ASSET_FILES)
assert len(ASSET_FILES) == 8  ##for checking (True / False)
