"""

[ Difficulty: Hard ]
[ Category: Graphs ]

##### Largest Island #####

You're given a two-dimensional array (a matrix) of potentially unequal height and 
width containing only 0s and 1s. Each 1 represents water, and each 0 represents 
part of a land mass. A land mass consists of any number of 0s that are either 
horizontally or vertically adjacent (but not diagonally adjacent). The number of 
adjacent 0s forming a land mass determine its size.

Note that a land mass can twist. In other words, it doesn't have to be a straight 
vertical line or a straight horizontal line; it can be L-shaped, for example.

Write a function that returns the largest possible land mass size after changing 
exactly one 1 to a 0. Note that the given matrix will always contain at least one 
1, and you may mutate the matrix.


##### Sample Input #####
matrix = [ 
  [0, 1, 1], 
  [0, 0, 1], 
  [1, 1, 0]
]

##### Sample Output #####
  // Switching either matrix[1][2] or matrix[2][1]
5 // creates a land mass of size 5

##### Hints #####

Hint 1
A brute force approach to this problem would be to try changing every 1 into a 0. 
From there, you can check what the largest land mass size is from the newly changed 
index.

Hint 2
The brute force approach potentially calculates the size of the same land mass 
multiple times. Can you try to optimize this?

Hint 3
You can change values in the matrix to help keep track of additional useful 
information about a given index.

Hint 4
Try first precomputing the sizes of each land mass. Changing any 1 would then create 
a new land mass of the combined sizes of all its adjacent land masses plus one to 
account for the newly changed value.

Hint 5
To avoid double counting land masses, try updating the matrix with unique identifiers 
for each land mass to know which 0's are from the same land mass.

Optimal Space & Time Complexity
O(w * h) time | O(w * h) space - where w is the width of the matrix, and h is the 
height of the matrix

"""





##### Solution 1 #####
# O(w^2 * h^2) time | O(w * h) space - where w is the width of the matrix, and
# h is the height of the matrix
def largestIsland(matrix):
    maxSize = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                continue

            maxSize = max(maxSize, getSizeFromNode(row, col, matrix))

    return maxSize


def getSizeFromNode(row, col, matrix):
    size = 1
    visited = [[False for value in row] for row in matrix]
    nodesToExplore = getLandNeighbors(row, col, matrix)
    while len(nodesToExplore) > 0:
        currentNode = nodesToExplore.pop()
        currentRow, currentCol = currentNode[0], currentNode[1]

        if visited[currentRow][currentCol]:
            continue

        visited[currentRow][currentCol] = True
        size += 1
        nodesToExplore += getLandNeighbors(currentRow, currentCol, matrix)

    return size


def getLandNeighbors(row, col, matrix):
    landNeighbors = []
    if row > 0 and matrix[row - 1][col] != 1:
        landNeighbors.append([row - 1, col])
    if row < len(matrix) - 1 and matrix[row + 1][col] != 1:
        landNeighbors.append([row + 1, col])
    if col > 0 and matrix[row][col - 1] != 1:
        landNeighbors.append([row, col - 1])
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] != 1:
        landNeighbors.append([row, col + 1])

    return landNeighbors


# Solution 2
# O(w * h) time | O(w * h) space - where w is the width of the matrix, and
# h is the height of the matrix
def largestIsland(matrix):
    islandSizes = []
    # islandNumber starts at 2 to avoid overwriting existing 0s and 1s
    islandNumber = 2
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                islandSizes.append(getSizeFromNode(row, col, matrix, islandNumber))
                islandNumber += 1

    maxSize = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 1:
                continue

            landNeighbors = getLandNeighbors(row, col, matrix)
            islands = set()
            for neighbor in landNeighbors:
                islands.add(matrix[neighbor[0]][neighbor[1]])

            size = 1
            for island in islands:
                size += islandSizes[island - 2]
            maxSize = max(maxSize, size)

    return maxSize


def getSizeFromNode(row, col, matrix, islandNumber):
    size = 0
    nodesToExplore = [[row, col]]
    while len(nodesToExplore) > 0:
        currentNode = nodesToExplore.pop()
        currentRow, currentCol = currentNode[0], currentNode[1]

        if matrix[currentRow][currentCol] != 0:
            continue

        matrix[currentRow][currentCol] = islandNumber
        size += 1
        nodesToExplore += getLandNeighbors(currentRow, currentCol, matrix)

    return size


def getLandNeighbors(row, col, matrix):
    landNeighbors = []
    if row > 0 and matrix[row - 1][col] != 1:
        landNeighbors.append([row - 1, col])
    if row < len(matrix) - 1 and matrix[row + 1][col] != 1:
        landNeighbors.append([row + 1, col])
    if col > 0 and matrix[row][col - 1] != 1:
        landNeighbors.append([row, col - 1])
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] != 1:
        landNeighbors.append([row, col + 1])

    return landNeighbors
