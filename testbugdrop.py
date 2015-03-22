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
    
    def testAddToColumnForInvalidColumnDoesNothing(self):
        self.bugDrop.addToColumn(1, -1)
        total = 0
        for x in range(6):
            total += self.bugDrop.gameGrid[x][0]
        self.assertEquals(0, total)  
        
    def testAddToColumnForMaxedColumnLosesGame(self):
        self.bugDrop.gameGrid[1][11] = 1
        self.bugDrop.addToColumn(1, 1)
        self.assertEquals('Lost', self.bugDrop.status)       
    
    def testAddToColumnIncreasesBase(self):
        self.bugDrop.addToColumn(1, 1)
        self.assertEquals(1, self.bugDrop.getColumnBase(1))        
        
    def testDropUpBugSetInColumnChangesGameGrid(self):
        self.bugDrop.dropBugSetInColumn(self.bugSet, 1)
        self.assertEquals(self.bugDrop.gameGrid[1][1], self.bugSet.bugColor2)
        
    def testDropDownBugSetInColumnChangesGameGrid(self):
        self.bugSet.position = 'downPosition'
        self.bugDrop.dropBugSetInColumn(self.bugSet, 1)
        self.assertEquals(self.bugDrop.gameGrid[1][1], self.bugSet.bugColor1)
        
    def testDropVerticalBugSetInFullColumnLoses(self):
        self.bugDrop.gameGrid[1][10] = 1
        self.bugDrop.dropBugSetInColumn(self.bugSet, 1)
        self.assertTrue('Lost', self.bugDrop.status)
        
    def testDropLeftBugSetInColumnChangesGameGrid(self):
        self.bugSet.position = 'leftPosition'
        self.bugDrop.dropBugSetInColumn(self.bugSet, 5)
        self.assertEquals(self.bugDrop.gameGrid[4][0], self.bugSet.bugColor2)
        
    def testDropRightBugSetInColumnChangesGameGrid(self):
        self.bugSet.position = 'rightPosition'
        self.bugDrop.dropBugSetInColumn(self.bugSet, 3)
        self.assertEquals(self.bugDrop.gameGrid[4][0], self.bugSet.bugColor2)
        
    def testDropInvalidPositionBugSetInColumnDoesNothing(self):
        self.bugSet.position = 'blah'
        self.bugDrop.dropBugSetInColumn(self.bugSet, 0)
        self.assertEquals(0, self.bugDrop.gameGrid[0][0])
        
        
class BugSetTest(unittest.TestCase):
    def setUp(self):
        self.bugSet = BugSet()
        
    def testCanary(self):
        self.assertTrue(True)
        
    def testInitialBugSetCreatesRandomSets(self):
        random = BugSet()
        self.assertTrue(self.bugSet != random)

        
if __name__ == '__main__':
    unittest.main()