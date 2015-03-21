import unittest
from bugdrop import *

class BugDropTest(unittest.TestCase):
    def setUp(self): 
        self.bugDrop = BugDrop()
        self.bugSet = BugSet()        
        
    def testcanary(self):
        self.assertTrue(True)        
        
    def testContentChangesColumnBase(self):
        self.bugDrop.gameGrid[1][0] = 1
        self.assertEquals(1, self.bugDrop.getColumnBase(1))    
        
    def testIsAtMaxOnMaxedBaseReturnsTrue(self):
        self.bugDrop.gameGrid[1][11] = 1       #GAMEHEIGHT - 1
        self.assertTrue(self.bugDrop.isAtMax(1))        
    
    def testIsAtMaxOnLowBaseReturnsFalse(self):
        self.bugDrop.gameGrid[1][3] = 1
        self.assertFalse(self.bugDrop.isAtMax(1))    
        
    def testAddToColumnChangesGameGrid(self):
        self.bugDrop.addToColumn(1, 0)
        self.assertEquals(1, self.bugDrop.gameGrid[0][0])        
    
    def testAddToColumnForInvalidColumnRaisesException(self):
        self.assertRaises(IndexError, self.bugDrop.addToColumn, 1, -1) 
        
    def testAddToColumnForMaxedColumnRaisesException(self):
        self.bugDrop.gameGrid[1][11] = 1
        self.assertRaises(IndexError, self.bugDrop.addToColumn, 1, -1)       
    
    def testAddToColumnIncreasesBase(self):
        self.bugDrop.addToColumn(1, 1)
        self.assertEquals(1, self.bugDrop.getColumnBase(1))        
        
    def testDropUpBugSetInColumnChangesGameGrid(self):
        self.bugDrop.dropBugSetInColumn(self.bugSet, 1)
        self.assertTrue(self.bugDrop.gameGrid[1][2] != 0)
        
        
class BugSetTest(unittest.TestCase):
    def setUp(self):
        self.bugSet = BugSet()
        
    def testCanary(self):
        self.assertTrue(True)
        
    def testInitialBugSetCreatesRandomSets(self):
        random = BugSet()
        self.assertTrue(self.bugSet != random)
        
    def testSetPositionChangesPositionForValidValue(self):
        self.bugSet.setPosition('down')
        self.assertEquals('down', self.bugSet.position)
        
    def testSetPositionThrowsErrorsForInvalidPositionValue(self):
        self.assertRaises(ValueError, self.bugSet.setPosition, 'random')

        
if __name__ == '__main__':
    unittest.main()