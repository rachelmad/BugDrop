import unittest
from bugdropui import *

class BugDropTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)
        
    def setUp(self):
        self.bug_drop = BugDrop()
        self.ui = BugDropUI(self.bug_drop.num_columns, self.bug_drop.column_height)
        
    def test_bug_size_is_even(self):
        self.assertEquals(0, BUG_SIZE % 2)
        
    def test_main_width_is_large_enough(self):
        self.assertTrue(self.ui.MAIN_WIDTH > self.bug_drop.num_columns)
        
    def test_main_height_is_large_enough(self):
        self.assertTrue(self.ui.MAIN_HEIGHT > self.bug_drop.column_height)
    
if __name__ == '__main__':
    unittest.main()