import unittest
from bugdrop import *

class BugDropTest(unittest.TestCase):
    def setUp(self): 
        self.bug_drop = BugDrop()
        self.bug_set = BugSet()        
        
    def test_canary(self):
        self.assertTrue(True)        
        
    def test_content_changes_column_base(self):
        self.bug_drop.game_grid[1][0] = 1
        self.assertEquals(1, self.bug_drop.get_column_base(1))    
        
    def test_is_at_max_on_maxed_base_returns_true(self):
        self.bug_drop.game_grid[1][11] = 1       #GAMEHEIGHT - 1
        self.assertTrue(self.bug_drop.is_at_max(1))        
    
    def test_is_at_max_on_low_base_returns_false(self):
        self.bug_drop.game_grid[1][3] = 1
        self.assertFalse(self.bug_drop.is_at_max(1))    
        
    def test_add_to_column_changes_game_grid(self):
        self.bug_drop.add_to_column(1, 0)
        self.assertEquals(1, self.bug_drop.game_grid[0][0])        
    
    def test_add_to_column_for_invalid_column_does_nothing(self):
        self.bug_drop.add_to_column(1, -1)
        total = 0
        for x in range(6):
            total += self.bug_drop.game_grid[x][0]
        self.assertEquals(0, total)  
        
    def test_add_to_column_for_maxed_column_loses_game(self):
        self.bug_drop.game_grid[1][11] = 1
        self.bug_drop.add_to_column(1, 1)
        self.assertEquals('Lost', self.bug_drop.status)       
    
    def test_add_to_column_increases_base(self):
        self.bug_drop.add_to_column(1, 1)
        self.assertEquals(1, self.bug_drop.get_column_base(1))        
        
    def test_drop_up_bug_set_in_column_changes_game_grid(self):
        self.bug_drop.drop_bug_set_in_column(self.bug_set, 1)
        self.assertEquals(self.bug_drop.game_grid[1][1], self.bug_set.bug_color2)
        
    def test_drop_down_bug_set_in_column_changes_game_grid(self):
        self.bug_set.position = 'down_position'
        self.bug_drop.drop_bug_set_in_column(self.bug_set, 1)
        self.assertEquals(self.bug_drop.game_grid[1][1], self.bug_set.bug_color1)
        
    def test_drop_vertical_bug_set_in_full_column_loses(self):
        self.bug_drop.game_grid[1][10] = 1
        self.bug_drop.drop_bug_set_in_column(self.bug_set, 1)
        self.assertTrue('Lost', self.bug_drop.status)
        
    def test_drop_left_bug_set_in_column_changes_game_grid(self):
        self.bug_set.position = 'left_position'
        self.bug_drop.drop_bug_set_in_column(self.bug_set, 5)
        self.assertEquals(self.bug_drop.game_grid[4][0], self.bug_set.bug_color2)
        
    def test_drop_right_bug_set_in_column_changes_game_grid(self):
        self.bug_set.position = 'right_position'
        self.bug_drop.drop_bug_set_in_column(self.bug_set, 3)
        self.assertEquals(self.bug_drop.game_grid[4][0], self.bug_set.bug_color2)
        
    def test_drop_invalid_position_bug_set_in_column_does_nothing(self):
        self.bug_set.position = 'blah'
        self.bug_drop.drop_bug_set_in_column(self.bug_set, 0)
        self.assertEquals(0, self.bug_drop.game_grid[0][0])
        
    def test_count_adjacent_color_returns_correct_number_of_adjacent_colors(self):
        self.bug_drop.game_grid[2][0] = 1
        self.bug_drop.game_grid[3][0] = 1
        self.bug_drop.game_grid[4][0] = 1
        self.assertEquals(2, self.bug_drop.count_adjacent_colors(3, 0))
        
        
class bug_setTest(unittest.TestCase):
    def setUp(self):
        self.bug_set = BugSet()
        
    def test_canary(self):
        self.assertTrue(True)
        
    def test_initial_bug_set_creates_random_sets(self):
        random = BugSet()
        self.assertTrue(self.bug_set != random)

        
if __name__ == '__main__':
    unittest.main()