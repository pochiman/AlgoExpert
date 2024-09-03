

# This is the class of the input Linked List.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space - where n is the number of nodes in the Linked List
def invertedBisection(head):
    length = getLinkedListLength(head)
    if length <= 3:
        return head

    firstHalfTail = getMiddleNode(head, length)
    middleNode = None
    secondHalfHead = None
    if length % 2 == 0:
        secondHalfHead = firstHalfTail.next
    else:
        middleNode = firstHalfTail.next
        secondHalfHead = firstHalfTail.next.next

    firstHalfTail.next = None
    reverseLinkedList(head)
    reversedSecondHalfHead = reverseLinkedList(secondHalfHead)

    if middleNode is None:
        head.next = reversedSecondHalfHead
    else:
        head.next = middleNode
        middleNode.next = reversedSecondHalfHead

    return firstHalfTail


def getLinkedListLength(head):
    length = 0
    currentNode = head
    while currentNode is not None:
        currentNode = currentNode.next
        length += 1
    return length


def getMiddleNode(head, length):
    halfLength = length // 2
    currentPosition = 1
    currentNode = head
    while currentPosition != halfLength:
        currentNode = currentNode.next
        currentPosition += 1
    return currentNode


def reverseLinkedList(head):
    previousNode, currentNode = None, head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode
