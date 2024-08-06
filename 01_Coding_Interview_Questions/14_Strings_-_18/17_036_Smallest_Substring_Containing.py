""" 

[ Difficulty: Very Hard ]
[ Category: Strings ]

##### Smallest Substring Containing #####

You're given two non-empty strings: a big string and a small string. Write a function 
that returns the smallest substring in the big string that contains all of the small 
string's characters.

Note that:

  * The substring can contain other characters not found in the small string.

  * The characters in the substring don't have to be in the same order as they 
    appear in the small string.

  * If the small string has duplicate characters, the substring has to contain 
    those duplicate characters (it can also contain more, but not fewer).

You can assume that there will only be one relevant smallest substring.      


##### Sample Input #####
bigString = "abcd$ef$axb$c$"
smallString = "$$abf" 

##### Sample Output #####
"f$axb$"


##### Hints #####

Hint 1
Try storing all of the small string's character counts in a hash table where 
each character maps to the number of times that it appears in the small string.

Hint 2
Try using two pointers (a left pointer and a right pointer) to traverse through 
the big string. How can this help you find the relevant smallest substring?

Hint 3
With the two pointers mentioned in Hint #2, move the right pointer to the right 
in the big string, keeping track of all the characters you visit in a hash table 
identical to the one mentioned in Hint #1, until you've found all of the 
characters contained in the small string. At that point, move the left pointer to 
the right in the big string, keeping track of all the characters you "lose", and 
stop once you no longer have all of the small string's characters in between the 
left and right pointers. Then, repeat the process by moving the right pointer 
forward and implementing the same logic described in this Hint.

Optimal Space & Time Complexity
O(b + s) time | O(b + s) space - where b is the length of the big input string 
and s is the length of the small input string 

"""





##### Solution 1 #####
# O(b + s) time | O(b + s) space - where b is the length of the big 
# input string and s is the length of the small input string 
def smallestSubstringContaining(bigString, smallString):
    targetCharCounts = getCharCounts(smallString)
    substringBounds = getSubstringBounds(bigString, targetCharCounts)
    return getStringFromBounds(bigString, substringBounds)


def getCharCounts(string):
    charCounts = {}
    for char in string:
        increaseCharCount(char, charCounts)
    return charCounts    


def getSubstringBounds(string, targetCharCounts):
    substringBounds = [0, float("inf")]
    substringCharCounts = {}
    numUniqueChars = len(targetCharCounts.keys())
    numUniqueCharsDone = 0
    leftIdx = 0
    rightIdx = 0
    # Move the rightIdx to the right in the string until you've counted
    # all of the target characters enough times.
    while rightIdx < len(string):
        rightChar = string[rightIdx]
        if rightChar not in targetCharCounts:
            rightIdx += 1
            continue
        increaseCharCount(rightChar, substringCharCounts)
        if substringCharCounts[rightChar] == targetCharCounts[rightChar]:
            numUniqueCharsDone += 1
        # Move the leftIdx to the right in the string until you no longer 
        # have enough of the target characters in between the leftIdx and 
        # the rightIdx. Update the substringBounds accordingly.
        while numUniqueCharsDone == numUniqueChars and leftIdx <= rightIdx:
            substringBounds = getCloserBounds(leftIdx, rightIdx, substringBounds[0], substringBounds[1])  
            leftChar = string[leftIdx]
            if leftChar not in targetCharCounts:
                leftIdx += 1
                continue
            if substringCharCounts[leftChar] == targetCharCounts[leftChar]:
                numUniqueCharsDone -= 1
            decreaseCharCount(leftChar, substringCharCounts)
            leftIdx += 1
        rightIdx += 1
    return substringBounds


def getCloserBounds(idx1, idx2, idx3, idx4):
    return [idx1, idx2] if idx2 - idx1 < idx4 - idx3 else [idx3, idx4]


def getStringFromBounds(string, bounds):
    start, end = bounds
    if end == float("inf"):
        return ""
    return string[start : end + 1]


def increaseCharCount(char, charCounts):
    if char not in charCounts:
        charCounts[char] = 0
    charCounts[char] += 1
    

def decreaseCharCount(char, charCounts):
    charCounts[char] -= 1
