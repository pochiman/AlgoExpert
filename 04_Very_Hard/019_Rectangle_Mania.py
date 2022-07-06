""" 

##### Rectangle Mania #####

Write a function that takes in a list of Cartesian coordinates (i.e., (x, y) 
coordinates) and returns the number of rectangles formed by these coordinates.

A rectangle must have its four corners amongst the coordinates in order to be 
counted, and we only care about rectangles with sides parallel to the x and y 
axes (i.e., with horizontal and vertical sides--no diagonal sides).

You can also assume that no coordinate will be farther than 100 units from the 
origin.


##### Sample Input #####
coords = [
  [0, 0], [0, 1], [1, 1], [1, 0], 
  [2, 1], [2, 0], [3, 1], [3, 0], 
]

##### Sample Output #####
6


##### Hints #####

Hint 1
Try treating every coordinate as the potential lower left corner of a rectangle. 
What conditions would need to be met in order to actually have a rectangle with 
any given coordinate as its lower left corner?

Hint 2
Following Hint #1, if you treat every coordinate as the potential lower left 
corner of a rectangle, you can move in a clockwise pattern (i.e., directly up, 
then directly right, then directly down, and finally directly left) to try to 
find a rectangle. There are a few ways to do this, one of which involves storing, 
for every coordinate, all other coordinates that are directly above it, directly 
to the right of it, directly below it, and directly to the left of it. With this 
information, you can iterate through all of the coordinates and then traverse 
through potential rectangles in an up-right-down-left pattern.

Hint 3
Following Hint #2, do you actually need to store all of the coordinates above, 
to the right, below, and to the left of every coordinate?

Hint 4
Another, perhaps more clever way of solving this problem is to realize that, 
for any coordinate to be a valid lower left corner of a rectangle, there must 
be a corresponding upper right corner of the same rectangle, which is just 
another coordinate located to the upper right of the first coordinate. If you 
have two such coordinates, you should be able to easily find whether 
corresponding upper left and lower right corners exist.

Optimal Space & Time Complexity
O(n^2) time | O(n) space - where n is the number of coordinates

"""





##### Solution 1 #####
# O(n^2) time | O(n^2) space - where n is the number of coordinates
def rectangleMania(coords):
  coordsTable = getCoordsTable(coords)
  return getRectangleCount(coords, coordsTable)  


def getCoordsTable(coords):
  coordsTable = {}
  for coord1 in coords:
    coord1Directions = {UP: [], RIGHT: [], DOWN: [], LEFT: []}
    for coord2 in coords:
      coord2Direction = getCoordDirection(coord1, coord2)  
      if coord2Direction in coord1Directions:
        coord1Directions[coord2Direction].append(coord2)
    coord1String = coordToString(coord1)      
    coordsTable[coord1String] = coord1Directions
  return coordsTable


def getCoordDirection(coord1, coord2):
  x1, y1 = coord1
  x2, y2 = coord2
  if y2 == y1:
    if x2 > x1:
      return RIGHT
    elif x2 < x1:
      return LEFT
  elif x2 == x1:
    if y2 > y1:
      return UP
    elif y2 < y1:
      return DOWN
  return ""      


def getRectangleCount(coords, coordsTable):
  rectangleCount = 0
  for coord in coords:
    rectangleCount += clockwiseCountRectangles(coord, coordsTable, UP, coord)  
  return rectangleCount

    
def clockwiseCountRectangles(coord, coordsTable, direction, origin):
  coordString = coordToString(coord)
  if direction == LEFT:
    rectangleFound = origin in coordsTable[coordString][LEFT]
    return 1 if rectangleFound else 0
  else:
    rectangleCount = 0
    nextDirection = getNextClockwiseDirection(direction)
    for nextCoord in coordsTable[coordString][direction]:
      rectangleCount += clockwiseCountRectangles(nextCoord, coordsTable, nextDirection, origin)  
    return rectangleCount    


def getNextClockwiseDirection(direction):
  if direction == UP:
    return RIGHT
  if direction == RIGHT:
    return DOWN
  if direction == DOWN:
    return LEFT
  return ""    


def coordToString(coord):
  x, y = coord
  return str(x) + "-" + str(y)  


UP = "up"
RIGHT = "right"
DOWN = "down"
LEFT = "left"





##### Solution 2 #####
# O(n^2) time | O(n) space - where n is the number of coordinates
def rectangleMania(coords):
  coordsTable = getCoordsTable(coords)
  return getRectangleCount(coords, coordsTable)  


def getCoordsTable(coords):
  coordsTable = {"x": {}, "y": {}}
  for coord in coords:
    x, y = coord
    if x not in coordsTable["x"]:
      coordsTable["x"][x] = []
    coordsTable["x"][x].append(coord)
    if y not in coordsTable["y"]:
      coordsTable["y"][y] = []
    coordsTable["y"][y].append(coord)    
  return coordsTable


def getRectangleCount(coords, coordsTable):
  rectangleCount = 0
  for coord in coords:
    lowerLeftY = coord[1]  
    rectangleCount += clockwiseCountRectangles(coord, coordsTable, UP, lowerLeftY)  
  return rectangleCount

    
def clockwiseCountRectangles(coord1, coordsTable, direction, lowerLeftY):
  x1, y1 = coord1
  if direction == DOWN:
    relevantCoords = coordsTable["x"][x1]
    for coord2 in relevantCoords:
      lowerRightY = coord2[1]  
      if lowerRightY == lowerLeftY:
        return 1  
    return 0  
  else:  
    rectangleCount = 0
    if direction == UP:
      relevantCoords = coordsTable["x"][x1]
      for coord2 in relevantCoords:
        y2 = coord2[1]
        isAbove = y2 > y1
        if isAbove:
          rectangleCount += clockwiseCountRectangles(coord2, coordsTable, RIGHT, lowerLeftY)  
    elif direction == RIGHT:
      relevantCoords = coordsTable["y"][y1]
      for coord2 in relevantCoords:
        x2 = coord2[0]
        isRight = x2 > x1
        if isRight:
          rectangleCount += clockwiseCountRectangles(coord2, coordsTable, DOWN, lowerLeftY)  
    return rectangleCount


UP = "up"
RIGHT = "right"
DOWN = "down"





##### Solution 3 #####
# O(n^2) time | O(n) space - where n is the number of coordinates
def rectangleMania(coords):
  coordsTable = getCoordsTable(coords)
  return getRectangleCount(coords, coordsTable)  


def getCoordsTable(coords):
  coordsTable = {}
  for coord in coords:
    coordString = coordToString(coord)
    coordsTable[coordString] = True  
  return coordsTable


def getRectangleCount(coords, coordsTable):
  rectangleCount = 0
  for x1, y1 in coords:
    for x2, y2 in coords:
      if not isInUpperRight([x1, y1], [x2, y2]):
        continue
      upperCoordString = coordToString([x1, y2])
      rightCoordString = coordToString([x2, y1])
      if upperCoordString in coordsTable and rightCoordString in coordsTable:    
        rectangleCount += 1
  return rectangleCount

    
def isInUpperRight(coord1, coord2):
  x1, y1 = coord1
  x2, y2 = coord2
  return x2 > x1 and y2 > y1
    

def coordToString(coord):
  x, y = coord
  return str(x) + "-" + str(y)
