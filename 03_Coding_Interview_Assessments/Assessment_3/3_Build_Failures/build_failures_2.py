

# O(nlog(m)) time | O(1) space - where n is the number of
# build runs and m is the length of the longest build run
def buildFailures(buildRuns):
    longestLength = 1
    currentLongestLength = 1
    previousGreenPercentage = calculateGreenPercentage(buildRuns[0])

    for i in range(1, len(buildRuns)):
        currentGreenPercentage = calculateGreenPercentage(buildRuns[i])
        if currentGreenPercentage < previousGreenPercentage:
            currentLongestLength += 1
            longestLength = max(longestLength, currentLongestLength)
        else:
            currentLongestLength = 1
        previousGreenPercentage = currentGreenPercentage

    return longestLength if longestLength > 1 else -1


def calculateGreenPercentage(buildRun):
    firstFalseIdx = binarySearchForFirstFalse(buildRun)
    return firstFalseIdx / len(buildRun)


# Iterative Binary Search.
def binarySearchForFirstFalse(array):
    leftIdx = 0
    rightIdx = len(array) - 1

    while leftIdx <= rightIdx:
        middleIdx = (leftIdx + rightIdx) // 2
        isFalse = not array[middleIdx]
        if isFalse:
            isFirstFalse = middleIdx == 0 or array[middleIdx - 1]
            if isFirstFalse:
                return middleIdx
            else:
                rightIdx = middleIdx - 1
        else:
            leftIdx = middleIdx + 1

    return -1
