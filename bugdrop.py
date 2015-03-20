#IMPORT
import sys, pygame, random
from pygame.locals import *

#INITIALIZE
MAINWIDTH = 800
MAINHEIGHT = 600

CELLSIZE = 34
assert CELLSIZE % 2 == 0, "Cellsize must be even"
assert CELLSIZE * 6  < MAINWIDTH, "Main width not enough"
assert CELLSIZE * 16 < MAINHEIGHT, "Main height not enough"
GAMEXCELLS = 6
GAMEYCELLS = 12

WHITE = ( 255, 255, 255)
RED = ( 255, 0, 0)
DARKRED = ( 155, 0, 0)
GREEN = ( 0, 255, 0)
DARKGREEN = ( 0, 155, 0)
BLUE = ( 0, 0, 255)
DARKBLUE = ( 0, 0, 155)
PURPLE = ( 255, 0, 255)
DARKPURPLE = ( 155, 0, 155)
YELLOW = ( 255, 255, 0)
DARKYELLOW = ( 155, 155, 0)
BLACK = ( 0, 0, 0)

REDBUG = 1
GREENBUG = 2
BLUEBUG = 3
PURPLEBUG = 4
YELLOWBUG = 5

LEFT = 'left'
RIGHT = 'right'
DOWN = 'down'

UPPOS = 'up position'
LEFTPOS = 'left position'
DOWNPOS = 'down position'
RIGHTPOS = 'right position'

CLOCKWISE = 2
COUNTERCLOCKWISE = 1

def main():
    global MAINFRAME, GAMEWIDTH, GAMEHEIGHT, GAMEPOSITIONX, GAMEPOSITIONY
    
    GAMEWIDTH = CELLSIZE * GAMEXCELLS
    GAMEHEIGHT = CELLSIZE * GAMEYCELLS
    GAMEPOSITIONX = MAINWIDTH / 2 + MAINWIDTH / 8
    GAMEPOSITIONY = CELLSIZE * 4    #number of bugs + 1
    
    pygame.init()
    MAINFRAME = pygame.display.set_mode((MAINWIDTH, MAINHEIGHT))
    pygame.display.set_caption('Bug drop!')
    play = True
    
    while play:
        playGame()
    

def playGame():
    global STARTX, STARTY
    
    STARTX = GAMEPOSITIONX + CELLSIZE * 2 + CELLSIZE / 2
    STARTY = GAMEPOSITIONY - (CELLSIZE / 2) - 10 
    
    nextDrop = [randomBug(), 
                randomBug(), 
                randomBug(), STARTX, STARTY]
    currentDrop = nextDrop
    currentPos = UPPOS
    currentColumn = 2
    
    grid = [[0 for x in range(GAMEXCELLS)] for x in range(GAMEYCELLS)]
    base = [0 for x in range(GAMEXCELLS)]
    
    timer = 0
    lastDrop = 0
    drop = True
    
    while True:
        MAINFRAME.fill(WHITE)
        pygame.draw.rect(MAINFRAME, BLACK, (GAMEPOSITIONX, GAMEPOSITIONY, GAMEWIDTH, GAMEHEIGHT), 5)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        if drop == True:
            currentDrop = nextDrop
            nextDrop = generateNextDrop()
            lastDrop = timer
            drop = False
        elif drop == False and timer - lastDrop > 120:
            drawUpDrop(nextDrop)
            
        if currentDrop[4] != yToPixel(base[currentColumn]):
            currentDrop = moveCurrentDrop(currentDrop)
        else:
            drop = True
            landBug(grid, base, currentDrop, currentPos, currentColumn, base[currentColumn])
            
        if currentPos == UPPOS:
            drawUpDrop(currentDrop)
            
        drawLandedBugs(grid)
        pygame.display.update()
        pygame.time.Clock().tick(100)
        timer += 1
        
        
def yToPixel(y):
    return (11 - y) * CELLSIZE + (CELLSIZE / 2) + GAMEPOSITIONY
    
    
def xToPixel(x):
    return x * CELLSIZE + (CELLSIZE / 2) + GAMEPOSITIONX 

    
def landBug(grid, base, drop, position, column, row):
    if position == UPPOS:
        grid[row + 2][column] = drop[0]
        grid[row + 1][column] = drop[1]
        grid[row][column] = drop[2]
        base[column] += 3

    
def randomBug():
    return random.randint(1, 5)
    

def generateNextDrop():
    nextDrop = [randomBug(), 
                randomBug(), 
                randomBug(), STARTX, STARTY]
    return nextDrop
    

def moveCurrentDrop(drop):
    return [drop[0], drop[1], drop[2], drop[3], drop[4] + 1]
    
    
def drawUpDrop(drop):
    centerX = drop[3]
    centerY3 = drop[4]
    centerY2 = centerY3 - CELLSIZE
    centerY1 = centerY2 - CELLSIZE
    drawBug(drop[0], centerX, centerY1)
    drawBug(drop[1], centerX, centerY2)
    drawBug(drop[2], centerX, centerY3)
    
    
def drawLandedBugs(grid):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] != 0:
                drawBug(grid[row][column], xToPixel(column), yToPixel(row))
    

def drawBug(color, centerX, centerY):
    if color == REDBUG:
        pygame.draw.circle(MAINFRAME, DARKRED, (centerX, centerY), (CELLSIZE / 2), 0)
        pygame.draw.circle(MAINFRAME, RED, (centerX, centerY), (CELLSIZE / 2 - 2), 0)
    elif color == GREENBUG:
        pygame.draw.circle(MAINFRAME, DARKGREEN, (centerX, centerY), (CELLSIZE / 2), 0)
        pygame.draw.circle(MAINFRAME, GREEN, (centerX, centerY), (CELLSIZE / 2 - 2), 0)
    elif color == BLUEBUG:
        pygame.draw.circle(MAINFRAME, DARKBLUE, (centerX, centerY), (CELLSIZE / 2), 0)
        pygame.draw.circle(MAINFRAME, BLUE, (centerX, centerY), (CELLSIZE / 2 - 2), 0)
    elif color == PURPLEBUG:
        pygame.draw.circle(MAINFRAME, DARKPURPLE, (centerX, centerY), (CELLSIZE / 2), 0)
        pygame.draw.circle(MAINFRAME, PURPLE, (centerX, centerY), (CELLSIZE / 2 - 2), 0)
    elif color == YELLOWBUG:
        pygame.draw.circle(MAINFRAME, DARKYELLOW, (centerX, centerY), (CELLSIZE / 2), 0)
        pygame.draw.circle(MAINFRAME, YELLOW, (centerX, centerY), (CELLSIZE / 2 - 2), 0)
        
    
#CALL MAIN
if __name__ == '__main__':
    main()
    
