

# O(n) time | O(1) space - where n is the total number of elements in the array
def spinRings(array):
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array) - 1

    while startRow < endRow and startCol < endCol:
        originalTopRightValue = array[startRow][endCol]

        for col in reversed(range(startCol + 1, endCol + 1)):
            array[startRow][col] = array[startRow][col - 1]

        for row in range(startRow, endRow):
            array[row][startCol] = array[row + 1][startCol]

        for col in range(startCol, endCol):
            array[endRow][col] = array[endRow][col + 1]

        for row in reversed(range(startRow + 2, endRow + 1)):
            array[row][endCol] = array[row - 1][endCol]

        array[startRow + 1][endCol] = originalTopRightValue

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
