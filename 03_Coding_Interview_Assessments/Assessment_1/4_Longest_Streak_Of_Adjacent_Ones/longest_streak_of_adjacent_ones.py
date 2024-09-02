

# O(n) time | O(1) space - where n is the length of the input array
def longestStreakOfAdjacentOnes(array):
    longestStreakLength = 0
    longestStreakReplacedZeroIdx = -1

    currentStreakLength = 0
    replacedZeroIdx = -1

    for i in range(len(array)):
        if array[i] == 1:
            currentStreakLength += 1
        else:
            currentStreakLength = i - replacedZeroIdx
            replacedZeroIdx = i

        if currentStreakLength > longestStreakLength:
            longestStreakLength = currentStreakLength
            longestStreakReplacedZeroIdx = replacedZeroIdx

    return longestStreakReplacedZeroIdx
