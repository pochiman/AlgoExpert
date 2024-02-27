""" 

[ Difficulty: Medium ]
[ Category: Binary Trees ]

##### Symmetrical Tree #####

Write a function that takes in a Binary Tree and returns if that tree is symmetrical. 
A tree is symmetrical if the left and right subtrees are mirror images of each other.

Each BinaryTree node has an integer value, a left child node, and a right child node. 
Children nodes can either be BinaryTree nodes themselves or None / null.


##### Sample Input #####
tree =    1
       /     \
      2       2
    /   \   /   \
   3     4 4     3
 /   \          /  \
5     6        6    5

##### Sample Output #####
True


##### Hints #####

Hint 1
It's important to first think about what it means for a binary tree to be symmetrical. 
The left and right subtrees do not need to be the same, but rather they need to be 
mirror images of each other (i.e. the same if one is inverted).

Hint 2
It can be helpful to think about this problem one step at a time. Looking at just the 
first node, how can you ensure its children are symmetrical? Then looking at those 
children, how can you make sure they are symmetrical of each other?

Hint 3
This problem can be solved either recursively or iteratively. Either way, try traversing 
through the tree, uses a mirrored traversal on one side, and check that the values of 
each node are the same.

Optimal Space & Time Complexity
O(n) time | O(h) space - where n is the number of nodes in the tree and h is the 
height of the tree.

"""





##### Solution 1 #####
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space - where n is the number of nodes in the tree
# and h is the height of the tree.
def symmetricalTree(tree):
    stackLeft = [tree.left]
    stackRight = [tree.right]

    while len(stackLeft) > 0:
        left = stackLeft.pop()
        right = stackRight.pop()

        if left is None and right is None:
            continue

        if left is None or right is None or left.value != right.value:
            return False

        stackLeft.append(left.left)
        stackLeft.append(left.right)
        stackRight.append(right.right)
        stackRight.append(right.left)

    return True





##### Solution 2 #####
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space - where n is the number of nodes in the tree
# and h is the height of the tree.
def symmetricalTree(tree):
    return treesAreMirrored(tree.left, tree.right)


def treesAreMirrored(left, right):
    if left is not None and right is not None and left.value == right.value:
        return treesAreMirrored(left.left, right.right) and treesAreMirrored(left.right, right.left)

    return left == right
