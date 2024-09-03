

# Average case: when there aren't too many strings with
# identical prefixes that are found in another string
# O(n * m) time | O(n * m) space - where n is the number
# of strings and m is the length of the longest string
# --------
# See the Notes section in the Explanation tab for more info.
def specialStrings(strings):
    trie = Trie()
    for string in strings:
        trie.insert(string)
    return list(filter(lambda string: isSpecial(string, trie.root, 0, 0, trie), strings))


def isSpecial(string, trieNode, idx, count, trie):
    char = string[idx]
    if char not in trieNode:
        return False

    atEndOfString = idx == len(string) - 1
    if atEndOfString:
        return trie.endSymbol in trieNode[char] and count + 1 >= 2

    if trie.endSymbol in trieNode[char]:
        restIsSpecial = isSpecial(string, trie.root, idx + 1, count + 1, trie)
        if restIsSpecial:
            return True

    return isSpecial(string, trieNode[char], idx + 1, count, trie)


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def insert(self, string):
        currentTrieNode = self.root
        for i in range(len(string)):
            if string[i] not in currentTrieNode:
                currentTrieNode[string[i]] = {}
            currentTrieNode = currentTrieNode[string[i]]
        currentTrieNode[self.endSymbol] = string
