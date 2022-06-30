""" 

##### Node Depths #####

The distance between a node in a Binary Tree and the tree's root is called the 
node's depth.

Write a function that takes in a Binary Tree and returns the sum of its nodes' 
depths.

Each BinaryTree node has an integer value, a left child node, and a right child 
node. Children nodes can either be BinaryTree nodes themselves or None / null.


##### Sample Input #####
tree =     1
        /      \ 
       2        3   
     /   \    /   \ 
   4      5  6     7
 /   \ 
8     9

##### Sample Output #####
16
// The depth of the node with value 2 is 1.
// The depth of the node with value 3 is 1.
// The depth of the node with value 4 is 2.
// The depth of the node with value 5 is 2.
// Etc..
// Summing all of these depths yields 16.


##### Hints #####

Hint 1
As obvious as it may seem, to solve this question, you'll have to figure out 
how to compute the depth of any given node; once you know how to do that, you 
can compute all of the depths and add them up to obtain the desired output.

Hint 2
To compute the depth of a given node, you need information about its position 
in the tree. Can you pass this information down from the node's parent?

Hint 3
The depth of any node in the tree is equal to the depth of its parent node 
plus 1. By starting at the root node whose depth is 0, you can pass down 
to every node in the tree its respective depth, and you can implement the 
algorithm that does this and that sums up all of the depths either 
recursively or iteratively.

Optimal Space & Time Complexity
Average case: when the tree is balanced O(n) time | O(h) space - where n is 
the number of nodes in the Binary Tree and h is the height of the Binary Tree

"""





##### Solution 1 #####
# Average case: when the tree is balanced
# O(n) time | O(h) space - where n is the number of nodes in
# the Binary Tree and h is the height of the Binary Tree
def nodeDepths(root):
  sumOfDepths = 0
  stack = [{"node": root, "depth": 0}]
  while len(stack) > 0:
    nodeInfo = stack.pop()
    node, depth = nodeInfo["node"], nodeInfo["depth"]
    if node is None:
      continue
    sumOfDepths += depth
    stack.append({"node": node.left, "depth": depth + 1})
    stack.append({"node": node.right, "depth": depth + 1})
  return sumOfDepths  


# This is the class of the input binary tree.
class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None



 

##### Solution 2 #####
# Average case: when the tree is balanced
# O(n) time | O(h) space - where n is the number of nodes in
# the Binary Tree and h is the height of the Binary Tree
def nodeDepths(root, depth=0):
  if root is None:
    return 0
  return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


# This is the class of the input binary tree.
class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
