

# O(n^2 + m * w) time | O(n^2 + m * w) space - where n is the length of the
# phone number, m is the number of words, and w is the length of the longest word
def wordsInPhoneNumber(phoneNumber, words):
    phoneNumberSuffixTrie = ModifiedSuffixTrie(phoneNumber)
    return list(filter(lambda word: wordIsInPhoneNumber(phoneNumberSuffixTrie, word), words))


def wordIsInPhoneNumber(phoneNumberSuffixTrie, word):
    digitWord = wordToDigits(word)
    return phoneNumberSuffixTrie.contains(digitWord)


def wordToDigits(word):
    return "".join(map(lambda letter: LETTER_DIGITS[letter], list(word)))


LETTER_DIGITS = {
    "a": "2",
    "b": "2",
    "c": "2",
    "d": "3",
    "e": "3",
    "f": "3",
    "g": "4",
    "h": "4",
    "i": "4",
    "j": "5",
    "k": "5",
    "l": "5",
    "m": "6",
    "n": "6",
    "o": "6",
    "p": "7",
    "q": "7",
    "r": "7",
    "s": "7",
    "t": "8",
    "u": "8",
    "v": "8",
    "w": "9",
    "x": "9",
    "y": "9",
    "z": "9",
}


class ModifiedSuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.populateModifiedSuffixTrieFrom(string)

    def populateModifiedSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, i, string):
        currentTrieNode = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in currentTrieNode:
                currentTrieNode[letter] = {}
            currentTrieNode = currentTrieNode[letter]

    def contains(self, string):
        currentTrieNode = self.root
        for letter in string:
            if letter not in currentTrieNode:
                return False
            currentTrieNode = currentTrieNode[letter]
        return True
