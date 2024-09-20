# Longest Increasing Matrix Path

# [Difficulty:_Hard]
# [Category:_Recursion]

  Write a function that takes in a non-empty two-dimensional integer array (a
  matrix) of potentially unequal height and width and returns the length of its
  longest increasing path.

  A matrix path is a collection of matrix elements where each element is
  horizontally or vertically adjacent to the next element.

  A matrix path is increasing if each of its elements is strictly greater than
  the previous element.

# [Sample_Input]

  matrix = [
    [1,  2,  4,  3,  2],
    [7,  6,  5,  5,  1],
    [8,  9,  7, 15, 14],
    [5, 10, 11, 12, 13],
  ]

# [Sample_Output]

  15

  // The longest increasing path can be clearly
  // seen here, starting at 1 and ending at 15:
  // [
  //   [ ,   ,  4,  3,  2],
  //   [7,  6,  5,   ,  1],
  //   [8,  9,   , 15, 14],
  //   [ , 10, 11, 12, 13],
  // ]

# Hints

# [Hint_1]

  You'll have to use some form of caching in order to solve this problem optimally.

# [Hint_2]

  Create a matrix of the same size as the input matrix, and at each cell in this matrix, store the length of the longest increasing matrix path starting at that cell. Use this matrix as a cache to avoid computing the same values multiple times, since some values in this matrix will naturally depend on other, adjacent values in the matrix.

# [Optimal_Space_&_Time_Complexity]

  O(n) time | O(n) space - where n is the total number of elements in the matrix
