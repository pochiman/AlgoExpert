

# O(n) time | O(1) space - where n is the length of the input array
def balanceIndex(array):
    arraySum = sum(array)

    leftSideSum = 0
    rightSideSum = arraySum
    for i in range(len(array)):
        rightSideSum -= array[i]
        if leftSideSum == rightSideSum:
            return i
        leftSideSum += array[i]

    return -1
