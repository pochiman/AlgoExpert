""" 

[ Difficulty: Easy ]
[ Category: Linked Lists ]

##### Middle Node #####

You're given a Linked List with at least one node. Write a function that returns 
the middle node of the Linked List. If there are two middle nodes (i.e. an even 
length list), your function should return the second of these nodes.

Each LinkedList node has an integer value as well as a next node pointing to the 
next node in the list or to None / null if it's the tail of the list.


##### Sample Input #####
linkedList = 2 -> 7 -> 3 -> 5

##### Sample Output #####
       // The middle could be 7 or 3,
3 -> 5 // we return the second middle node


##### Hints #####

Hint 1
The middle node of a Linked List will always be at index length / 2.

Hint 2
While the LinkedList class has no length, you can calculate it by simply 
iterating through the entire list.

Hint 3
If you create a slow and a fast pointer, with the fast one iterating at twice
the speed, the slow one will be in the middle when the fast one reaches the
end.

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the number of nodes in the linked list

"""





##### Solution 1 #####
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space - where n is the number of nodes in the linked list
def middleNode(linkedList):
    count = 0
    currentNode = linkedList
    while currentNode is not None:
        count += 1
        currentNode = currentNode.next

    middleNode = linkedList
    for _ in range(count // 2):
        middleNode = middleNode.next
    return middleNode





##### Solution 2 #####
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space - where n is the number of nodes in the linked list
def middleNode(linkedList):
    slowNode = linkedList
    fastNode = linkedList
    while fastNode and fastNode.next:
        slowNode = slowNode.next
        fastNode = fastNode.next.next

    return slowNode
