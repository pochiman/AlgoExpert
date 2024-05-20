""" 

[ Difficulty: Medium ]
[ Category: Linked Lists ]

##### Merging Linked Lists #####

You're given two Linked Lists of potentially unequal length. These Linked Lists 
potentially merge at a shared intersection node. Write a function that returns 
the intersection node or returns None / null  if there is no intersection.
  
Each LinkedList node has an integer value as well as a next node pointing to the 
next node in the list or to None / null if it's the tail of the list.
  
Note: Your function should return an existing node. It should not modify either 
Linked List, and it should not create any new Linked Lists.


##### Sample Input #####
linkedListOne = 2 -> 3 -> 1 -> 4
linkedListTwo = 8 -> 7 -> 1 -> 4

##### Sample Output #####
1 -> 4 // The lists intersect at the node with value 1


##### Hints #####

Hint 1
All of the nodes after the intersection point of two Linked Lists will be 
the same.

Hint 2
If the two Linked Lists are of different lengths, then none of the extra 
nodes of the longer list at the beginning can be the intersection point, 
since the ends must be the same.

Hint 3
The length of the first list + the distance of the second head from the 
intersection point will be equal to the length of the second list + the 
distance of the first head from the intersection point. This can be 
proven using the information from hints 1 and 2.

Optimal Space & Time Complexity
O(n + m) time | O(1) space - where n is the length of the first Linked List 
and m is the length of the second Linked List

"""





##### Solution 1 #####
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n + m) time | O(n) space - where n is the length of the
# first Linked List and m is the length of the second Linked List
def mergingLinkedLists(linkedListOne, linkedListTwo):
    listOneNodes = set()
    currentNodeOne = linkedListOne
    while currentNodeOne is not None:
        listOneNodes.add(currentNodeOne)
        currentNodeOne = currentNodeOne.next

    currentNodeTwo = linkedListTwo
    while currentNodeTwo is not None:
        if currentNodeTwo in listOneNodes:
            return currentNodeTwo
        currentNodeTwo = currentNodeTwo.next

    return None





##### Solution 2 #####
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n + m) time | O(1) space - where n is the length of the
# first Linked List and m is the length of the second Linked List
def mergingLinkedLists(linkedListOne, linkedListTwo):
    currentNodeOne = linkedListOne
    countOne = 0
    while currentNodeOne is not None:
        countOne += 1
        currentNodeOne = currentNodeOne.next

    currentNodeTwo = linkedListTwo
    countTwo = 0
    while currentNodeTwo is not None:
        countTwo += 1
        currentNodeTwo = currentNodeTwo.next

    difference = abs(countTwo - countOne)
    biggerCurrentNode = linkedListOne if countOne > countTwo else linkedListTwo
    smallerCurrentNode = linkedListTwo if countOne > countTwo else linkedListOne

    for _ in range(difference):
        biggerCurrentNode = biggerCurrentNode.next

    while biggerCurrentNode is not smallerCurrentNode:
        biggerCurrentNode = biggerCurrentNode.next
        smallerCurrentNode = smallerCurrentNode.next

    return biggerCurrentNode





##### Solution 3 #####
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n + m) time | O(1) space - where n is the length of the
# first Linked List and m is the length of the second Linked List
def mergingLinkedLists(linkedListOne, linkedListTwo):
    currentNodeOne = linkedListOne
    currentNodeTwo = linkedListTwo

    while currentNodeOne is not currentNodeTwo:
        if not currentNodeOne:
            currentNodeOne = linkedListTwo
        else:
            currentNodeOne = currentNodeOne.next

        if not currentNodeTwo:
            currentNodeTwo = linkedListOne
        else:
            currentNodeTwo = currentNodeTwo.next

    return currentNodeOne
