

# O(n) time | O(w) space - where n is the total number of
# elements in the array and w is the width of the array
def spinRings(array):
    spinRingsHelper(array, 0, len(array) - 1, 0, len(array) - 1)


def spinRingsHelper(array, startRow, endRow, startCol, endCol):
    if startRow >= endRow or startCol >= endCol:
        return

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

    spinRingsHelper(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1)
