""" 

##### Find Closest Value In BST #####

Write a function that takes in a Binary Search Tree (BST) and a target integer value 
and returns the closest value to that target value contained in the BST.

You can assume that there will only be one closest value.

Each BST node has an integer value, a left child node, and a right child node.
A node is said to be a valid BST node if and only if it satisfies the BST property: 
its value is strictly greater than the values of every node to its left; its value 
is less than or equal to the values of every node to its right; and its children 
nodes are either valid BST nodes themselves or None / null.


##### Sample Input #####
tree =   10
       /     \ 
      5      15   
    /   \   /   \ 
  2      5 13    22
 /           \ 
1            14
target = 12 

##### Sample Output #####
13


##### Hints #####

Hint 1
Try traversing the BST node by node, all the while keeping track of the node 
with the value closest to the target value.  Calculating the absolute value of 
the difference between a node's value and the target value should allow you 
to check if that node is closer than the current closest one.

Hint 2
Make use of the BST property to determine what side of any given node has 
values close to the target value and is therefore worth exploring.

Hint 3
What are the advantages and disadvantages of solving this problem 
iteratively as opposed to recursively?

Optimal Space & Time Complexity
Average: O(log(n)) time | O(1) space - where n is the number of nodes in the BST 
Worst: O(n) time | O(1) space - where n is the number of nodes in the BST

"""

""" 

##### Solution 1 #####
# Average: O(log(n)) time | O(log(n)) space 
# Worst: O(n) time | O(n) space
def findClosestValueInBst(tree, target):
  return findClosestValueInBstHelper(tree, target, tree.value)


def findClosestValueInBstHelper(tree, target, closest):
  if tree is None:
    return closest
  if abs(target - closest) > abs(target - tree.value):
    closest = tree.value
  if target < tree.value:
    return findClosestValueInBstHelper(tree.left, target, closest)
  elif target > tree.value:
    return findClosestValueInBstHelper(tree.right, target, closest)
  else:
    return closest


# This is the class of the input tree.
class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

 """

""" 

# Average: O(log(n)) time | O(log(n)) space 
# Worst: O(n) time | O(n) space
def findClosestValueInBst(tree, target):
  return findClosestValueInBstHelper(tree, target, tree.value)


def findClosestValueInBstHelper(tree, target, closest):
  if tree is None:
    return closest
  if abs(target - closest) > abs(target - tree.value):
    closest = tree.value
  if target < tree.value:
    return findClosestValueInBstHelper(tree.left, target, closest)
  elif target > tree.value:
    return findClosestValueInBstHelper(tree.right, target, closest)
  else:
    return closest


# This is the class of the input tree.
class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

 """

""" 

# Average: O(log(n)) time | O(1) space 
# Worst: O(n) time | O(l) space
def findClosestValueInBst(tree, target):
  return findClosestValueInBstHelper(tree, target, tree.value)


def findClosestValueInBstHelper(tree, target, closest):
  currentNode = tree
  while currentNode is not None:
    if abs(target - closest) > abs(target - currentNode.value):
      closest = currentNode.value
    if target < currentNode.value:
      currentNode = currentNode.left
    elif target > currentNode.value:
      currentNode = currentNode.right
    else:
      break
  return closest


# This is the class of the input tree.
class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

 """    