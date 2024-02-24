""" 

[ Difficulty: Medium ]
[ Category: Binary Trees ]

##### Binary Tree Diameter #####

Write a function that takes in a Binary Tree and returns its diameter. The diameter 
of a binary tree is defined as the length of its longest path, even if that path 
doesn't pass through the root of the tree.

A path is a collection of connected nodes in a tree, where no node is connected to 
more than two other nodes. The length of a path is the number of edges between 
the path's first node and its last node.

Each BinaryTree node has an integer value, a left child node, and a right child 
node. Children nodes can either be BinaryTree nodes themselves or None / null.


##### Sample Input #####
tree =    1
        /    \ 
       3      2   
     /   \     
    7     4
   /       \ 
  8         5
 /           \ 
9             6

##### Sample Output #####
6 // 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6
// There are 6 edges between the 
// first node and the last node 
// of this tree's longest path.


##### Hints #####

Hint 1
How can you use the height of a binary tree and the heights of its subtrees 
to calculate its diameter?

Hint 2
The length of the longest path that goes through the root of a binary tree is 
the sum of the heights of its left and right subtrees (left subtree height + 
right subtree height). The diameter of a binary tree can be calculated by 
taking the maximum of: 1) the maximum subtree diameter (max(left subtree 
diameter, right subtree diameter)); and 2) the length of the longest path 
that goes through the root (left subtree height + right subtree height).

Hint 3
Implement a variation of depth-first search that recursively keeps track of 
both the diameter and the height of each subtree in the input binary tree. 
Follow Hint #2 to continuously compute these diameters.

Optimal Space & Time Complexity
Average case: when the tree is balanced O(n) time | O(h) space - where n is 
the number of nodes in the Binary Tree and h is the height of the Binary Tree

"""





##### Solution 1 #####
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Average case: when the tree is balanced 
# O(n) time | O(h) space - where n is the number of nodes in 
# the Binary Tree and h is the height of the Binary Tree
def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currentDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
    currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

    return TreeInfo(currentDiameter, currentHeight)


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height
