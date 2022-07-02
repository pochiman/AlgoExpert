""" 

##### Palindrome Check #####

Write a function that takes in a non-empty string and that returns a boolean 
representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward and backward. 
Note that single-character strings are palindromes.


##### Sample Input #####
string = "abcdcba"

##### Sample Output #####
true // it's written the same forward and backward


##### Hints #####

Hint 1
Start by building the input string in reverse order and comparing this newly 
built string to the input string. Can you do this without using string 
concatenations?

Hint 2
Can you optimize your algorithm by using recursions? What are the implications 
of recursion on an algorithm's space-time complexity analysis?

Hint 3
Go back to an iterative solution and try using pointers to solve this problem: 
start with a pointer at the first index of the string and a pointer at the 
final index of the string. What can you do from there?

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the length of the input string

"""





##### Solution 1 #####
# O(n^2) time | O(n) space
def isPalindrome(string):
  reversedString = ""
  for i in reversed(range(len(string))):
    reversedString += string[i]
  return string == reversedString



 

##### Solution 2 #####
# O(n) time | O(n) space
def isPalindrome(string):
  reversedChars = []
  for i in reversed(range(len(string))):
    reversedChars.append(string[i])
  return string == "".join(reversedChars)



 

##### Solution 3 #####
# O(n) time | O(n) space
def isPalindrome(string, i=0):
  j = len(string) - 1 - i
  return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)



 

##### Solution 4 #####
# O(n) time | O(1) space
def isPalindrome(string):
  leftIdx = 0
  rightIdx = len(string) - 1
  while leftIdx < rightIdx:
    if string[leftIdx] != string[rightIdx]:
      return False
    leftIdx += 1
    rightIdx -= 1
  return True
