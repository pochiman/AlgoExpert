

# O(nlog(m)) time | O(n + log(m)) space - where n is the number
# of build runs and m is the length of the longest build run
def buildFailures(buildRuns):
    greenPercentages = list(map(calculateGreenPercentage, buildRuns))
    return getLongestDecreasingSubarrayLength(greenPercentages)


def calculateGreenPercentage(buildRun):
    firstFalseIdx = binarySearchForFirstFalse(buildRun, 0, len(buildRun) - 1)
    return firstFalseIdx / len(buildRun)


# Recursive Binary Search.
def binarySearchForFirstFalse(array, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return -1

    middleIdx = (leftIdx + rightIdx) // 2
    isFalse = not array[middleIdx]
    if isFalse:
        isFirstFalse = middleIdx == 0 or array[middleIdx - 1]
        if isFirstFalse:
            return middleIdx
        else:
            return binarySearchForFirstFalse(array, leftIdx, middleIdx - 1)
    else:
        return binarySearchForFirstFalse(array, middleIdx + 1, rightIdx)


def getLongestDecreasingSubarrayLength(array):
    longestLength = 1
    currentLongestLength = 1

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            currentLongestLength += 1
            longestLength = max(longestLength, currentLongestLength)
        else:
            currentLongestLength = 1

    return longestLength if longestLength > 1 else -1
