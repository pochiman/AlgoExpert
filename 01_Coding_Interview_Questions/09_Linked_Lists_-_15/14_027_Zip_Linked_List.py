""" 

[ Difficulty: Very Hard ]
[ Category: Linked Lists ]

##### Zip Linked List #####

You're given the head of a Singly Linked List of arbitrary length k. Write a function 
that zips the Linked List in place (i.e., doesn't create a brand new list) and returns 
its head.

A Linked List is zipped if its nodes are in the following order, where k is the length 
of the Linked List:

1st node -> kth node -> 2nd node -> (k - 1)th node -> 3rd node -> (k - 2)th node -> ... 

Each LinkedList node has an integer value as well as a next node pointing to the next 
node in the list or to None / null if it's the tail of the list.

You can assume that the input Linked List will always have at least one node; in other 
words, the head will never be None / null.


##### Sample Input #####
linkedList = 1 -> 2 -> 3 -> 4 -> 5 -> 6 // the head node with value 1    


##### Sample Output #####
1 -> 6 -> 2 -> 5 -> 3 -> 4 -> // the head node with value 1  


##### Hints #####

Hint 1
Try to imagine how you would solve this problem if you were given two distinct 
linked lists. For example, how would you zip the list 1 -> 2 -> 3 with the list 
4 -> 5 to get 1 -> 5 -> 2 -> 4 -> 3?

Hint 2
One of the most straightforward ways to solve this problem is to split the 
original linked list into two linked lists and to reverse the second linked 
list before interweaving it with the first one. Ultimately, you want the first 
node, then the kth node, then the second node, etc., so reversing the second 
linked list before interweaving it with the first one makes things simple.

Hint 3
After you split the linked list into two halves and reverse the second half, 
you'll have something like 1 -> 2 -> 3 and 5 -> 4; at this point, you can simply 
add the first node of the reversed second half into the first half between 1 and 
2 as in 1 -> 5 -> 2.... Simply continue this process until you've inserted all 
of the nodes from the reversed second half into the first.

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the length of the input Linked List

"""





##### Solution 1 #####
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space - where n is the length of the Linked List
def zipLinkedList(linkedList):
    if linkedList.next is None or linkedList.next.next is None:
        return linkedList

    firstHalfHead = linkedList
    secondHalfHead = splitLinkedList(linkedList)  

    reversedSecondHalfHead = reverseLinkedList(secondHalfHead)

    return interweaveLinkedLists(firstHalfHead, reversedSecondHalfHead)  


def splitLinkedList(linkedList):
    slowIterator = linkedList
    fastIterator = linkedList
    while fastIterator is not None and fastIterator.next is not None:
        slowIterator = slowIterator.next
        fastIterator = fastIterator.next.next

    secondHalfHead = slowIterator.next
    slowIterator.next = None
    return secondHalfHead


def interweaveLinkedLists(linkedList1, linkedList2):
    linkedList1Iterator = linkedList1
    linkedList2Iterator = linkedList2
    while linkedList1Iterator is not None and linkedList2Iterator is not None: 
        linkedList1IteratorNext = linkedList1Iterator.next
        linkedList2IteratorNext = linkedList2Iterator.next
        
        linkedList1Iterator.next = linkedList2Iterator 
        linkedList2Iterator.next = linkedList1IteratorNext

        linkedList1Iterator = linkedList1IteratorNext
        linkedList2Iterator = linkedList2IteratorNext

    return linkedList1


def reverseLinkedList(linkedList):
    previousNode, currentNode = None, linkedList
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode
