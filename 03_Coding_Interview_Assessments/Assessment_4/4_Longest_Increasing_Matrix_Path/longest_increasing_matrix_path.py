

# O(n) time | O(n) space - where n is the total number of elements in the matrix
def longestIncreasingMatrixPath(matrix):
    longestPathLengths = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(None)
        longestPathLengths.append(row)

    longestPathLength = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            longestPathLength = max(
                getLongestPathLengthAt(matrix, row, col, float("-inf"), longestPathLengths),
                longestPathLength,
            )

    return longestPathLength


def getLongestPathLengthAt(matrix, row, col, lastPathValue, longestPathLengths):
    isOutOfBounds = row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0])
    if isOutOfBounds:
        return 0

    currentValue = matrix[row][col]
    if currentValue <= lastPathValue:
        return 0

    if longestPathLengths[row][col] is None:
        longestPathLengths[row][col] = 1 + max(
            getLongestPathLengthAt(matrix, row - 1, col, currentValue, longestPathLengths),
            getLongestPathLengthAt(matrix, row + 1, col, currentValue, longestPathLengths),
            getLongestPathLengthAt(matrix, row, col - 1, currentValue, longestPathLengths),
            getLongestPathLengthAt(matrix, row, col + 1, currentValue, longestPathLengths),
        )

    return longestPathLengths[row][col]
