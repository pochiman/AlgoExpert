""" 

[ Difficulty: Medium ]
[ Category: Binary Trees ]

##### Split Binary Tree #####

Write a function that takes in a Binary Tree with at least one node and checks 
if that Binary Tree can be split into two Binary Trees of equal sum by removing 
a single edge. If this split is possible, return the new sum of each Binary Tree, 
otherwise return 0. Note that you do not need to return the edge that was removed.

The sum of a Binary Tree is the sum of all values in that Binary Tree.

Each BinaryTree node has an integer value, a left child node, and a right child 
node. Children nodes can either be BinaryTree nodes themselves or None / null.


##### Sample Input #####
tree =     1
        /     \
       3       -2
     /   \    /  \
    6    -5  5    2
  /
 2

##### Sample Output #####
  // Remove the edge to the left of the root node,
6 // creating two trees, each with sums of 6


##### Hints #####

Hint 1
Try first calculating the sum of the entire Binary Tree. What information does 
this give you towards solving the problem?

Hint 2
If the sum of the entire Binary Tree is odd, then there is no possible solution, 
because the values are all integers. Otherwise, the solution could be that sum 
divided by two, or potentially there is still no solution. What does the scenario 
look like where the solution is the sum divided by two?

Hint 3
There is a solution if there is a subtree that has a sum equal to the the total 
Binary Tree sum divided by two. In this case, removing the incoming edge to that 
node would have to create another Binary Tree of equal sum.

Hint 4
To prevent recalculating the same subtree sums, try using a post-order traversal 
of the Binary Tree. This allows you to calculate the sums of the smallest subtrees 
first, then send that information back up to the parents to quickly calculate their 
sums.

Optimal Space & Time Complexity
O(n) time | O(h) space - where n is the number of nodes in the tree and h is the 
height of the tree

"""





##### Solution 1 #####
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space - where n is the number of nodes in the tree and
# h is the height of the tree
def splitBinaryTree(tree):
    desiredSubtreeSum = getTreeSum(tree) / 2
    canBeSplit = trySubtrees(tree, desiredSubtreeSum)[1]
    return desiredSubtreeSum if canBeSplit else 0


def trySubtrees(tree, desiredSubtreeSum):
    if tree is None:
        return (0, False)

    leftSum, leftCanBeSplit = trySubtrees(tree.left, desiredSubtreeSum)
    rightSum, rightCanBeSplit = trySubtrees(tree.right, desiredSubtreeSum)

    currentTreeSum = tree.value + leftSum + rightSum
    canBeSplit = leftCanBeSplit or rightCanBeSplit or currentTreeSum == desiredSubtreeSum
    return (currentTreeSum, canBeSplit)


def getTreeSum(tree):
    if tree is None:
        return 0
    return tree.value + getTreeSum(tree.left) + getTreeSum(tree.right)
