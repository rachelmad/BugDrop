import pygame, sys
from bugdrop import *

MAIN_WIDTH = 800
MAIN_HEIGHT = 600

WHITE = ( 255, 255, 255)

def main():
    pygame.init()
    ui = BugDropUI(MAIN_WIDTH, MAIN_HEIGHT)
    pygame.display.set_caption('Bug Drop Clone')
    
    while True:
        ui.main_frame.fill(WHITE)
        pygame.display.update()
        pygame.time.Clock().tick(100)

class BugDropUI(object):
    def __init__(self, width, height):
        self.main_frame = pygame.display.set_mode((width, height))
        
if __name__ == '__main__':
    main()
    
    
                    # LEARN ABOUT SPRITES!!!