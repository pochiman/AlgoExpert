# Count Contained Permutations

# [Difficulty:_Very_Hard]
# [Category:_Strings]

  You're given two non-empty strings: a big string and a small string. Write a
  function that returns the number of permutations of the small string that are
  contained in the big string.

  Repeated permutations should be counted, and the small string counts as a
  permutation of itself.

# [Sample_Input]

  bigString = "cbabcacabca"
  smallString = "abc"

# [Sample_Output]

  6 // "cba", "abc", "bca", "cab", "abc", "bca"

# Hints

# [Hint_1]

  You can solve this question with a single pass through the big string and without computing any of the permutations of the small string.

# [Hint_2]

  Start by storing the counts of the small string's characters in a hash table. Then, use two pointers separated by the length of the small string to traverse the big string, continuously checking if the counts of the characters in between the pointers match those of the characters in the substring.

# [Optimal_Space_&_Time_Complexity]

  O(b + s) time | O(s) space - where b is the length of the big input string and s is the length of the small input string
