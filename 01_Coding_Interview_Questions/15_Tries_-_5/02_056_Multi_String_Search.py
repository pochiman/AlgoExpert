""" 

[ Difficulty: Hard ]
[ Category: Tries ]

##### Multi String Search #####

Write a function that takes in a big string and an array of small strings, all of 
which are smaller in length than the big string. The function should return an array 
of booleans, where each boolean represents whether the small string at that index in 
the array of small strings is contained in the big string.

Note that you can't use language-built-in string-matching methods.


##### Sample Input #1 #####
bigString = "this is a big string"
smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]

##### Sample Output #1 #####
[true, false, true, true, false, true, false]

##### Sample Input #2 #####
bigString = "abcdefghijklmnopqrstuvwxyz"
smallStrings = ["abc", "mnopqr", "wyz", "no", "e", "tuuv"]

##### Sample Output #2 #####
[true, true, false, true, true, false]


##### Hints #####

Hint 1
A simple way to solve this problem is to iterate through all of the small 
strings, checking if each of them is contained in the big string by iterating 
through the big string's characters and comparing them to the given small 
string's characters with a couple of loops. Is this approach efficient from a 
time-complexity point of view?

Hint 2
Try building a suffix-trie-like data structure containing all of the big 
string's suffixes. Then, iterate through all of the small strings and check 
if each of them is contained in the data structure you've created. What are 
the time-complexity ramifications of this approach?

Hint 3
Try building a trie containing all of the small strings. Then, iterate through 
the big string's characters and check if any part of the big string is a string 
contained in the trie you've created. Is this approach better than the one 
described in Hint #2 from a time-complexity point of view?

Optimal Space & Time Complexity
O(ns + bs) time | O(ns) space - where n is the number of small strings, s is 
the length of the longest small string, and b is the length of the big string 

"""





##### Solution 1 #####
# O(bns) time | O(n) space
def multiStringSearch(bigString, smallStrings):
    return [isInBigString(bigString, smallString) for smallString in smallStrings]


def isInBigString(bigString, smallString):
    for i in range(len(bigString)):
        if i + len(smallString) > len(bigString):
            break
        if isInBigStringHelper(bigString, smallString, i):
            return True
    return False


def isInBigStringHelper(bigString, smallString, startIdx):
    leftBigIdx = startIdx
    rightBigIdx = startIdx + len(smallString) - 1
    leftSmallIdx = 0
    rightSmallIdx = len(smallString) - 1
    while leftBigIdx <= rightBigIdx:
        if bigString[leftBigIdx] != smallString[leftSmallIdx] or bigString[rightBigIdx] != smallString[rightSmallIdx]: 
            return False
        leftBigIdx += 1
        rightBigIdx -= 1
        leftSmallIdx += 1
        rightSmallIdx -= 1
    return True





##### Solution 2 #####
# O(b^2 + ns) time | O(b^2 + n) space
def multiStringSearch(bigString, smallStrings):
    modifiedSuffixTrie = ModifiedSuffixTrie(bigString)
    return [modifiedSuffixTrie.contains(string) for string in smallStrings]


class ModifiedSuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.populateModifiedSuffixTrieFrom(string)

    def populateModifiedSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return True





##### Solution 3 #####
# O(ns + bs) time | O(ns) space
def multiStringSearch(bigString, smallStrings):
    trie = Trie()
    for string in smallStrings:
        trie.insert(string)
    containedStrings = {}
    for i in range(len(bigString)):
        findSmallStringsIn(bigString, i, trie, containedStrings)
    return [string in containedStrings for string in smallStrings]


def findSmallStringsIn(string, startIdx, trie, containedStrings):
    currentNode = trie.root
    for i in range(startIdx, len(string)):
        currentChar = string[i]
        if currentChar not in currentNode:
            break
        currentNode = currentNode[currentChar]
        if trie.endSymbol in currentNode:
            containedStrings[currentNode[trie.endSymbol]] = True
        
    
class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def insert(self, string):
        current = self.root
        for i in range(len(string)):
            if string[i] not in current:
                current[string[i]] = {}
            current = current[string[i]]
        current[self.endSymbol] = string
