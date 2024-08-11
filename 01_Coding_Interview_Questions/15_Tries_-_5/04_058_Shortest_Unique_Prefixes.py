"""

[ Difficulty: Hard ]
[ Category: Tries ]

##### Shortest Unique Prefixes #####

You're given an array of unique strings. Write a function that returns an array 
containing the shortest unique prefix for each string.

For example, given the strings ["algoexpert", "algorithm"], the shortest prefixes 
that uniquely identify each string are ["algoe", "algor"].

If a string strA is entirely contained in another string strB, then there is no 
completely unique prefix for strA, and thus its shortest unique prefix should be 
its entire self. For example, given the strings ["food", "foodie"], the shortest 
prefixes to uniquely identify each string would be ["food", "foodi"]. In this 
example, "food"'s shortest unique prefix must be "food" (the entire string), 
since it's entirely contained in "foodie". It follows that "foodie" can't have 
just "food" as its shortest unique prefix.

Your function should return the prefixes in the corresponding order of the input 
strings (i.e., the index of each prefix should be the same as the index of its 
corresponding string).


##### Sample Input #1 #####
strings = [
  "algoexpert",
  "algorithm",
]

##### Sample Output #1 #####
[
  "algoe",
  "algor"
]

##### Sample Input #2 #####
strings = [
  "hello",
  "world",
  "he",
  "foo",
  "worldly",
  "food",
  "algoexpert"
]

##### Sample Output #2 #####
[
  "hel",
  "world",
  "he",
  "foo",
  "worldl",
  "food",
  "a"
]

##### Sample Input #3 #####
strings = [
  "foo",
  "food",
  "foods",
  "foodie"
]

##### Sample Output #3 #####
[
  "foo",
  "food",
  "foods",
  "foodi"
]


##### Hints #####

Hint 1
This problem requires organizing the strings based on their starting characters. 
Is there a data structure that can help with this?

Hint 2
Try first inserting all of the strings into a trie, then use that trie to find 
the shortest unique prefix for each.

Hint 3
In the trie, any node that we only ever see once is unique to a word. Try keeping 
track of how many visits are made to each node. For each string, the path to the 
shortest unique prefix ends when a node with only 1 visit is found.

Optimal Space & Time Complexity
O(n * m) time | O(n * m) space - where n is the length of strings, and m is the 
length of the longest string

"""





##### Solution 1 #####
# O(n * m) time | O(n * m) space - where n is the length of strings, and m
# is the length of the longest string
def shortestUniquePrefixes(strings):
    trie = Trie()
    for string in strings:
        trie.insert(string)

    prefixes = []
    for string in strings:
        uniquePrefix = findUniquePrefix(string, trie)
        prefixes.append(uniquePrefix)

    return prefixes


def findUniquePrefix(string, trie):
    currentStringIdx = 0
    currentTrieNode = trie.root

    while currentStringIdx < len(string) - 1:
        currentStringChar = string[currentStringIdx]
        currentTrieNode = currentTrieNode[currentStringChar]
        if currentTrieNode["count"] == 1:
            break
        currentStringIdx += 1

    return string[0 : currentStringIdx + 1]


class Trie:
    def __init__(self):
        self.root = {"count": 0}

    def insert(self, string):
        currentTrieNode = self.root
        for i in range(len(string)):
            if string[i] not in currentTrieNode:
                currentTrieNode[string[i]] = {"count": 0}
            currentTrieNode = currentTrieNode[string[i]]
            currentTrieNode["count"] += 1
