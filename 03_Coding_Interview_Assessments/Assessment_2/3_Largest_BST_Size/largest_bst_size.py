

# Average case: when the tree is balanced
# O(n) time | O(h) space - where n is the number of nodes in
# the Binary Tree and h is the height of the Binary Tree
def largestBstSize(tree):
    return getTreeInfo(tree).runningLargestBstSize


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(
            True,
            float("-inf"),
            float("inf"),
            0,
            0,
        )

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    treeSize = 1 + leftTreeInfo.treeSize + rightTreeInfo.treeSize

    satisfiesBstProp = tree.value > leftTreeInfo.maxValue and tree.value <= rightTreeInfo.minValue
    isBst = satisfiesBstProp and leftTreeInfo.isBst and rightTreeInfo.isBst

    maxValue = max(tree.value, max(leftTreeInfo.maxValue, rightTreeInfo.maxValue))
    minValue = min(tree.value, min(leftTreeInfo.minValue, rightTreeInfo.minValue))

    runningLargestBstSize = 0
    if isBst:
        runningLargestBstSize = treeSize
    else:
        runningLargestBstSize = max(
            leftTreeInfo.runningLargestBstSize, rightTreeInfo.runningLargestBstSize
        )

    return TreeInfo(
        isBst,
        maxValue,
        minValue,
        runningLargestBstSize,
        treeSize,
    )


class TreeInfo:
    def __init__(self, isBst, maxValue, minValue, runningLargestBstSize, treeSize):
        self.isBst = isBst
        self.maxValue = maxValue
        self.minValue = minValue
        self.runningLargestBstSize = runningLargestBstSize
        self.treeSize = treeSize


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
