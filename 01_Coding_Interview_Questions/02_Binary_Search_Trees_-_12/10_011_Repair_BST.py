""" 

[ Difficulty: Hard ]
[ Category: Binary Search Trees ]

##### Repair BST #####

You're given a Binary Search Tree (BST) that has at least 2 nodes and that only 
has nodes with unique values (no duplicate values). Exactly two nodes in the BST 
have had their values swapped, therefore breaking the BST. Write a function that 
returns a repaired version of the tree with all values on the correct nodes.

Your function can mutate the original tree; you do not need to create a new one. 
Moreover, the shape of the returned tree should be exactly the same as that of 
the original input tree.

Each BST node has an integer value, a left child node, and a right child node. A 
node is said to be a valid BST node if and only if it satisfies the BST property: 
its value is strictly greater than the values of every node to its left; its value
is less than or equal to the values of every node to its right; and its children 
nodes are either valid BST nodes themselves or None / null.


##### Sample Input #####
tree =    10
        /     \
       7       20
     /   \    /  \
   3     12  8   22
  /           \
2              14

##### Sample Output #####
          10
        /     \
       7       20
     /   \    /  \
   3      8  12   22
  /           \
2              14


##### Hints #####

Hint 1
If a binary tree is valid, an in order traversal would return all of the nodes 
in order.

Hint 2
By doing an in order traversal, you can find the two nodes that are in the 
incorrect places. Keep track of these nodes and swap their values at the end.

Hint 3
You can keep a global to represent the previous node you saw during the in order 
traversal. That way with each node you can check if it is in the incorrect place.

Optimal Space & Time Complexity
O(n) time | O(h) space - where n is the number of nodes in the tree and h is the 
height of the tree

"""





##### Solution 1 #####
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space - where n is the number of nodes in the
# tree and h is the height of the tree
def repairBst(tree):
    nodeOne = nodeTwo = previousNode = None

    def inOrderTraversal(node):
        nonlocal nodeOne, nodeTwo, previousNode
        if node is None:
            return

        inOrderTraversal(node.left)

        if previousNode is not None and previousNode.value > node.value:
            if nodeOne is None:
                nodeOne = previousNode
            nodeTwo = node

        previousNode = node
        inOrderTraversal(node.right)

    inOrderTraversal(tree)

    nodeOne.value, nodeTwo.value = nodeTwo.value, nodeOne.value
    return tree





##### Solution 2 #####
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space - where n is the number of nodes in the
# tree and h is the height of the tree
def repairBst(tree):
    nodeOne = nodeTwo = previousNode = None

    stack = []
    currentNode = tree
    while currentNode is not None or len(stack) > 0:
        while currentNode is not None:
            stack.append(currentNode)
            currentNode = currentNode.left
        currentNode = stack.pop()

        if previousNode is not None and previousNode.value > currentNode.value:
            if nodeOne is None:
                nodeOne = previousNode
            nodeTwo = currentNode

        previousNode = currentNode
        currentNode = currentNode.right

    nodeOne.value, nodeTwo.value = nodeTwo.value, nodeOne.value
    return tree
