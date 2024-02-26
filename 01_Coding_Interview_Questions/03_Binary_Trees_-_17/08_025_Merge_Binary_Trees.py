""" 

[ Difficulty: Medium ]
[ Category: Binary Trees ]

##### Merge Binary Trees #####

Write a function that takes in two Binary Trees, merges them, and returns the 
resulting tree. If two nodes overlap during the merge, the value of the merged 
node should be the sum of the overlapping nodes' values.

Note that your solution can either mutate the input trees or return a new tree.

Each BinaryTree node has an integer value, a left child node, and a right child 
node. Children nodes can either be BinaryTree nodes themselves or None / null.


##### Sample Input #####
tree1 =   1
        /   \
       3     2
     /   \
    7     4

tree2 =   1
        /   \
       5     9
     /      / \
    2      7   6

##### Sample Output #####
output =  2
        /   \
      8      11
    /  \    /  \
  9     4  7    6


##### Hints #####

Hint 1
If the function takes two tree nodes as parameters then what should be returned 
if either of the two nodes is null? Remember, if two nodes overlap during the 
merger then sum the values, otherwise use the existing node. How can you sum 
the tree node values when they overlap?

Hint 2
If two tree nodes overlap then sum the values into either one of the nodes. 
This node will be returned from the function. Recursively call the function 
twice passing in both trees' left nodes as well as their right nodes.

Hint 3
The iterative approach to this problem uses a stack in replacement of the recusions 
stack space. What would you push onto the stack in order to traverse and merge the 
binary trees?

Hint 4
You can either use a single stack and push associated pairs of nodes on the stack,
or you can maintain a stack for each tree.

Optimal Space & Time Complexity
O(n) time | O(h) space - where n is the number of nodes in the smaller of the 
two trees and h is the height of the shorter tree.

"""





##### Solution 1 #####
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space - where n is the number of nodes in the smaller of the
# two trees and h is the height of the shorter tree.
def mergeBinaryTrees(tree1, tree2):
    if tree1 is None:
        return tree2
    if tree2 is None:
        return tree1

    tree1.value += tree2.value
    tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
    tree1.right = mergeBinaryTrees(tree1.right, tree2.right)
    return tree1





##### Solution 2 #####
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space - where n is the number of nodes in the smaller of the
# two trees and h is the height of the shorter tree.
def mergeBinaryTrees(tree1, tree2):
    if tree1 is None:
        return tree2

    tree1Stack = [tree1]
    tree2Stack = [tree2]

    while len(tree1Stack) > 0:
        tree1Node = tree1Stack.pop()
        tree2Node = tree2Stack.pop()

        if tree2Node is None:
            continue

        tree1Node.value += tree2Node.value

        if tree1Node.left is None:
            tree1Node.left = tree2Node.left
        else:
            tree1Stack.append(tree1Node.left)
            tree2Stack.append(tree2Node.left)

        if tree1Node.right is None:
            tree1Node.right = tree2Node.right
        else:
            tree1Stack.append(tree1Node.right)
            tree2Stack.append(tree2Node.right)

    return tree1
