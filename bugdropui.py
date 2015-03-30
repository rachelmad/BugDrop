import pygame, sys
from bugdrop import *

MAIN_WIDTH = 800
MAIN_HEIGHT = 600
BUG_SIZE = 34

WHITE = ( 255, 255, 255)

def main():
    pygame.init()
    ui = BugDropUI(MAIN_WIDTH, MAIN_HEIGHT)
    pygame.display.set_caption('Bug Drop Clone')
    
    while True:
        ui.main_frame.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        pygame.time.Clock().tick(100)


class BugDropUI(object):
    def __init__(self, width, height):
        self.main_frame = pygame.display.set_mode((width, height))
        self.all_sprites = pygame.sprite.Group()
        self.all_bugs = pygame.sprite.Group()
        
        #add game frame
        #all_sprites_list.add(block)
        
class Bug(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__(self)
        self.image = pygame.Surface((BUG_SIZE, BUG_SIZE))
        pygame.draw.circle(self.image, color, (0, 0), BUG_SIZE / 2)
        self.rect = self.image.get_rect()
        
if __name__ == '__main__':
    main()
    