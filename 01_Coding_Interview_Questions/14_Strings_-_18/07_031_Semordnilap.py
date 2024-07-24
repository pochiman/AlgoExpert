"""

[ Difficulty: Easy ]
[ Category: Strings ]

##### Semordnilap #####

Write a function that takes in a list of unique strings and returns a list of 
semordnilap pairs.

A semordnilap pair is defined as a set of different strings where the reverse of 
one word is the same as the forward version of the other. For example the words 
"diaper" and "repaid" are a semordnilap pair, as are the words "palindromes" and 
"semordnilap".

The order of the returned pairs and the order of the strings within each pair 
does not matter.


##### Sample Input #####
words = ["diaper", "abc", "test", "cba", "repaid"]

##### Sample Output #####
[["diaper", "repaid"], ["abc", "cba"]]

##### Hints #####

Hint 1
It can be helpful to convert the input array into a set, so that you can 
check if a word exists in the list in constant time.

Hint 2
After creating the set of words, try iterating through the original array. 
For each word, can you check if its semordnilap pair is in the word list?

Optimal Space & Time Complexity
O(n * m) time | O(n * m) space - where n is the number of words and m is 
the length of the longest word

"""





##### Solution 1 #####
# O(n * m) time | O(n * m) space - where n is the number of words and
# m is the length of the longest word
def semordnilap(words):
    wordsSet = set(words)
    semordnilapPairs = []

    for word in words:
        reverse = word[::-1]
        if reverse in wordsSet and reverse != word:
            semordnilapPairs.append([word, reverse])
            wordsSet.remove(word)
            wordsSet.remove(reverse)

    return semordnilapPairs