# Spin Rings

# [Difficulty:_Medium]
# [Category:_Arrays]


  Write a function that takes in a square-shaped (n x n) two-dimensional array
  representing a set of rings. For instance, a 4 x 4 array is made up of the
  following two rings:

  [
    [-, -, -, -],
    [-,  ,  , -],
    [-,  ,  , -]
    [-, -, -, -],
  ]

  [
    [ ,  ,  ,  ],
    [ , -, -,  ],
    [ , -, -,  ]
    [ ,  ,  ,  ],
  ]


  The function should spin the rings in the array in a clockwise direction. In
  other words, every value in each respective ring should be shifted by one
  position in a clockwise direction.

  This operation should be done in place; it should mutate the input array.

# [Sample_Input]

  array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
  ]

# [Sample_Output]

  // This is the mutated input array.
  [
    [5, 1, 2, 3],
    [9, 10, 6, 4],
    [13, 11, 7, 8],
    [14, 15, 16, 12]
  ]  

# Hints

# [Hint_1]

  You can solve this problem both iteratively and recursively using four for loops.

# [Hint_2]

  Going off of Hint #1, you'll have to declare four variables: a starting row, a starting column, an ending row, and an ending column. These four variables will represent the bounds of the each ring that you spin. Start with the outermost ring, and then move the bounds inwards.

# [Optimal_Space_&_Time_Complexity]

  O(n) time | O(1) space - where n is the total number of elements in the array
