# Reverse Alternating K Nodes

# [Difficulty:_Very_Hard]
# [Category:_Linked_Lists]

  Write a function that takes in the head of a Singly Linked List and a non-zero
  integer `k`, reverses alternating groups of k nodes in the linked
  list in place (i.e., doesn't create a brand new list), and returns its new
  head.

  Reversing alternating groups of k nodes means reversing the first k nodes in
  the list, then not reversing the following k nodes, then reversing the k nodes
  after that, then not reversing the k nodes after that, and so on and so forth
  until the tail of the linked list.

  Note that the linked list won't necessarily have a total number of nodes
  that's divisible by k. In other words, the final group of nodes in the linked
  list might have fewer than k nodes.

  Each `LinkedList` node has an integer `value` as well as
  a `next` node pointing to the next node in the list or to
  `None` / `null` if it's the tail of the list.

  You can assume that the input Linked List will always have at least one node;
  in other words, the head will never be `None` / `null`.

# [Sample_Input]

  head = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14 // the head node with value 1
  k = 3

# [Sample_Output]

  3 -> 2 -> 1 -> 4 -> 5 -> 6 -> 9 -> 8 -> 7 -> 10 -> 11 -> 12 -> 14 -> 13 // the new head node with value 3

# Hints

# [Hint_1]

  Make sure not to lose reference to the conceptual tails and heads of the various groups of k nodes in the linked list, since you'll have to update certain pointers when you "reattach" groups that have been reversed.

# [Hint_2]

  Try traversing the linked list a single time, repeatedly reversing k nodes in place and then skipping the following k nodes by simply iterating through them.

# [Optimal_Space_&_Time_Complexity]

  O(n) time | O(1) space - where n is the number of nodes in the Linked List
