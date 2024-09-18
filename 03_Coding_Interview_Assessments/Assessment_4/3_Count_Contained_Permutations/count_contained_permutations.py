

# O(b + s) time | O(s) space - where b is the length of the big
# input string and s is the length of the small input string
def countContainedPermutations(bigString, smallString):
    smallStringCharCounts = getCharCounts(smallString)
    numUniqueChars = len(smallStringCharCounts.keys())

    runningCharCounts = {}
    permutationsCount = 0
    numUniqueCharsDone = 0
    leftIdx = 0
    rightIdx = 0
    while rightIdx < len(bigString):
        rightChar = bigString[rightIdx]
        if rightChar in smallStringCharCounts:
            increaseCharCount(rightChar, runningCharCounts)

            if runningCharCounts[rightChar] == smallStringCharCounts[rightChar]:
                numUniqueCharsDone += 1

        if numUniqueCharsDone == numUniqueChars:
            permutationsCount += 1

        rightIdx += 1
        shouldIncrementLeftIdx = rightIdx - leftIdx == len(smallString)
        if not shouldIncrementLeftIdx:
            continue

        leftChar = bigString[leftIdx]
        if leftChar in smallStringCharCounts:
            if runningCharCounts[leftChar] == smallStringCharCounts[leftChar]:
                numUniqueCharsDone -= 1

            decreaseCharCount(leftChar, runningCharCounts)

        leftIdx += 1

    return permutationsCount


def getCharCounts(string):
    charCounts = {}
    for char in string:
        increaseCharCount(char, charCounts)
    return charCounts


def increaseCharCount(char, charCounts):
    if char not in charCounts:
        charCounts[char] = 0
    charCounts[char] += 1


def decreaseCharCount(char, charCounts):
    charCounts[char] -= 1
