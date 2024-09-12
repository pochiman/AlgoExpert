# Balance Index

# [Difficulty:_Medium]
# [Category:_Arrays]


  Write a function that takes in a non-empty array of integers and returns its
  balance index.

  An array `a`'s balance index is an index `i` such that `a[0] + a[1] + ... + a[i - 1]` 
  is equal to `a[i + 1] + a[i + 2] + ... + a[lastIdx]`.

  In order for `0` to be an array's balance index, `a[1] + a[2] + ... + a[lastIdx]` must be equal to `0`.

  Similarly, in order for the last index of an array to be the array's balance
  index, `a[0] + a[1] + ... + a[lastIdx - 1]` must be equal to `0`.

  If there is no balance index in the array, your function should return `-1`; if there are multiple possible answers, your function can return any of them.
  
# [Sample_Input]

  array = [0, 9, -8, 2, 7, 1, 11, -2, 1]

# [Sample_Output]

  5 // 0 + 9 + -8 + 2 + 7 == 11 + -2 + 1

# Hints

# [Hint_1]

  You can solve this question in linear time and with constant space.

# [Hint_2]

  At index 0, the sum of the left side of the array is 0 and the sum of the right side of the array is the sum of all values in the array minus the very first value. If you store these two values and move to index 1, what do you have to do to these stored values to get the newly relevant left-side sum and right-side sum?

# [Optimal_Space_&_Time_Complexity]

  O(n) time | O(1) space - where n is the length of the input array
