""" 

[ Difficulty: Very Hard ]
[ Category: Binary Trees ]

##### All Kinds Of Node Depths #####

The distance between a node in a Binary Tree and the tree's root is called the 
node's depth.

Write a function that takes in a Binary Tree and returns the sum of all of its 
subtrees' nodes' depths.

Each BinaryTree node has an integer value, a left child node, and a right child 
node. Children nodes can either be BinaryTree nodes themselves or None / null.


##### Sample Input #####
tree =    1
       /     \ 
      2       3
    /   \   /   \  
   4     5 6     7
 /   \ 
8     9

##### Sample Output #####
26
// The sum of the root tree's node depths is 16.
// The sum of the tree rooted at 2's node depths is 6.
// The sum of the tree rooted at 3's node depths is 2.
// The sum of the tree rooted at 4's node depths is 2.
// Summing all of these sums yields 26.


##### Hints #####

Hint 1
You can calculate the sum of a tree's node depths with a simple recursive function. 
Iterate through every node in the tree, call the simple recursive function on each 
node to calculate the sum of the node depths of the tree rooted at the node in 
question, and add up all of the sums to obtain the final sum.

Hint 2
You can solve this question in linear time by coming up with a relation between a 
tree's sum of node depths and the sums of node depths of the trees rooted at its 
left and right child nodes.

Hint 3
The depth of a node relative to a node X is 1 value smaller than its depth relative 
to node X's parent node Y. It follows that, if a subtree rooted at node X has a sum 
of node depths S, you can get the sum of those node depths relative to node Y by 
calculating: S + number-of-nodes-in-subtree-rooted-at-X, since this effectively 
increments all of the node depths relative to node X by 1.

Hint 4
From Hint #3, we can deduce the formula: nodeDepths(node) = nodeDepths(node.left) + 
numberOfNodesInLeftSubtree + nodeDepths(node.right) + numberOfNodesInRightSubtree. 
We can easily count the number of nodes in each subtree with a single pass in the 
input tree, and then we can apply this formula to calculate all of the node depths 
in linear time and finally sum them up.

Optimal Space & Time Complexity
Average case: when the tree is balanced O(n) time | O(h) space - where n is 
the number of nodes in the Binary Tree and h is the height of the Binary Tree

"""





##### Solution 1 #####
# Average case: when the tree is balanced 
# O(nlog(n)) time | O(h) space - where n is the number of nodes in 
# the Binary Tree and h is the height of the Binary Tree
def allKindsOfNodeDepths(root):
    sumOfAllDepths = 0
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        if node is None:
            continue
        sumOfAllDepths += nodeDepths(node)
        stack.append(node.left)  
        stack.append(node.right)
    return sumOfAllDepths    


def nodeDepths(node, depth=0):
    if node is None:
        return 0
    return depth + nodeDepths(node.left, depth + 1) + nodeDepths(node.right, depth + 1)    
    
    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None





##### Solution 2 #####
# Average case: when the tree is balanced 
# O(nlog(n)) time | O(h) space - where n is the number of nodes in 
# the Binary Tree and h is the height of the Binary Tree
def allKindsOfNodeDepths(root):
    if root is None:
        return 0
    return allKindsOfNodeDepths(root.left) + allKindsOfNodeDepths(root.right) + nodeDepths(root)
    

def nodeDepths(node, depth=0):
    if node is None:
        return 0
    return depth + nodeDepths(node.left, depth + 1) + nodeDepths(node.right, depth + 1)    
    
    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None





##### Solution 3 #####
# Average case: when the tree is balanced
# O(n) time | O(n) space - where n is the number of nodes in the Binary Tree
def allKindsOfNodeDepths(root):
    nodeCounts = {}
    addNodeCounts(root, nodeCounts)
    nodeDepths = {}
    addNodeDepths(root, nodeDepths, nodeCounts)
    return sumAllNodeDepths(root, nodeDepths)  


def sumAllNodeDepths(node, nodeDepths):
    if node is None:
        return 0
    return sumAllNodeDepths(node.left, nodeDepths) + sumAllNodeDepths(node.right, nodeDepths) + nodeDepths[node]   
    

def addNodeDepths(node, nodeDepths, nodeCounts):
    nodeDepths[node] = 0
    if node.left is not None:
        addNodeDepths(node.left, nodeDepths, nodeCounts)
        nodeDepths[node] += nodeDepths[node.left] + nodeCounts[node.left]    
    if node.right is not None:
        addNodeDepths(node.right, nodeDepths, nodeCounts)
        nodeDepths[node] += nodeDepths[node.right] + nodeCounts[node.right]
      

def addNodeCounts(node, nodeCounts):
    nodeCounts[node] = 1
    if node.left is not None:
        addNodeCounts(node.left, nodeCounts)
        nodeCounts[node] += nodeCounts[node.left]
    if node.right is not None:
        addNodeCounts(node.right, nodeCounts)  
        nodeCounts[node] += nodeCounts[node.right]


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None





##### Solution 4 #####
# Average case: when the tree is balanced 
# O(n) time | O(h) space - where n is the number of nodes in 
# the Binary Tree and h is the height of the Binary Tree
def allKindsOfNodeDepths(root):
    return getTreeInfo(root).sumOfAllDepths


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0, 0)

    leftTreeInfo = getTreeInfo(tree.left)    
    rightTreeInfo = getTreeInfo(tree.right)

    sumOfLeftDepths = leftTreeInfo.sumOfDepths + leftTreeInfo.numNodesInTree  
    sumOfRightDepths = rightTreeInfo.sumOfDepths + rightTreeInfo.numNodesInTree  

    numNodesInTree = 1 + leftTreeInfo.numNodesInTree + rightTreeInfo.numNodesInTree
    sumOfDepths = sumOfLeftDepths + sumOfRightDepths
    sumOfAllDepths = sumOfDepths + leftTreeInfo.sumOfAllDepths + rightTreeInfo.sumOfAllDepths  

    return TreeInfo(numNodesInTree, sumOfDepths, sumOfAllDepths)
    

class TreeInfo:
    def __init__(self, numNodesInTree, sumOfDepths, sumOfAllDepths):
        self.numNodesInTree = numNodesInTree
        self.sumOfDepths = sumOfDepths
        self.sumOfAllDepths = sumOfAllDepths  

    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None





##### Solution 5 #####
# Average case: when the tree is balanced 
# O(n) time | O(h) space - where n is the number of nodes in 
# the Binary Tree and h is the height of the Binary Tree
def allKindsOfNodeDepths(root, depthSum=0, depth=0):
    if root is None:
        return 0  

    depthSum += depth
    return (
        depthSum
            + allKindsOfNodeDepths(root.left, depthSum, depth + 1)  
            + allKindsOfNodeDepths(root.right, depthSum, depth + 1)  
    )

    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None





##### Solution 6 #####
# Average case: when the tree is balanced 
# O(n) time | O(h) space - where n is the number of nodes in 
# the Binary Tree and h is the height of the Binary Tree
def allKindsOfNodeDepths(root, depth=0):
    if root is None:
        return 0  

    # Formula to calculate 1 + 2 + 3 + ... + depth - 1 + depth      
    depthSum = (depth * (depth + 1)) / 2
    return depthSum + allKindsOfNodeDepths(root.left, depth + 1) + allKindsOfNodeDepths(root.right, depth + 1)  


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
