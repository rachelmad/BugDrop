import pygame, sys
from bugdrop import *

MAIN_WIDTH = 800
MAIN_HEIGHT = 600
BUG_SIZE = 34

WHITE = ( 255, 255, 255)
BLACK = ( 0, 0, 0)

def main():
    pygame.init()
    ui = BugDropUI(MAIN_WIDTH, MAIN_HEIGHT)
    pygame.display.set_caption('Bug Drop Clone')
    
    while True:
        ui.main_frame.fill(WHITE)
        ui.make_walls()
        ui.game_frame.draw(ui.main_frame)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        pygame.time.Clock().tick(100)


class BugDropUI(object):
    def __init__(self, width, height):
        self.bugdrop = BugDrop()
        
        self.main_frame = pygame.display.set_mode((width, height))
        self.game_frame = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_bugs = pygame.sprite.Group()
        
        
    def make_walls(self):
        game_frame_width = BUG_SIZE * self.bugdrop.num_columns
        game_frame_height = BUG_SIZE * self.bugdrop.column_height
        top_left_position_x = (3 * MAIN_WIDTH / 4) - game_frame_width / 2
        top_left_position_y = BUG_SIZE * 3
        
        left_wall = Wall(5, game_frame_height)
        left_wall.rect.x = top_left_position_x - 5
        left_wall.rect.y = top_left_position_y
        bottom_wall = Wall(game_frame_width + 10, 5)
        bottom_wall.rect.x = top_left_position_x - 5
        bottom_wall.rect.y = top_left_position_y + game_frame_height
        right_wall = Wall(5, game_frame_height)
        right_wall.rect.x = top_left_position_x + game_frame_width
        right_wall.rect.y = top_left_position_y
        
        self.game_frame.add(left_wall)
        self.game_frame.add(bottom_wall)
        self.game_frame.add(right_wall)
     
        
class Bug(pygame.sprite.Sprite):
    def __init__(self, color):
        super(Bug, self).__init__()
        self.image = pygame.Surface((BUG_SIZE, BUG_SIZE))
        pygame.draw.circle(self.image, color, (0, 0), BUG_SIZE / 2)
        self.rect = self.image.get_rect()
        
        
class Wall(pygame.sprite.Sprite):
    def __init__(self, width, height):       
        super(Wall, self).__init__()
        self.image = pygame.Surface((width, height))
        pygame.draw.rect(self.image, BLACK, (0, 0, width, height), 0)
        self.rect = self.image.get_rect()

        
        
if __name__ == '__main__':
    main()
    