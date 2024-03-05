""" 

[ Difficulty: Very Hard ]
[ Category: Binary Trees ]

##### Flatten Binary Tree #####

Write a function that takes in a Binary Tree, flattens it, and returns its leftmost 
node.

A flattened Binary Tree is a structure that's nearly identical to a Doubly Linked List 
(except that nodes have left and right pointers instead of prev and next pointers), 
where nodes follow the original tree's left-to-right order.

Note that if the input Binary Tree happens to be a valid Binary Search Tree, the 
nodes in the flattened tree will be sorted.

The flattening should be done in place, meaning that the original data structure 
should be mutated (no new structure should be created).

Each BinaryTree node has an integer value, a left child node, and right child node. 
Children nodes can either be BinaryTree nodes themselves or None / null.


##### Sample Input #####
tree =    1
       /     \ 
      2       3
    /   \   /  
   4     5 6     
        / \ 
       7   8    

##### Sample Output #####
4 <-> 2 <-> 7 <-> 5 <-> 8 <-> 1 <-> 6 <-> 3 // the leftmost node with value 4


##### Hints #####

Hint 1
You can solve this problem pretty easily by traversing the tree using the 
in-order tree-traversal technique, gathering all of the nodes in an array, 
and then iterating through them from left to right and connecting them 
accordingly. Can you solve this problem without storing an entire array of 
the tree's nodes?

Hint 2
Try to figure out what the relation between two adjacent nodes in the in-
order-traversal order is, as far as positioning in the tree is concerned.

Hint 3
At any given node in the in-order-traversal order, the node immediately to 
its left is the rightmost node of its left subtree, and the node immediately 
the its right is the leftmost node of its right subtree.

Hint 4
Write a function that recursively gets the leftmost and rightmost nodes of 
a given node's left subtree and right subtree and that connects the left 
subtree's rightmost node to the given node and the right subtree's leftmost 
node to the given node.

Optimal Space & Time Complexity
O(n) time | O(d) space - where n is the number of nodes in the Binary Tree 
and d is the depth (height) of the Binary Tree

"""





##### Solution 1 #####
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space - where n is the number of nodes in the Binary Tree 
def flattenBinaryTree(root):
    inOrderNodes = getNodesInOrder(root, [])
    for i in range(0, len(inOrderNodes) - 1):
        leftNode = inOrderNodes[i]
        rightNode = inOrderNodes[i + 1]
        leftNode.right = rightNode
        rightNode.left = leftNode
    return inOrderNodes[0]


def getNodesInOrder(tree, array):
    if tree is not None:
        getNodesInOrder(tree.left, array)
        array.append(tree)
        getNodesInOrder(tree.right, array)
    return array





##### Solution 2 #####
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(d) space - where n is the number of nodes in the Binary Tree 
# and d is the depth (height) of the Binary Tree
def flattenBinaryTree(root):
    leftMost, _ = flattenTree(root)
    return leftMost  


def flattenTree(node):
    if node.left is None:
        leftMost = node
    else:
        leftSubtreeLeftMost, leftSubtreeRightMost = flattenTree(node.left)
        connectNodes(leftSubtreeRightMost, node)
        leftMost = leftSubtreeLeftMost

    if node.right is None:
        rightMost = node
    else:
        rightSubtreeLeftMost, rightSubtreeRightMost = flattenTree(node.right)  
        connectNodes(node, rightSubtreeLeftMost)
        rightMost = rightSubtreeRightMost

    return [leftMost, rightMost]    


def connectNodes(left, right):
    left.right = right
    right.left = left
