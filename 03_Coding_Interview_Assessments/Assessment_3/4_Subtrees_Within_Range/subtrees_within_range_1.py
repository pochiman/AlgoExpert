

# Average case: when the tree is balanced
# O(n) time | O(h) space - where n is the number of
# nodes in the BST and h is the height of the BST
def subtreesWithinRange(tree, targetRange):
    return getTreeInfo(tree, targetRange).numSubtreesWithinRange


def getTreeInfo(tree, targetRange):
    numSubtreesWithinRange = 0
    maxValue = tree.value
    minValue = tree.value

    if tree.left is not None:
        leftSubtreeInfo = getTreeInfo(tree.left, targetRange)
        minValue = leftSubtreeInfo.minValue
        numSubtreesWithinRange += leftSubtreeInfo.numSubtreesWithinRange

    if tree.right is not None:
        rightSubtreeInfo = getTreeInfo(tree.right, targetRange)
        maxValue = rightSubtreeInfo.maxValue
        numSubtreesWithinRange += rightSubtreeInfo.numSubtreesWithinRange

    if minValue >= targetRange[0] and maxValue <= targetRange[1]:
        numSubtreesWithinRange += 1

    return TreeInfo(
        maxValue,
        minValue,
        numSubtreesWithinRange,
    )


class TreeInfo:
    def __init__(self, maxValue, minValue, numSubtreesWithinRange):
        self.maxValue = maxValue
        self.minValue = minValue
        self.numSubtreesWithinRange = numSubtreesWithinRange


# This is the class of the input BST.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
