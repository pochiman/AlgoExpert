"""

[ Difficulty: Easy ]
[ Category: Strings ]

##### Common Characters #####

Write a function that takes in a non-empty list of non-empty strings and returns a 
list of characters that are common to all strings in the list, ignoring multiplicity.

Note that the strings are not guaranteed to only contain alphanumeric characters. 
The list you return can be in any order.

##### Sample Input #####
strings = ["abc", "bcd", "cbaccd"]

##### Sample Output #####
["b", "c"] // The characters could be ordered differently.

##### Hints #####

Hint 1
What data structure could be helpful to remember characters we've seen and how 
many strings contained those characters?

Hint 2
We can use a map to keep track of the characters we have seen and how many strings 
we have seen them in. If a character is seen len(strings) times, then it must be in 
every string.

Hint 3
Converting a string to a set can quickly get all of the unique characters from that 
string, which can be helpful since we are ignoring multiplicity in this problem.

Optimal Space & Time Complexity
O(n * m) time | O(m) space - where n is the number of strings, and m is the length 
of the longest string

"""





##### Solution 1 #####
# O(n * m) time | O(c) space - where n is the number of strings, m is the
# length of the longest string, and c is the number of unique characters across
# all strings
def commonCharacters(strings):
    characterCounts = {}
    for string in strings:
        uniqueStringCharacters = set(string)
        for character in uniqueStringCharacters:
            if character not in characterCounts:
                characterCounts[character] = 0
            characterCounts[character] += 1

    finalCharacters = []
    for character, count in characterCounts.items():
        if count == len(strings):
            finalCharacters.append(character)

    return finalCharacters


# Solution 2
# O(n * m) time | O(m) space - where n is the number of strings, and m is the
# length of the longest string
def commonCharacters(strings):
    smallestString = getSmallestString(strings)
    potentialCommonCharacters = set(smallestString)

    for string in strings:
        removeNonexistentCharacters(string, potentialCommonCharacters)

    return list(potentialCommonCharacters)


def getSmallestString(strings):
    smallestString = strings[0]
    for string in strings:
        if len(string) < len(smallestString):
            smallestString = string

    return smallestString


def removeNonexistentCharacters(string, potentialCommonCharacters):
    uniqueStringCharacters = set(string)

    for character in list(potentialCommonCharacters):
        if character not in uniqueStringCharacters:
            potentialCommonCharacters.remove(character)
