""" 

[ Difficulty: Hard ]
[ Category: Dynamic Programming ]

##### Longest Common Subsequence #####

Write a function that takes in two strings and returns their longest common subsequence.

A subsequence of a string is a set of characters that aren't necessarily adjacent in 
the string but that are in the same order as they appear in the string. For instance, 
the characters ["a", "c", "d"] form a subsequence of the string "abcd", and so do the 
characters ["b", "d"]. Note that a single character in a string and the string itself 
are both valid subsequences of the string.

You can assume that there will only be one longest common subsequence.


##### Sample Input #####
str1 = "ZXVVYZW"
str2 = "XKYKZPW"

##### Sample Output #####
["X", "Y", "Z", "W"]


##### Hints #####

Hint 1
Try building a two-dimensional array of the longest common subsequences 
of substring pairs of the input strings. Let the rows of the array represent 
substrings of the second input string str2. Let the first row represent the 
empty string. Let each row i thereafter represent the substrings of str2 from 
0 to i, with i excluded. Let the columns similarly represent the first input 
string str1.

Hint 2
Build up the array mentioned in Hint #1 one row at a time. In other words, 
find the longest common subsequences for all the substrings of str1 
represented by the columns and the empty string represented by the first 
row, then for all the substrings of str1 represented by the columns and the 
first letter of str2 represented by the second row, etc., until you compare 
both full strings. Find a formula that relates the longest common 
subsequence at any given point to previous subsequences.

Hint 3
Do you really need to build and store subsequences at each point in the 
two-dimensional array mentioned in Hint #1? Try storing booleans to 
determine whether or not a letter at a given point in the two-dimensional 
array is part of the longest common subsequence as well as pointers to 
determine what should come before this letter in the final subsequence. 
Use these pointers to backtrack your way through the array and to build 
up the longest common subsequence at the end of your algorithm.

Optimal Space & Time Complexity
O(nm) time | O(nm) space - where n and m are the lengths of the two input strings

"""





##### Solution 1 #####
# O(nm*min(n, m)) time | O(nm*min(n, m)) space
def longestCommonSubsequence(str1, str2):
    lcs = [[[] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + [str2[i - 1]]
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key=len)
    return lcs[-1][-1]





##### Solution 2 #####
# O(nm*min(n, m)) time | O((min(n, m))^2) space
def longestCommonSubsequence(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    evenLcs = [[] for x in range(len(small) + 1)]
    oddLcs = [[] for x in range(len(small) + 1)]
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            currentLcs = oddLcs
            previousLcs = evenLcs
        else:
            currentLcs = evenLcs
            previousLcs = oddLcs
        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                currentLcs[j] = previousLcs[j - 1] + [big[i - 1]]
            else:
                currentLcs[j] = max(previousLcs[j], currentLcs[j - 1], key=len)
    return evenLcs[-1] if len(big) % 2 == 0 else oddLcs[-1]





##### Solution 3 #####
# O(nm) time | O(nm) space
def longestCommonSubsequence(str1, str2):
    lcs = [[[None, 0, None, None] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                lcs[i][j] = [str2[i - 1], lcs[i - 1][j - 1][1] + 1, i - 1, j - 1]
            else:
                if lcs[i - 1][j][1] > lcs[i][j - 1][1]:
                    lcs[i][j] = [None, lcs[i - 1][j][1], i - 1, j]
                else:
                    lcs[i][j] = [None, lcs[i][j - 1][1], i, j - 1]
    return buildSequence(lcs)


def buildSequence(lcs):
    sequence = []
    i = len(lcs) - 1
    j = len(lcs[0]) - 1
    while i != 0 and j != 0:
        currentEntry = lcs[i][j]
        if currentEntry[0] is not None:
            sequence.append(currentEntry[0])
        i = currentEntry[2]
        j = currentEntry[3]
    return list(reversed(sequence))





##### Solution 4 #####
# O(nm) time | O(nm) space
def longestCommonSubsequence(str1, str2):
    lengths = [[0 for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                lengths[i][j] = lengths[i - 1][j - 1] + 1
            else:
                lengths[i][j] = max(lengths[i - 1][j], lengths[i][j - 1])
    return buildSequence(lengths, str1)


def buildSequence(lengths, string):
    sequence = []
    i = len(lengths) - 1
    j = len(lengths[0]) - 1
    while i != 0 and j != 0:
        if lengths[i][j] == lengths[i - 1][j]:
            i -= 1
        elif lengths[i][j] == lengths[i][j - 1]:
            j -= 1
        else:
            sequence.append(string[j - 1])
            i -= 1
            j -= 1  
    return list(reversed(sequence))
