""" 

##### Merge Linked Lists #####

Write a function that takes in the heads of two Singly Linked List that are in 
sorted order, respectively. The function should merge the lists in place (i.e., 
it shouldn't create a brand new list) and return the head of the merged list; 
the merged list should be in sorted order.

Each LinkedList node has an integer value as well as well as a next node pointing 
to the next node in the list or to None / null if it's the tail of the list.

You can assume that the input Linked Lists will always have at least one node; in 
other words, the heads will never be None / null.


##### Sample Input #####
headOne = 2 -> 6 -> 7 -> 8 // the head node with value 2
headTwo = 1 -> 3 -> 4 -> 5 -> 9 -> 10 // the head node with value 1

##### Sample Output #####
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 // the new head node with value 1


##### Hints #####

Hint 1
You can iterate through the Linked Lists from head to tail and merge them 
along the way by inserting nodes from the second Linked List into the first 
Linked List.

Hint 2
You'll need to manipulate three nodes at once at every step.

Hint 3
At every step, you'll need to have three variables (p1, p2, and p1Prev) 
pointing to the current node in the first Linked List (p1), the current 
node in the second Linked List (p2), and the previous node in the first 
Linked List (p1Prev). If the value of p1 is smaller than the value of 
p2, then you can just "move forward" in the first Linked List by moving 
p1 and p1Prev forward by one position (p1Prev becomes p1 and p1 becomes 
p1.next). If the value of p1 is greater than the value of p2, then you 
need to insert p2 before p1. You'll have to first make p1Prev point to 
p2, then make p2 point to p1, all the while not losing track of p2's 
"next" node, which you'll need to move to right after. You'll also have 
to handle edge cases when you're dealing with head nodes or tail nodes.

Hint 4
You can implement this algorithm both iteratively and recursively 
following nearly identical logic.

Optimal Space & Time Complexity
O(n + m) time | O(1) space - where n is the number of nodes in the first 
Linked List and m is the number of nodes in the second Linked List

"""





##### Solution 1 #####
# This is an input class. Do not edit.
class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None


# O(n + m) time | O(1) space - where n is the number of nodes in the first 
# Linked List and m is the number of nodes in the second Linked List
def mergeLinkedLists(headOne, headTwo):
  p1 = headOne
  p1Prev = None
  p2 = headTwo
  while p1 is not None and p2 is not None:
    if p1.value < p2.value:
      p1Prev = p1
      p1 = p1.next
    else:
      if p1Prev is not None:
        p1Prev.next = p2
      p1Prev = p2
      p2 = p2.next
      p1Prev.next = p1
  if p1 is None:
    p1Prev.next = p2
  return headOne if headOne.value < headTwo.value else headTwo





##### Solution 2 #####
# This is an input class. Do not edit.
class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None


# O(n + m) time | O(n + m) space - where n is the number of nodes in the first 
# Linked List and m is the number of nodes in the second Linked List
def mergeLinkedLists(headOne, headTwo):
  recursiveMerge(headOne, headTwo, None)
  return headOne if headOne.value < headTwo.value else headTwo   


def recursiveMerge(p1, p2, p1Prev):
  if p1 is None:
    p1Prev.next = p2
    return
  if p2 is None:
    return  
    
  if p1.value < p2.value:
    recursiveMerge(p1.next, p2, p1)
  else:
    if p1Prev is not None:
      p1Prev.next = p2
    newP2 = p2.next
    p2.next = p1
    recursiveMerge(p1, newP2, p2)
