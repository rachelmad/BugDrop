import unittest
from bugdrop import *

class BugDropTest(unittest.TestCase):
    def setUp(self): 
        self.bugDrop = BugDrop()
        
        
    def testcanary(self):
        self.assertTrue(True)
        
        
    def testAddToColumnChangesGameGrid(self):
        self.bugDrop.addToColumn(1, 0)
        self.assertEquals(1, self.bugDrop.gameGrid[0][0])
        
    
    def testAddToColumnForInvalidColumnRaisesException(self):
        self.assertRaises(IndexError, self.bugDrop.addToColumn(1, -1))
        
        
    def testIsAtMaxOnMaxedBaseReturnsTrue(self):
        self.bugDrop.base[0] = 11       #GAMEHEIGHT - 1
        self.assertTrue(self.bugDrop.isAtMax(0))
        
    
    def testIsAtMaxOnLowBaseReturnsFalse(self):
        self.bugDrop.base[0] = 0
        self.assertFalse(self.bugDrop.isAtMax(0))
        
    
    def testAddToColumnIncreasesBase(self):
        self.bugDrop.addToColumn(1, 0)
        self.bugDrop.updateBase()
        self.assertEquals(1, self.bugDrop.base[0])
        
if __name__ == '__main__':
    unittest.main()