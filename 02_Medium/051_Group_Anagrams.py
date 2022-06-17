""" 

##### Group Anagrams #####

Write a function that takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't 
matter.  For example, "cinema" and "iceman" are anagrams; similarly, 
"foo" and "ofo" are anagrams.

Your function should return a list of anagram groups in no particular order.


##### Sample Input #####
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

##### Sample Output #####
[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]


##### Hints #####

Hint 1
Try rearranging every input string such that each string's letters are ordered 
in alphabetical order.  What can you do with the resulting strings?

Hint 2
For any two of the resulting strings mentioned in Hint #1 that are equal to 
each other, their original strings (with their letters in normal order) must be 
anagrams.  Realizing this, you could bucket all of these resulting strings 
together, all the while keeping track of their original strings, to find the 
groups of anagrams.

Hint 3
Can you simply store the resulting strings mentioned in Hint #1 in a hash 
table and find the groups of anagrams using this hash table?

Optimal Space & Time Complexity
O(w * n * log(n)) time | O(wn) space - where w is the number of words and n 
is the length of the longest word

"""





##### Solution 1 #####
# O(w * n * log(n) + n * w * log(w)) time | O(wn) space - where w is the number of words and 
# n is the length of the longest word
def groupAnagrams(words):
  if len(words) == 0:
    return []

  sortedWords = ["".join(sorted(w)) for w in words]
  indices = [i for i in range(len(words))]
  indices.sort(key=lambda x: sortedWords[x])

  result = []
  currentAnagramGroup = []
  currentAnagram = sortedWords[indices[0]]
  for index in indices:
    word = words[index]
    sortedWord = sortedWords[index]

    if sortedWord == currentAnagram:
      currentAnagramGroup.append(word)
      continue

    result.append(currentAnagramGroup)
    currentAnagramGroup = [word]
    currentAnagram = sortedWord

  result.append(currentAnagramGroup)

  return result





##### Solution 2 #####
# O(w * n * log(n)) time | O(wn) space - where w is the number of words and 
# n is the length of the longest word
def groupAnagrams(words):
  anagrams = {}
  for word in words:
    sortedWord = "".join(sorted(word))
    if sortedWord in anagrams:
      anagrams[sortedWord].append(word)
    else:    
      anagrams[sortedWord] = [word]
  return list(anagrams.values())
