# Longest Streak Of Adjacent Ones

# [Difficulty:_Medium]
# [Category:_Arrays]

  Write a function that takes in a non-empty array of only `0`s and `1`s and returns the index of the `0` that, if replaced
  by a `1`, would form the longest streak of adjacent `1`s
  in the entire array.

  If there are no `0`s in the array, your function should return
  `-1`; if there are multiple possible answers, your function can
  return any of them.

# [Sample_Input]

  array = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1]

# [Sample_Output]

  8 // Replacing the 0 at index 8 with a 1 forms a streak of 6 adjacent 1s.

# Hints

# [Hint_1]

  You can solve this problem in a single pass through the input array.

# [Hint_2]

  As you traverse through the array, you'll only need to store four variables. Namely, the index of the replaced zero at any point in time, the length of the current streak of ones given the currently replaced zero, the length of the longest streak of ones found, and of course the potential answer throughout the traversal.

# [Optimal_Space_&_Time_Complexity]
  
  O(n) time | O(1) space - where n is the length of the input array
