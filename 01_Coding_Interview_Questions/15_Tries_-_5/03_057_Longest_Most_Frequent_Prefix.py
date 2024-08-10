"""

[ Difficulty: Hard ]
[ Category: Tries ]

##### Longest Most Frequent Prefix #####

Write a function that takes in an array of unique strings and returns the prefix 
that appears most frequently throughout the strings. If there are two or more 
such prefixes, your function should return the longest one. If there are no such 
prefixes, your function should return the longest string. You can assume that 
there will only ever be one longest prefix or string.

For example, given the strings ["algoexpert", "algorithm", "foo", "food"], the 
most frequent prefix is either "algo" or "foo", since both appear in two strings. 
However, "algo" is longer than "foo", so "algo" is the desired answer.


##### Sample Input #1 #####
strings = [
  "algoexpert",
  "algorithm",
  "frontendexpert",
  "mlexpert"
]

##### Sample Output #1 #####
"algo"

##### Sample Input #2 #####
strings = [
  "hello",
  "world",
  "fossil",
  "worldly",
  "food",
  "forrest",
  "helium",
  "algoexpert",
  "algorithm"
]

##### Sample Output #2 #####
"fo"


##### Hints #####

Hint 1
This problem requires finding shared prefixes of various strings. Is there a 
data structure that can help with this?

Hint 2
Try first inserting all of the strings into a trie, and with that trie, keep 
track of the frequency of every prefix you see. The most common prefix will 
be the solution.

Hint 3
To avoid iterating through the trie after creating it, try calculating what 
the current solution to the problem is as you insert into the trie.

Optimal Space & Time Complexity
O(n * m) time | O(n * m) space - where n is the length of strings, and m is 
the length of the longest string

"""





##### Solution 1 #####
# O(n * m) time | O(n * m) space - where n is the length of strings, and m
# is the length of the longest string
def longestMostFrequentPrefix(strings):
    trie = Trie()
    for string in strings:
        trie.insert(string)
    return trie.maxPrefixFullString[0 : trie.maxPrefixLength]


class Trie:
    def __init__(self):
        self.root = {"count": 0}
        self.maxPrefixCount = 0
        self.maxPrefixLength = 0
        self.maxPrefixFullString = ""

    def insert(self, string):
        currentTrieNode = self.root
        for i in range(len(string)):
            if string[i] not in currentTrieNode:
                currentTrieNode[string[i]] = {"count": 0}
            currentTrieNode = currentTrieNode[string[i]]
            currentTrieNode["count"] += 1

            if currentTrieNode["count"] > self.maxPrefixCount:
                self.maxPrefixCount = currentTrieNode["count"]
                self.maxPrefixLength = i + 1
                self.maxPrefixFullString = string
            elif currentTrieNode["count"] == self.maxPrefixCount and i + 1 > self.maxPrefixLength:
                self.maxPrefixLength = i + 1
                self.maxPrefixFullString = string
