""" 

##### Same BSTs #####

An array of integers is said to represent the Binary Search Tree (BST) obtained by 
inserting each integer in the array, from left to right, into the BST.

Write a function that takes in two arrays of integers and determines whether these 
arrays represent the same BST.  Note that you're not allowed to construct any BSTs 
in your code.

A BST is a Binary Tree that consists only of BST nodes.  A node is said to be a valid 
BST node if and only if it satisfies the BST property: its value is strictly greater 
than the values of every node to its left; its value is less than or equal to the 
values of every node to its right; and its children nodes are either valid BST nodes 
themselves or None / null.


##### Sample Input #####
arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]

##### Sample Output #####
true // both arrays represent the BST below
          10
       /      \ 
      8       15
    /        /   \ 
   5       12    94
 /        /     /
2        11    81


##### Hints #####

Hint 1
You can immediately conclude that the input arrays don't represent the 
same BST if their values aren't equal to each other, since their first 
values represent the root of the BST.  Similarly, you can conclude this 
if their lengths are different.  If their first values are equal to each 
other and their lengths are the same, what should your next step be?

Hint 2
Given an array of integers, all of the values in the array that are smaller 
than the the first value in the array are located in the left subtree of the 
BST that the array represents, and all of the values in the array that are 
greater than or equal to the first value in the array are located in the right 
subtree of the BST that the array represents.  Use this fact and Hint #1 to 
recursively determine whether all subtrees in the BSTs represented by the 
arrays are equal to each other.

Hint 3
Write a recursive function that takes in two arrays of integers.  If the first 
values of the arrays aren't equal to each other or if the arrays don't have the 
same length, the arrays don't represent the same BST.  If the first values and 
lengths are equal to each other, respectively, perform the following actions 
on both arrays: gather all integers that are smaller than the first integer; 
these form a new array that represents the left subtree of the relevant BST; 
gather all integers that are greater than or equal to the first integer, these 
form a new array that represents the right subtree of the relevant BST.  Call 
the recursive function twice: once with the two left-subtree arrays and once 
with the two right-subtree arrays.

Hint 4
Do you actually need to create all of the auxiliary array mentioned in Hint #3?

Optimal Space & Time Complexity
O(n^2) time | O(d) space - where n is the number of nodes in each array, 
respectively, and d is the depth of the BST that they represent

"""





##### Solution 1 #####
# O(n^2) time | O(n^2) space - where n is the number of 
# nodes in each array, respectively 
def sameBsts(arrayOne, arrayTwo):
  if len(arrayOne) != len(arrayTwo):
    return False

  if len(arrayOne) == 0 and len(arrayTwo) == 0:
    return True

  if arrayOne[0] != arrayTwo[0]:
    return False

  leftOne = getSmaller(arrayOne)
  leftTwo = getSmaller(arrayTwo)  
  rightOne = getBiggerOrEqual(arrayOne)
  rightTwo = getBiggerOrEqual(arrayTwo)

  return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)


def getSmaller(array):
  smaller = []
  for i in range(1, len(array)):
    if array[i] < array[0]:
      smaller.append(array[i])
  return smaller


def getBiggerOrEqual(array):
  biggerOrEqual = []
  for i in range(1, len(array)):
    if array[i] >= array[0]:
      biggerOrEqual.append(array[i])
  return biggerOrEqual





##### Solution 2 #####
# O(n^2) time | O(d) space - where n is the number of 
# nodes in each array, respectively, and d is the depth 
# of the BST that they represent
def sameBsts(arrayOne, arrayTwo):
  return areSameBsts(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))


def areSameBsts(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxVal):
  if rootIdxOne == -1 or rootIdxTwo == -1:
    return rootIdxOne == rootIdxTwo

  if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
    return False

  leftRootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIdxOne, minVal)
  leftRootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIdxTwo, minVal)
  rightRootIdxOne = getIdxOfFirstBiggerOrEqual(arrayOne, rootIdxOne, maxVal)
  rightRootIdxTwo = getIdxOfFirstBiggerOrEqual(arrayTwo, rootIdxTwo, maxVal)

  currentValue = arrayOne[rootIdxOne]
  leftAreSame = areSameBsts(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, currentValue)
  rightAreSame = areSameBsts(arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentValue, maxVal)

  return leftAreSame and rightAreSame


def getIdxOfFirstSmaller(array, startingIdx, minVal):
  # Find the index of the first smaller value after the startingIdx.
  # Make sure that this value is greater than or equal to the minVal, 
  # which is the value of the previous parent node in the BST.  If it 
  # isn't, then that value is located in the left subtree of the 
  # previous parent node.
  for i in range(startingIdx + 1, len(array)):
    if array[i] < array[startingIdx] and array[i] >= minVal:
      return i
  return -1


def getIdxOfFirstBiggerOrEqual(array, startingIdx, maxVal):
  # Find the index of the first bigger/equal value after the startingIdx.
  # Make sure that this value is smaller than maxVal, which is the value 
  # of the previous parent node in the BST.  If it isn't, then that value 
  # is located in the right subtree of the previous parent node.
  for i in range(startingIdx + 1, len(array)):
    if array[i] >= array[startingIdx] and array[i] < maxVal:
      return i
  return -1
