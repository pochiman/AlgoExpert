""" 

##### Validate Subsequence #####

Given two non-empty arrays of integers, write a function that determines whether 
the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in 
the array but that are in the same order as they appear in the array. For instance, 
the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the 
numbers [2, 4]. Note that a single number in an array and the array itself are both 
valid subsequences of the array.


##### Sample Input #####
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

##### Sample Output #####
true


##### Hints #####

Hint 1
You can solve this question by iterating through the main input array once.

Hint 2
Iterate through the main array, and look for the first integer in the 
potential subsequence. If you find that integer, keep on iterating through 
the main array, but now look for the second integer in the potential 
subsequence. Continue this process until you either find every integer 
in the potential subsequence or you reach the end of the main array.

Hint 3
To actually implement what Hint #2 describes, you'll have to declare a 
variable holding your position in the potential subsequence. At first, this 
position will be the 0th index in the sequence, as you find the sequence's 
integers in the main array, you'll increment the position variable until 
you reach the end of the sequence.

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the length of the array

"""

 



##### Solution 1 #####
# O(n) time | O(1) space - where n is the length of the array
def isValidSubsequence(array, sequence):
  arrIdx = 0
  seqIdx = 0
  while arrIdx < len(array) and seqIdx < len(sequence):
    if array[arrIdx] == sequence[seqIdx]:
      seqIdx += 1
    arrIdx += 1
  return seqIdx == len(sequence)



 

##### Solution 2 #####
# O(n) time | O(1) space - where n is the length of the array
def isValidSubsequence(array, sequence):
  seqIdx = 0
  for value in array:
    if seqIdx == len(sequence):
      break
    if sequence[seqIdx] == value:
      seqIdx += 1
  return seqIdx == len(sequence)    
