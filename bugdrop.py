import random

NUMGAMECOLUMNS = 6
COLUMNHEIGHT = 12


class BugDrop(object):
    def __init__(self):
        self.gameGrid = [[0 for x in range(COLUMNHEIGHT + 2)] for x in range(NUMGAMECOLUMNS)]      #+3 for drawing purposes
        self.status = 'Playing'
    
    
    def getColumnBase(self, column):
        base = 0
        for item in range(len(self.gameGrid[column])):
            if self.gameGrid[column][item] != 0:
                base = item + 1
        return base
            
            
    def isAtMax(self, column):
        if self.getColumnBase(column) == COLUMNHEIGHT:
            return True
        return False
                
        
    def addToColumn(self, color, column):
        if column < NUMGAMECOLUMNS and column >= 0:
            if self.isAtMax(column):
                self.status = 'Lost'
            self.gameGrid[column][self.getColumnBase(column)] = color
        else:
            raise IndexError('Column does not exist')
                    
                    
    def dropBugSetInColumn(self, bugSet, column):
        if bugSet.position == 'upPosition':
            self.addToColumn(bugSet.bugColor1, column)
            self.addToColumn(bugSet.bugColor2, column)
        if bugSet.position == 'downPosition':
            self.addToColumn(bugSet.bugColor2, column)
            self.addToColumn(bugSet.bugColor1, column)
        if bugSet.position == 'leftPosition':
            self.addToColumn(bugSet.bugColor1, column)
            self.addToColumn(bugSet.bugColor2, column - 1)
        if bugSet.position == 'rightPosition':
            self.addToColumn(bugSet.bugColor1, column)
            self.addToColumn(bugSet.bugColor2, column + 1)    


class BugSet(object):
    def __init__(self):
        self.bugColor1 = random.randint(1, 5)
        self.bugColor2 = random.randint(1, 5)
        self.position = 'upPosition'
        self.location = 2
        
        
    def setPosition(self, newPosition):
        if newPosition == 'upPosition' or newPosition == 'downPosition' or newPosition == 'leftPosition' or newPosition == 'rightPosition':
            self.position = newPosition
        else:
            raise ValueError('Invalid position')
    
    
    

    
        