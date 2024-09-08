# Max Subsequence Dot Product

# [Difficulty:_Very_Hard]
# [Category:_Dynamic_Programming]

  In mathematics, the dot product of two vectors `a = [a1, a2, ..., an]` and 
  `b = [b1, b2, ..., bn]` is equal to `a1 * b1 + a2 * b2 + ... + an * bn`.

  This operation isn't limited to just vectors; it can be applied to any two
  sequences of numbers of the same length.

  Write a function that takes in two non-empty arrays of integers and returns
  the maximum dot product that can be obtained from any two subsequences of the respective input arrays (one subsequence from each array).

  While the input arrays might have different lengths, the two subsequences that yield the maximum dot product will have to be of equal length, as per the definition of the dot product.
  
  A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers `[1, 3, 4]` form a subsequence of the array `[1, 2, 3, 4]`, and so do the numbers `[2, 4]`. Note
  that a single number in an array and the array itself are both valid
  subsequences of the array.

# [Sample_Input]

  arrayOne = [4, 7, 9, -6, 6]
  arrayTwo = [5, 1, -1, -3, -2, -10]

# [Sample_Output]

  105 // From the subsequences [9, -6] and [5, -10].

# Hints

# [Hint_1]

  You can solve this question optimally by using dynamic programming.

# [Hint_2]

  Build an (n + 1) x (m + 1) table, where n and m are the respective lengths of the arrays. The value at indices (i, j) in the table will represent the max dot product that can be obtained for the arrays ending at indices i - 1 and j - 1, respectively, and the first row and column will represent the relevant empty arrays. You'll need to figure out the relation between previously computed max dot products and the integers at given indices in the arrays as you build up the table.

# [Optimal_Space_&_Time_Complexity]

  O(n * m) time | O(n * m) space - where n is the length of the first input array and m is the length of the second input array
