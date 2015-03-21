import random

NUMGAMECOLUMNS = 6
COLUMNHEIGHT = 12


class BugDrop(object):
    def __init__(self):
        self.gameGrid = [[0 for x in range(COLUMNHEIGHT)] for x in range(NUMGAMECOLUMNS)]      
    
    
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
                raise IndexError('Column is full')
            self.gameGrid[column][self.getColumnBase(column)] = color
        else:
            raise IndexError('Column does not exist')
                    
                    
    def dropBugSetInColumn(self, bugSet, column):
        if bugSet.position == 'up':
            self.addToColumn(bugSet.bugColor1, column)
            self.addToColumn(bugSet.bugColor2, column)
            self.addToColumn(bugSet.bugColor3, column)


class BugSet(object):
    def __init__(self):
        self.bugColor1 = random.randint(1, 5)
        self.bugColor2 = random.randint(1, 5)
        self.bugColor3 = random.randint(1, 5)
        self.position = 'up'
        self.location = (-1, -1)
        
        
    def setPosition(self, newPosition):
        if newPosition == 'up' or newPosition == 'down' or newPosition == 'left' or newPosition == 'right':
            self.position = newPosition
        else:
            raise ValueError('Invalid position')
    

    
        