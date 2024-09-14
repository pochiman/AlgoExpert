

# Average case: when the tree is balanced
# O(n) time | O(h) space - where n is the number of
# nodes in the BST and h is the height of the BST
def subtreesWithinRange(tree, targetRange):
    answer = {"result": 0}
    isTreeWithinRange(tree, targetRange, answer)
    return answer["result"]


def isTreeWithinRange(tree, targetRange, answer):
    if tree is None:
        return True

    leftTreeWithinRange = isTreeWithinRange(tree.left, targetRange, answer)
    rightTreeWithinRange = isTreeWithinRange(tree.right, targetRange, answer)
    nodeInRange = tree.value >= targetRange[0] and tree.value <= targetRange[1]
    treeWithinRange = leftTreeWithinRange and rightTreeWithinRange and nodeInRange

    if treeWithinRange:
        answer["result"] += 1

    return treeWithinRange


# This is the class of the input BST.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
