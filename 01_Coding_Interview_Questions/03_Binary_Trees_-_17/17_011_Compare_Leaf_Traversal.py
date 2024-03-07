""" 

[ Difficulty: Very Hard ]
[ Category: Binary Trees ]

##### Compare Leaf Traversal #####

Write a function that takes in the root nodes of two Binary Trees and returns a 
boolean representing whether their leaf traversals are the same.

The leaf traversal of a Binary Tree traverses only its leaf nodes from left to right. 
A leaf node is any node that has no left or right children.

For example, the leaf traversal of the following Binary Tree is 1, 3, 2.

   4
 /   \ 
1     5
    /   \ 
   3     2

Each BinaryTree node has an integer value, a left child node, and a right child node. 
Children nodes can either be BinaryTree nodes themselves or None / null.


##### Sample Input #####
tree1 =  1
       /   \ 
      2     3
    /   \     \  
   4     5     6
       /   \ 
      7     8
tree2 =  1
       /   \ 
      2     3
    /   \     \  
   4     7     5
             /   \ 
            8     6

##### Sample Output #####
true 


##### Hints #####

Hint 1
To traverse the leaf nodes of a tree from left to right, you'll need to use a 
pre-order traversal.

Hint 2
The simplest approach to solving this problem is to perform a pre-order 
traversal on both trees, to store their leaf nodes in arrays in the order in 
which they're visited, and to then compare the two resulting arrays. This 
solution works, but it's not optimal from a space-complexity perspective. 
Can you think of a way to solve this problem using less extra space? It's 
possible to solve this with O(h1 + h2) space or better, where h1 is the 
height of tree1 and h2 is the height of tree2.

Hint 3
To solve this problem with a more optimal space complexity, you can 
perform pre-order traversals on both trees at the same time. As you traverse 
the trees, you need to look for the next leaf node in each tree and pause the 
traversal as soon as you find it. Once you've found the next leaf node in both 
trees, you can compare their values and see if they match; if they do, 
continue the traversal, and repeat the process. If they don't match, the leaf 
traversals aren't the same, and you can return false.

Hint 4
Another unique way to solve this problem is to connect all of the leaf nodes 
in each individual tree so as to form two linked lists. Since the leaf nodes 
don't have any children, you can use their right pointers to store the next 
leaf nodes in the leaf traversals. And since you're reusing the input trees to 
store the leaf traversals, the only extra space you'll be using comes from the 
recursion used in the traversal of the trees. Once both trees have their leaf 
nodes connected, you can iterate through the linked lists and check if they're 
the same. To compare the linked lists, you'll need to keep track of their heads 
(the first lead node in each tree).

Optimal Space & Time Complexity
O(n + m) time | O(max(h1, h2)) space - where n is the number of nodes in the 
first Binary Tree, m is the number in the second, h1 is the height of the 
first Binary Tree, and h2 is the height of the second

"""





##### Solution 1 #####
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n + m) time | O(max(h1, h2)) space - where n is the number of nodes in the first 
# Binary Tree, m is the number in the second, h1 is the height of the first Binary 
# Tree, and h2 is the height of the second
def compareLeafTraversal(tree1, tree2):
    tree1TraversalStack = [tree1]
    tree2TraversalStack = [tree2]

    while len(tree1TraversalStack) > 0 and len(tree2TraversalStack) > 0:
        tree1Leaf = getNextLeafNode(tree1TraversalStack)  
        tree2Leaf = getNextLeafNode(tree2TraversalStack)  

        if tree1Leaf.value != tree2Leaf.value:
            return False

    return len(tree1TraversalStack) == 0 and len(tree2TraversalStack) == 0
    

def getNextLeafNode(traversalStack):
    currentNode = traversalStack.pop()

    while not isLeafNode(currentNode):
        if currentNode.right is not None:
            traversalStack.append(currentNode.right)

        # We purposely add the left node to the stack after the 
        # right node so that it gets popped off the stack first.
        if currentNode.left is not None:
            traversalStack.append(currentNode.left)

        currentNode = traversalStack.pop()

    return currentNode


def isLeafNode(node):
    return node.left is None and node.right is None





##### Solution 2 #####
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n + m) time | O(max(h1, h2)) space - where n is the number of nodes in the first 
# Binary Tree, m is the number in the second, h1 is the height of the first Binary 
# Tree, and h2 is the height of the second
def compareLeafTraversal(tree1, tree2):
    tree1LeafNodesLinkedList, _ = connectLeafNodes(tree1)
    tree2LeafNodesLinkedList, _ = connectLeafNodes(tree2)

    list1CurrentNode = tree1LeafNodesLinkedList
    list2CurrentNode = tree2LeafNodesLinkedList
    while list1CurrentNode is not None and list2CurrentNode is not None:
        if list1CurrentNode.value != list2CurrentNode.value: 
            return False

        list1CurrentNode = list1CurrentNode.right
        list2CurrentNode = list2CurrentNode.right
      
    return list1CurrentNode is None and list2CurrentNode is None
    

def connectLeafNodes(currentNode, head=None, previousNode=None):
    if currentNode is None:
        return head, previousNode  

    if isLeafNode(currentNode):
        if previousNode is None:
            head = currentNode
        else:
            previousNode.right = currentNode

        previousNode = currentNode    

    leftHead, leftPreviousNode = connectLeafNodes(currentNode.left, head, previousNode)  
    return connectLeafNodes(currentNode.right, leftHead, leftPreviousNode)  


def isLeafNode(node):
    return node.left is None and node.right is None
