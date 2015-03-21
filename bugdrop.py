GAMEWIDTH = 6
GAMEHEIGHT = 12

class BugDrop(object):
    def __init__(self):
        self.gameGrid = [[0 for x in range(GAMEHEIGHT)] for x in range(GAMEWIDTH)]      #grid = list of columns
        self.base = [0 for x in range(GAMEWIDTH)]
    
    
    def addToColumn(self, color, column):
        if column < GAMEWIDTH or column > 0:
            self.gameGrid[column][self.base[column]] = color
        else:
            raise IndexError('Column does not exist')
            
            
    def isAtMax(self, column):
        if self.base[column] == GAMEHEIGHT - 1:
            return True
        return False
        
    
    def updateBase(self):
        for column in range(len(self.gameGrid)):
            for row in range(len(self.gameGrid[column])):
                if self.gameGrid[column][row] != 0:
                    self.base[column] = row + 1

        
    

    
        