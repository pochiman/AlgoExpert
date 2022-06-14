""" 

##### Remove Islands #####

You're given a two-dimensional array (a matrix) of potentially unequal height and 
width containing only 0s and 1s.  The matrix represents a two-toned image, where 
each 1 represents black and each 0 represents white.  An island is defined as any 
number of 1s that are horizontally or vertically adjacent (but not diagonally 
adjacent) and that don't touch the border of the image.  In other words, a group 
of horizontally or vertically adjacent 1s isn't an island if any of those 1s are 
in the first row, last row, first column, or last column of the input matrix.

Note that an island can twist.  In other words, it doesn't have to be a straight 
vertical line or a straight horizontal line; it can be L-shaped, for example.

You can think of islands as patches of black that don't touch the border of the 
two-toned image.

Write a function that returns a modified version of the input matrix, where all of 
the islands are removed.  You remove an island by replacing it with 0s.

Naturally, you're allowed to mutate the input matrix.


##### Sample Input #####
matrix = 
[
  [1, 0, 0, 0, 0, 0], 
  [0, 1, 0, 1, 1, 1], 
  [0, 0, 1, 0, 1, 0], 
  [1, 1, 0, 0, 1, 0], 
  [1, 0, 1, 1, 0, 0], 
  [1, 0, 0, 0, 0, 1], 
]

##### Sample Output #####
[
  [1, 0, 0, 0, 0, 0], 
  [0, 0, 0, 1, 1, 1], 
  [0, 0, 0, 0, 1, 0], 
  [1, 1, 0, 0, 1, 0], 
  [1, 0, 0, 0, 0, 0], 
  [1, 0, 0, 0, 0, 1], 
]
// The islands that were removed can be clearly seen here:
// [
//   [ ,  ,  ,  ,  ,  ], 
//   [ , 1,  ,  ,  ,  ], 
//   [ ,  , 1,  ,  ,  ], 
//   [ ,  ,  ,  ,  ,  ], 
//   [ ,  , 1, 1,  ,  ], 
//   [ ,  ,  ,  ,  ,  ], 
// ]



##### Hints #####

Hint 1
How would you solve this problem if you knew the positions of all the non-
island 1s?

Hint 2
Find and store the positions of all the non-island 1s.  You can do this by 
performing a graph traversal (depth-first search, for example) on all the 1s
that are on the border of the image.  Afterwards, you can easily identify and 
remove all the island 1s from the input matrix by relying on the data 
structure that you used to store the positions of non-island 1s.

Hint 3
You can also solve this problem without the use of a data structure that 
stores the positions of non-island 1s.  Simply loop through the border of the 
image, and perform a depth-first search on all positions with the value 1.
During this depth-first search, find all the 1s that are connected to the 
original position on the border, and change them from 1 to 2.  After changing 
all non-island 1s to 2s, you can simply remove all the remaining 1s, which 
are guaranteed to be islands, from the matrix (by replacing them with 0s), 
and you can then change all the 2s back to 1s, since these were previously 
determined to be non-islands.

Optimal Space & Time Complexity
O(wh) time | O(wh) space - where w and h are the width and height of the 
input matrix

"""





##### Solution 1 #####
# O(wh) time | O(wh) space - where w and h 
# are the width and height of the input matrix
def removeIslands(matrix):
  onesConnectedToBorder = [[False for col in matrix[0]] for row in matrix]

  # Find all the 1s that are not islands
  for row in range(len(matrix)):
    for col in range(len(matrix[row])):
      rowIsBorder = row == 0 or row == len(matrix) - 1
      colIsBorder = col == 0 or col == len(matrix[row]) - 1
      isBorder = rowIsBorder or colIsBorder
      if not isBorder:
        continue

      if matrix[row][col] != 1:
        continue

      findOnesConnectedToBorder(matrix, row, col, onesConnectedToBorder)

  for row in range(1, len(matrix) - 1):
    for col in range(1, len(matrix[row]) - 1):
      if onesConnectedToBorder[row][col]:
        continue

      matrix[row][col] = 0

  return matrix


def findOnesConnectedToBorder(matrix, startRow, startCol, onesConnectedToBorder):
  stack = [(startRow, startCol)]

  while len(stack) > 0:
    currentPosition = stack.pop()
    currentRow, currentCol = currentPosition

    alreadyVisited = onesConnectedToBorder[currentRow][currentCol]
    if alreadyVisited:
      continue

    onesConnectedToBorder[currentRow][currentCol] = True

    neighbors = getNeighbors(matrix, currentRow, currentCol)
    for neighbor in neighbors:
      row, col = neighbor

      if matrix[row][col] != 1:
        continue

      stack.append(neighbor)


def getNeighbors(matrix, row, col):
  neighbors = []

  numRows = len(matrix)
  numCols = len(matrix[row])

  if row - 1 >= 0:  # UP
    neighbors.append((row - 1, col))
  if row + 1 < numRows:  # DOWN
    neighbors.append((row + 1, col))
  if col - 1 >= 0:  # LEFT
    neighbors.append((row, col - 1))
  if col + 1 < numCols:  # RIGHT
    neighbors.append((row, col + 1))

  return neighbors





##### Solution 2 #####
# O(wh) time | O(wh) space - where w and h 
# are the width and height of the input matrix
def removeIslands(matrix):
  for row in range(len(matrix)):
    for col in range(len(matrix[row])):
      rowIsBorder = row == 0 or row == len(matrix) - 1
      colIsBorder = col == 0 or col == len(matrix[row]) - 1
      isBorder = rowIsBorder or colIsBorder
      if not isBorder:
        continue

      if matrix[row][col] != 1:
        continue

      changeOnesConnectedToBorderToTwos(matrix, row, col)

  for row in range(len(matrix)):
    for col in range(len(matrix[row])):
      color = matrix[row][col]
      if color == 1:
        matrix[row][col] = 0
      elif color == 2:
        matrix[row][col] = 1  

  return matrix


def changeOnesConnectedToBorderToTwos(matrix, startRow, startCol):
  stack = [(startRow, startCol)]

  while len(stack) > 0:
    currentPosition = stack.pop()
    currentRow, currentCol = currentPosition

    matrix[currentRow][currentCol] = 2

    neighbors = getNeighbors(matrix, currentRow, currentCol)
    for neighbor in neighbors:
      row, col = neighbor

      if matrix[row][col] != 1:
        continue

      stack.append(neighbor)


def getNeighbors(matrix, row, col):
  neighbors = []

  numRows = len(matrix)
  numCols = len(matrix[row])

  if row - 1 >= 0:  # UP
    neighbors.append((row - 1, col))
  if row + 1 < numRows:  # DOWN
    neighbors.append((row + 1, col))
  if col - 1 >= 0:  # LEFT
    neighbors.append((row, col - 1))
  if col + 1 < numCols:  # RIGHT
    neighbors.append((row, col + 1))

  return neighbors
