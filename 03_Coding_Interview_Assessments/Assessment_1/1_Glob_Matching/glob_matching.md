# Glob Matching

# [Difficulty:_Hard]
# [Category:_Dynamic_Programming]

In most modern-day computers, glob patterns are used to refer to multiple file names on the computer's system at once.

Glob patterns typically take advantage of the following two special characters:

  1. Wildcards, represented by the `*` symbol, which match any
    number of characters, including zero characters.

  2. Question marks, represented by the `?` symbol, which match any single character (exactly one).

For example, the glob pattern `"*.js"` matches any file name ending in the JavaScript `.js` extension.

Write a function that takes in a file name and a pattern (both strings) and returns whether that file name matches the pattern.

# [Sample_Input]

  fileName = "abcdefg"
  pattern = "a*e?g"

# [Sample_Output]

  true

# Hints

# [Hint_1]

  You can solve this question optimally by using dynamic programming.

# [Hint_2]

  Build an (n + 1) x (m + 1) table, where n and m are the respective lengths of the file name and pattern. The value at indices (i, j) in the table will represent whether the file name and pattern ending at indices i - 1 and j - 1, respectively, match; and the first row and column will represent the relevant empty strings. You'll need to figure out the relation between previously computed matches and the characters at given indices in the strings as you build up the table.

# [Optimal_Space_&_Time_Complexity]

  O(n * m) time | O(n * m) space - where n is the length of the fileName and m is the length of the pattern.
