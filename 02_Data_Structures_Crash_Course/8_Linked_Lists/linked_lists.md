# 8 - Linked Lists

The data structure whose singular purpose in life is to be reversed. Even right here on AlgoExpert, in fact.

That’s right, head on over to the hard questions list after watching this video, and reverse that bad boy six ways to Sunday.

# Key Terms

# [Singly_Linked_List]

  A data structure that consists of nodes, each with some value and a pointer to
  the next node in the linked list. A linked list node's value and next node are
  typically stored in `value` and `next` properties, respectively.
  
  The first node in a linked list is referred to as the `head` of the
  linked list, while the last node in a linked list, whose `next` property points to the `null` value, is known as the `tail` of the linked list.
  
  Below is a visual representation of a singly linked list whose nodes hold
  integer values:
  
    0 -> 1 -> 2 -> 3 -> 4 -> 5 -> null

  A singly linked list typically exposes its head to its user for easy access.
  While finding a node in a singly linked list involves traversing through all
  of the nodes leading up to the node in question (as opposed to instant access
  with an array), adding or removing nodes simply involves overwriting `next` 
  pointers (assuming that you have access to the node right before the node that 
  you're adding or removing).

  The following are a singly linked list's standard operations and their
  corresponding time complexities:

  • `Accessing the head`: O(1)
  • `Accessing the tail`: O(n)
  • `Accessing a middle node`: O(n)
  • `Inserting / Removing the head`: O(1)
  • `Inserting / Removing the tail`: O(n) to access + O(1)
  • `Inserting / Removing a middle node`: O(n) to access + O(1)
  • `Searching for a value`: O(n)

# [Doubly_Linked_List]

  Similar to a `singly linked list`, except that each node in a doubly
  linked list also has a pointer to the previous node in the linked list. The
  previous node is typically stored in a `prev` property.

  Just as the `next` property of a doubly linked list's `tail` points to the 
  `null` value, so too does the `prev` property of a doubly linked list's `head`.

  Below is a visual representation of a doubly linked list whose nodes hold
  integer values:

    null <- 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 -> null  
   
  While a doubly linked list typically exposes both its head and tail to its
  user, as opposed to just its head in the case of a singly linked list, it
  otherwise behaves very similarly to a singly linked list. 

  The following are a doubly linked list's standard operations and their
  corresponding time complexities:

  • `Accessing the head`: O(1)
  • `Accessing the tail`: O(1)
  • `Accessing a middle node`: O(n)
  • `Inserting / Removing the head`: O(1)
  • `Inserting / Removing the tail`: O(1)
  • `Inserting / Removing a middle node`: O(n) to access + O(1)
  • `Searching for a value`: O(n)

# [Circular_Linked_List]

  A linked list that has no clear `head` or `tail`, because its "tail"
  points to its "head," effectively forming a closed circle.

  A circular linked list can be either a `singly circular linked list` or a 
  `doubly circular linked list`.
