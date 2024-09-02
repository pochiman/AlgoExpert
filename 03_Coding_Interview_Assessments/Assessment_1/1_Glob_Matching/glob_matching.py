

# O(n * m) time | O(n * m) space - where n is the length
# of the fileName and m is the length of the pattern.
def globMatching(fileName, pattern):
    matchTable = initializeMatchTable(fileName, pattern)
    for i in range(1, len(fileName) + 1):
        for j in range(1, len(pattern) + 1):
            if pattern[j - 1] == "*":
                matchTable[i][j] = matchTable[i][j - 1] or matchTable[i - 1][j]
            elif pattern[j - 1] == "?" or pattern[j - 1] == fileName[i - 1]:
                matchTable[i][j] = matchTable[i - 1][j - 1]
    return matchTable[len(fileName)][len(pattern)]


def initializeMatchTable(fileName, pattern):
    matchTable = [[False for j in range(len(pattern) + 1)] for i in range(len(fileName) + 1)]

    matchTable[0][0] = True
    for j in range(1, len(pattern) + 1):
        if pattern[j - 1] == "*":
            matchTable[0][j] = matchTable[0][j - 1]

    return matchTable
