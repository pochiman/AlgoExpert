""" 

##### Longest Substring Without Duplication #####

Write a function that takes in a string and returns its longest substring without 
duplicate characters.

You can assume that there will only be one longest substring without duplication.


##### Sample Input #####
string = "clementisacap"

##### Sample Output #####
"mentisac"


##### Hints #####

Hint 1
Try traversing the input string and storing the last position at which you see 
each character in a hash table. How can this help you solve the given problem?

Hint 2
As you traverse the input string, keep track of a starting index variable. This 
variable, as its name suggests, should represent the most recent index from 
which you could start a substring with no duplicate characters, ending at your 
current index. Use the hash table mentioned in Hint #1 to update this variable 
correctly, and update the longest substring as you go.

Optimal Space & Time Complexity
O(n) time | O(min(n, a)) space - where n is the length of the input string and a 
is the length of the character alphabet represented in the input string

"""





##### Solution 1 #####
# O(n) time | O(min(n, a)) space
def longestSubstringWithoutDuplication(string):
  lastSeen = {}
  longest = [0, 1]
  startIdx = 0
  for i, char in enumerate(string):
    if char in lastSeen:
      startIdx = max(startIdx, lastSeen[char] + 1)
    if longest[1] - longest[0] < i + 1 - startIdx:
      longest = [startIdx, i + 1]
    lastSeen[char] = i
  return string[longest[0] : longest[1]]
