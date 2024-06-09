""" 

[ Difficulty: Medium ]
[ Category: Recursion ]

##### Reveal Minesweeper #####

Minesweeper is a popular video game. From Wikipedia, "The game features a grid 
of clickable squares, with hidden "mines" scattered throughout the board. The 
objective is to clear the board without detonating any mines, with help from 
clues about the number of neighboring mines in each field."Specifically, when 
a player clicks on a square (also called a cell) that doesn't contain a mine, 
the square reveals a number representing the number of immediately adjacent 
mines (including diagonally adjacent mines).

You're given a two-dimensional array of strings that represents a Minesweeper 
board for a game in progress. You're also given a row and a column representing 
the indices of the next square that the player clicks on the board. Write a 
function that returns an updated board after the click (your function can 
mutate the input board).

The board will always contain only strings, and each string will be one of the 
following:

    • "M": A mine that has not been clicked on.

    • "X": A mine that has been clicked on, indicating a lost game.

    • "H": A cell with no mine, but whose content is still hidden to the player.

    • "0-8": A cell with no mine, with an integer from 0 to 8 representing 
      the number of adjacent mines. Note that this is a single-digit integer 
      represented as a string. For example "2" would mean there are 2 adjacent 
      cells with mines. Numbered cells are not clickable as they have already 
      been revealed.

If the player clicks on a mine, replace the "M" with "X", indicating the game 
was lost.

If the player clicks on a cell adjacent to a mine, replace the "H" with a string 
representing the number of adjacent mines.

If the player clicks on a cell with no adjacent mines, replace the "H" with "0". 
Additionally, reveal all of the adjacent hidden cells as if the player had clicked 
on those cells as well.

You can assume the given row and column will always represent a legal move. 
The board can be of any size and have any number of mines in it.


##### Sample Input #1 #####
board = [
  ["M", "M"],
  ["H", "H"],
  ["H", "H"]
]   
row = 2
column = 0

##### Sample Output #1 #####
[
  ["M", "M"],
  ["2", "2"],
  ["0", "0"]
]

##### Sample Input #2 #####
board = [
  ["H", "H", "H", "H", "M"],
  ["H", "1", "M", "H", "1"],
  ["H", "H", "H", "H", "H"],
  ["H", "H", "H", "H", "H"]
]   
row = 3
column = 4

##### Sample Output #2 #####
[
  ["0", "1", "H", "H", "M"],
  ["0", "1", "M", "2", "1"],
  ["0", "1", "1", "1", "0"],
  ["0", "0", "0", "0", "0"]
]

##### Hints #####

Hint 1
While the input is a 2D array, this problem can also be thought of as a graph
problem. Each cell is a node, each with up to 8 edges to their adjacent cells.

Hint 2
If the player clicks on a cell with no adjacent mines, it is as if they clicked 
on all of the hidden cells adjacent to that cell as well. Try solving this 
recursively, running the function again on those adjacent cells.

Hint 3
Doing DFS or BFS through all of the adjacent cells without mines will be the
most efficient way to find and reveal them all.

Optimal Space & Time Complexity
O(w * h) time | O(w * h) space - where w is the width of the board, and h is 
the height of the board

"""





##### Solution 1 #####
# O(w * h) time | O(w * h) space - where w is the width of the board, and
# h is the height of the board
def revealMinesweeper(board, row, column):
    if board[row][column] == "M":
        board[row][column] = "X"
        return board

    neighbors = getNeighbors(board, row, column)
    adjacentMinesCount = 0
    for neighborRow, neighborColumn in neighbors:
        if board[neighborRow][neighborColumn] == "M":
            adjacentMinesCount += 1

    if adjacentMinesCount > 0:
        board[row][column] = str(adjacentMinesCount)
    else:
        board[row][column] = "0"
        for neighborRow, neighborColumn in neighbors:
            if board[neighborRow][neighborColumn] == "H":
                revealMinesweeper(board, neighborRow, neighborColumn)

    return board


def getNeighbors(board, row, column):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    neighbors = []
    for directionRow, directionColumn in directions:
        newRow = row + directionRow
        newColumn = column + directionColumn
        if 0 <= newRow < len(board) and 0 <= newColumn < len(board[0]):
            neighbors.append([newRow, newColumn])

    return neighbors
