"""

[ Difficulty: Very Hard ]
[ Category: Tries ]

##### Strings Made Up Of Strings #####

Write a function that takes in a non-empty array of unique strings strings as 
well as another non-empty array of unique strings substrings. This function 
should return an array of all of the strings in strings that can be formed by 
concatenating one or more of the strings in substrings.

Note that:

    • The strings in substrings won't necessarily always be smaller than those 
      in strings. For example, the string "ab" could be contained in substrings 
      with the string "a" contained in strings.

    • A substring can be used multiple times to make up a string. For example, 
      the substring "foo" can be used twice to make up the string "foofoo".

    • A substring must be entirely contained in a string in order to be part of it.

    • If a string is exactly equal to a substring, that string should be included 
      in the output array.

    • The order of the strings in the output array doesn't matter. 


##### Sample Input #1 #####
strings = [
  "bar",
  "are",
  "foo",
  "ba",
  "b",
  "barely"
]
substrings = [
  "b",
  "a",
  "r",
  "ba",
  "ar",
  "bar"
]

##### Sample Output #1 #####
["bar", "ba", "b"]

##### Sample Input #2 #####
strings = [
  "barbar",
  "algoexpert",
  "frontendexpert"
]
substrings = [
  "algo",
  "bar",
  "expert",
  "end",
  "front"
]

##### Sample Output #2 #####
["barbar", "algoexpert", "frontendexpert"]


##### Hints #####

Hint 1
Try breaking this problem down into small chunks. For every string in strings, 
we want to first figure out if any of the substrings are the same as the beginning 
of the current string. Then the process should repeat for the remaining characters 
of the current string until the entire string has been found.

Hint 2
Since we need to be able to quickly find if the beginning of a string is present in
the substrings, it will be helpful to create a Trie to hold all of the substrings.

Hint 3
You'll likely end up doing a lot of repetitive work. For this reason, adding a 
memoization dictionary to contain all of the previous found substrings can help 
improve the time complexity.

Hint 4
Finding a substring of a string is usually an O(n) operation. To avoid this, try 
simply passing start and end indices to helper functions, rather than actually 
creating the substrings.

Optimal Space & Time Complexity
O(s2 * m + s1 * n^2) time | O(s2 * m + s1 * n) space - where s2 is the number of 
substrings, m is the length of the longest substring, s1 is the number of strings, 
and n is the length of the longest string

"""





##### Solution 1 #####
# O(s2 * m + s1 * n^2) time | O(s2 * m + s1 * n) space - where s2 is the number
# of substrings, m is the length of the longest substring, s1 is the
# number of strings, and n is the length of the longest string
def stringsMadeUpOfStrings(strings, substrings):
    trie = Trie()
    for substring in substrings:
        trie.insert(substring)

    solutions = []
    for string in strings:
        if isMadeUpOfStrings(string, 0, trie, {}):
            solutions.append(string)

    return solutions


def isMadeUpOfStrings(string, startIdx, trie, memo):
    if startIdx == len(string):
        return True
    if startIdx in memo:
        return memo[startIdx]

    currentTrieNode = trie.root
    for currentCharacterIdx in range(startIdx, len(string)):
        currentCharacter = string[currentCharacterIdx]
        if currentCharacter not in currentTrieNode:
            break

        currentTrieNode = currentTrieNode[currentCharacter]
        if currentTrieNode["isEndOfString"] and isMadeUpOfStrings(
            string, currentCharacterIdx + 1, trie, memo
        ):
            memo[startIdx] = True
            return True

    memo[startIdx] = False
    return False


class Trie:
    def __init__(self):
        self.root = {"isEndOfString": False}

    def insert(self, string):
        currentTrieNode = self.root
        for i in range(len(string)):
            if string[i] not in currentTrieNode:
                currentTrieNode[string[i]] = {"isEndOfString": False}
            currentTrieNode = currentTrieNode[string[i]]
        currentTrieNode["isEndOfString"] = True
