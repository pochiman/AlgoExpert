# 10 - Stacks And Queues

Push. Pop. FIFO. LIFO. That pretty much sums up stacks and queues.

Ok, there might be a bit more to them than meets the eye. Watch our video to find 
out. Plus, it even features nifty stick figures!

# Key Terms

# [Stack]

  An array-like data structure whose elements follow the `LIFO` rule: `L`ast `I`n, 
  `F`irst `O`ut.

  A stack is often compared to a stack of books on a table: the last book that's 
  placed on the stack of books is the first one that's taken off the stack.
  
  The following are a stack's standard operations and their
  corresponding time complexities:

  • `Pushing an element onto the stack`: O(1)
  • `Popping an element off the stack`: O(1)
  • `Peeking at the element on the top of the stack`: O(1)
  • `Searching for an element in the stack`: O(n)

  A stack is typically implemented with a `dynamic array` or with a `singly linked list`.

# [Queue]

  An array-like data structure whose elements follow the `FIFO` rule: `F`irst `I`n, 
  `F`irst `O`ut.

  A queue is often compared to a group of people standing in line to purchase 
  items at a store: the first person to get in line is the first one to purchase 
  items and to get out of the queue.
  
  The following are a queue's standard operations and their corresponding time 
  complexities:

  • `Enqueuing an element into the queue`: O(1)
  • `Dequeuing an element out of the queue`: O(1)
  • `Peeking at the element at the front of the queue`: O(1)
  • `Searching for an element in the queue`: O(n)

  A queue is typically implemented with a `doubly linked list`.
