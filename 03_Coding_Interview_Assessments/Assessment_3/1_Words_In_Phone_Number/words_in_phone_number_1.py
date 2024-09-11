

# O(m * w + n * 3^n) time | O(m * w + n) space - where n is the length of the
# phone number, m is the number of words, and w is the length of the longest word
def wordsInPhoneNumber(phoneNumber, words):
    wordTrie = getWordTrie(words)
    finalWords = {}
    for i in range(len(phoneNumber)):
        exploreTrie(phoneNumber, i, wordTrie.root, finalWords)
    return list(finalWords.keys())


def getWordTrie(words):
    wordTrie = Trie()
    for word in words:
        wordTrie.insert(word)
    return wordTrie


def exploreTrie(phoneNumber, digitIdx, trieNode, finalWords):
    if "*" in trieNode:
        word = trieNode["*"]
        finalWords[word] = True

    if digitIdx == len(phoneNumber):
        return

    currentDigit = phoneNumber[digitIdx]
    possibleLetters = DIGIT_LETTERS[currentDigit]
    for letter in possibleLetters:
        if letter not in trieNode:
            continue
        exploreTrie(phoneNumber, digitIdx + 1, trieNode[letter], finalWords)


DIGIT_LETTERS = {
    "0": [],
    "1": [],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def insert(self, word):
        currentTrieNode = self.root
        for letter in word:
            if letter not in currentTrieNode:
                currentTrieNode[letter] = {}
            currentTrieNode = currentTrieNode[letter]
        currentTrieNode[self.endSymbol] = word
