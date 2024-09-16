

# This is the class of the input Linked List.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space - where n is the number of nodes in the Linked List
def reverseAlternatingKNodes(head, k):
    finalHead = None

    previousNode = None
    currentNode = head
    while currentNode is not None:
        reversedGroupHead, nextNode = reverseKNodes(currentNode, k)
        # The `currentNode` is now the tail of the reversed
        # group, so we make it point to the `nextNode`.
        currentNode.next = nextNode
        currentNode = nextNode

        if previousNode is None:
            finalHead = reversedGroupHead
        else:
            previousNode.next = reversedGroupHead

        skippedNodesCount = 0
        while currentNode is not None and skippedNodesCount < k:
            previousNode = currentNode
            currentNode = currentNode.next

            skippedNodesCount += 1

    return finalHead


def reverseKNodes(head, k):
    reversedNodesCount = 0
    previousNode, currentNode = None, head
    while currentNode is not None and reversedNodesCount < k:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode

        reversedNodesCount += 1

    return (previousNode, currentNode)
