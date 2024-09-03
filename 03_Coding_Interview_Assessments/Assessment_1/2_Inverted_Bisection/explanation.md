# Inverted Bisection [Summary]

The solution to this question can be divided into four parts:

  • 1) Counting the number of nodes in the linked list.
  • 2) Splitting the linked list into two equal halves.
  • 3) Reversing the two halves of the linked list.
  • 4) Reattaching the two reversed halves.
 
# [1)_Counting_the_nodes]

This step is done trivially by simply iterating through the linked list and incrementing a counter at every node.

# [2)_Splitting_the_linked_list]

For this step, we first iterate through the linked list up to its halfway point, basing ourselves off of its previously calculated length.

At this point, we have to handle the trickiness that comes with an odd-length linked list. An odd-length linked list will have a middle node that should remain unmoved in the final linked list. To handle this, we keep a reference to the middle node if the linked list is of odd length before splitting the list in half.

The split is done by simply overwriting the first half's tail's next pointer.

In this process, we'll naturally keep references to the first half's tail and to the second half's head.

# [3)_Reversing_the_two_halves]

This step is very straightforward, but you'll need to know how to reverse a linked list; see the `Reverse Linked List` question on AlgoExpert if you need a refresher.

We simply write a helper function to reverse a linked list, and we call it on the two halves. We'll need to store a reference to the head of the reversed second half for the final step.

# [4)_Reattaching_the_two_halves]

Keeping in mind the trickiness of the middle node, we handle this step slightly differently depending on whether the linked list is of odd length.

If it is of odd length, then the tail of the reversed first half--which is the head of the original linked list--should point to the stored middle node, and the middle node should in turn point to the head of the reversed second half.

If it isn't of odd length, then the tail of the reversed first half should directly point to the head of the reversed second half.

# [Complexity_Analysis]

This question is self-evidently solved in linear time and with constant space.

# [Closing_Thoughts]

As with most Linked List problems, this question's difficulty lies in handling edge cases, overwriting pointers appropriately, and keeping references to certain nodes.

Oh, and reversing linked lists of course!
