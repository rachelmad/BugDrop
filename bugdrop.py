import random

NUM_GAME_COLUMNS = 6
COLUMN_HEIGHT = 12


class BugDrop(object):
    def __init__(self):
        self.game_grid = [[0 for x in range(COLUMN_HEIGHT + 2)] for x in range(NUM_GAME_COLUMNS)]      #+2 for drawing purposes
        self.status = 'Playing'
    
    
    def get_column_base(self, column):
        base = 0
        for item in range(len(self.game_grid[column])):
            if self.game_grid[column][item] != 0:
                base = item + 1
        return base
            
            
    def is_at_max(self, column):
        if self.get_column_base(column) == COLUMN_HEIGHT:
            return True
        return False
                
        
    def add_to_column(self, color, column):
        if column < NUM_GAME_COLUMNS and column >= 0:
            if self.is_at_max(column):
                self.status = 'Lost'
            self.game_grid[column][self.get_column_base(column)] = color
                    
                    
    def drop_bug_set_in_column(self, bug_set, column):
        if bug_set.position == 'up_position':
            self.add_to_column(bug_set.bug_color1, column)
            self.add_to_column(bug_set.bug_color2, column)
        if bug_set.position == 'down_position':
            self.add_to_column(bug_set.bug_color2, column)
            self.add_to_column(bug_set.bug_color1, column)
        if bug_set.position == 'left_position':
            self.add_to_column(bug_set.bug_color1, column)
            self.add_to_column(bug_set.bug_color2, column - 1)
        if bug_set.position == 'right_position':
            self.add_to_column(bug_set.bug_color1, column)
            self.add_to_column(bug_set.bug_color2, column + 1)
        
            
    def recursive_check_colors(self, column, row, similar_bugs, passed):
        passed[column][row] = 1
        if self.game_grid[column][row] == self.game_grid[column + 1][row] and passed[column + 1][row] == 0 and column < NUM_GAME_COLUMNS - 2:
            similar_bugs.append([column + 1, row])
            self.recursive_check_colors(column + 1, row, similar_bugs, passed)
        if self.game_grid[column][row] == self.game_grid[column][row - 1] and passed[column][row - 1] == 0 and row > 0:
            similar_bugs.append([column, row - 1])
            self.recursive_check_colors(column, row - 1, similar_bugs, passed)
        if self.game_grid[column][row] == self.game_grid[column - 1][row] and passed[column - 1][row] == 0 and column > 0:
            similar_bugs.append([column - 1, row])
            self.recursive_check_colors(column - 1, row, similar_bugs, passed)
        if self.game_grid[column][row] == self.game_grid[column][row + 1] and passed[column][row + 1] == 0 and row < COLUMN_HEIGHT - 2:
            similar_bugs.append([column, row + 1])
            self.recursive_check_colors(column, row + 1, similar_bugs, passed)           
        return similar_bugs
        
    
    def get_similar_bugs(self, column, row):
        passed_cells = [[0 for x in range(COLUMN_HEIGHT)] for x in range(NUM_GAME_COLUMNS)]
        return self.recursive_check_colors(column, row, [[column, row]], passed_cells)
        


class BugSet(object):
    def __init__(self):
        self.bug_color1 = random.randint(1, 5)
        self.bug_color2 = random.randint(1, 5)
        self.position = 'up_position'

    

    
    
    

    
        