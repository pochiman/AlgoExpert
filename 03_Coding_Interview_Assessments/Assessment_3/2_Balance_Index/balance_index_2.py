

# O(n) time | O(n) space - where n is the length of the input array
def balanceIndex(array):
    leftSideSums = array[:]

    leftSideSum = 0
    for i in range(len(array)):
        leftSideSums[i] = leftSideSum
        leftSideSum += array[i]

    rightSideSum = 0
    for i in reversed(range(len(array))):
        if leftSideSums[i] == rightSideSum:
            return i
        rightSideSum += array[i]

    return -1
