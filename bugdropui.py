import pygame, sys
from bugdrop import *

MAIN_WIDTH = 800
MAIN_HEIGHT = 600
BUG_SIZE = 34

WHITE = ( 255, 255, 255)
BLACK = ( 0, 0, 0)
RED = ( 255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
PURPLE = ( 255, 0, 255)
YELLOW = ( 255, 255, 0)

def main():
    pygame.init()
    ui = BugDropUI(MAIN_WIDTH, MAIN_HEIGHT)
    pygame.display.set_caption('Bug Drop Clone')
    
    while True:
        ui.play_game()
    

class BugDropUI(object):
    def __init__(self, width, height):
        self.bugdrop = BugDrop()
        
        self.main_frame = pygame.display.set_mode((width, height))
        self.game_frame = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_bugs = pygame.sprite.Group()
        
        self.game_frame_width = BUG_SIZE * self.bugdrop.num_columns
        self.game_frame_height = BUG_SIZE * self.bugdrop.column_height
        self.top_left_position_x = (3 * MAIN_WIDTH / 4) - self.game_frame_width / 2
        self.top_left_position_y = BUG_SIZE * 3
       
       
    def play_game(self):
        next_drop = self.create_new_bugset()
    
        while True:
            self.main_frame.fill(WHITE)
            self.make_walls()
            self.game_frame.draw(ui.main_frame)
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            next_drop.draw(ui.main_frame)
            pygame.display.update()
            pygame.time.Clock().tick(100)
             
        
    def make_walls(self):        
        left_wall = Wall(5, self.game_frame_height)
        left_wall.rect.x = self.top_left_position_x - 5
        left_wall.rect.y = self.top_left_position_y
        bottom_wall = Wall(self.game_frame_width + 10, 5)
        bottom_wall.rect.x = self.top_left_position_x - 5
        bottom_wall.rect.y = self.top_left_position_y + self.game_frame_height
        right_wall = Wall(5, self.game_frame_height)
        right_wall.rect.x = self.top_left_position_x + self.game_frame_width
        right_wall.rect.y = self.top_left_position_y
        
        self.game_frame.add(left_wall)
        self.game_frame.add(bottom_wall)
        self.game_frame.add(right_wall)
        

    def create_new_bugset(self):
        bugset = BugSet()
        if bugset.bug_color1 == 1:
            bug1 = Bug(RED)
        elif bugset.bug_color1 == 2:
            bug1 = Bug(GREEN)
        elif bugset.bug_color1 == 3:
            bug1 = Bug(BLUE)
        elif bugset.bug_color1 == 4:
            bug1 = Bug(PURPLE)
        elif bugset.bug_color1 == 5:
            bug1 = Bug(YELLOW)
            
        if bugset.bug_color2 == 1:
            bug2 = Bug(RED)
        elif bugset.bug_color2 == 2:
            bug2 = Bug(GREEN)
        elif bugset.bug_color2 == 3:
            bug2 = Bug(BLUE)
        elif bugset.bug_color2 == 4:
            bug2 = Bug(PURPLE)
        elif bugset.bug_color2 == 5:
            bug2 = Bug(YELLOW)
                
        bug1.rect.x = self.top_left_position_x + BUG_SIZE * 2
        bug1.rect.y = self.top_left_position_y - BUG_SIZE
        bug2.rect.x = self.top_left_position_x + BUG_SIZE * 2
        bug2.rect.y = self.top_left_position_y - BUG_SIZE * 2
        
        bugset_sprites = pygame.sprite.Group()
        bugset_sprites.add(bug1)
        bugset_sprites.add(bug2)
        return bugset_sprites
     
        
class Bug(pygame.sprite.Sprite):
    def __init__(self, color):
        super(Bug, self).__init__()
        self.image = pygame.Surface((BUG_SIZE, BUG_SIZE))
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, color, (BUG_SIZE / 2, BUG_SIZE / 2), BUG_SIZE / 2)
        self.rect = self.image.get_rect()
        
        
class Wall(pygame.sprite.Sprite):
    def __init__(self, width, height):       
        super(Wall, self).__init__()
        self.image = pygame.Surface((width, height))
        pygame.draw.rect(self.image, BLACK, (0, 0, width, height), 0)
        self.rect = self.image.get_rect()

        
        
if __name__ == '__main__':
    main()
    