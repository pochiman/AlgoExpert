

# O(n^2) time | O(1) space - where n is the length of the input array
def balanceIndex(array):
    for i in range(len(array)):
        leftSideSum = 0
        rightSideSum = 0

        for j in range(i):
            leftSideSum += array[j]

        for j in range(i + 1, len(array)):
            rightSideSum += array[j]

        if leftSideSum == rightSideSum:
            return i

    return -1
