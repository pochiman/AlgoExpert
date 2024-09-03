# Inverted Bisection

# [Difficulty:_Hard]
# [Category:_Linked_Lists]

Write a function that takes in the head of a Singly Linked List, inverts its
bisection in place (i.e., doesn't create a brand new list), and returns its
new head.

Inverting a Linked List's bisection means inverting the order of the nodes in 
the list's two halves; see the sample inputs and outputs for examples.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing 
to the next node in the list or to `None`/`null` if it's the tail of the list.

You can assume that the input Linked List will always have at least one node;
in other words, the head will never be `None`/`null`.

# [Sanple_Input_#1]

  head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 // the head node with value 0

# [Sanple_Output_#1]

  2 -> 1 -> 0 -> 5 -> 4 -> 3 // the new head node with value 2

# [Sanple_Input_#2]

  head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 // the head node with value 0

# [Sanple_Output_#2]

  2 -> 1 -> 0 -> 3 -> 6 -> 5 -> 4 // the new head node with value 2

# Hints

# [Hint_1]

  Try dividing this problem into multiple simple steps. Also, think of how you'll handle odd-length linked lists compared to even-length ones.

# [Hint_2]

  The solution to this question can be divided into four parts: 1) counting the number of nodes in the linked list; 2) splitting the linked list into two equal halves; 3) reversing the two halves of the linked list; 4) reattaching the two reversed halves.

# [Optimal_Space_&_Time_Complexity]

  O(n) time | O(1) space - where n is the number of nodes in the Linked List
