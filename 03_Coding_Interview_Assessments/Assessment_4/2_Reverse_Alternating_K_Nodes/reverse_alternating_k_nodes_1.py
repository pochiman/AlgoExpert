

# This is the class of the input Linked List.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space - where n is the number of nodes in the Linked List
def reverseAlternatingKNodes(head, k):
    finalHead = None

    isGroupToReverse = True
    runningK = 1

    previousGroupTail = None
    currentGroupHead = head
    currentNode = head

    while currentNode is not None:
        shouldReverse = isGroupToReverse and (runningK == k or currentNode.next is None)

        if not shouldReverse:
            if runningK == k:
                runningK = 1
                isGroupToReverse = True

                previousGroupTail = currentNode
                currentGroupHead = currentNode.next
            else:
                runningK += 1

            currentNode = currentNode.next
            continue

        runningK = 1
        isGroupToReverse = False

        nextNode = currentNode.next
        currentNode.next = None
        reversedGroupHead = reverseLinkedList(currentGroupHead)
        reversedGroupTail = currentGroupHead
        reversedGroupTail.next = nextNode

        if previousGroupTail is None:
            finalHead = reversedGroupHead
        else:
            previousGroupTail.next = reversedGroupHead

        currentNode = nextNode
        currentGroupHead = nextNode
        previousGroupTail = reversedGroupTail

    return finalHead


def reverseLinkedList(head):
    previousNode, currentNode = None, head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode
