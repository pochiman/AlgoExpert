# Repeated Matrix Values

# [Difficulty:_Medium]
# [Category:_Arrays]

  Write a function that takes in a non-empty two-dimensional integer array (a
  matrix) of potentially unequal height and width and returns a list of the
  elements that appear at least once in each row and each column of the matrix.

# [Sample_Input]

  matrix = [
    [1, 3, 7, 4, 5],
    [2, 5, 9, 3, 3],
    [1, 8, 5, 3, 5],
    [5, 0, 3, 5, 6],
    [3, 8, 3, 5, 6],
    [1, 0, 3, 0, 5],
  ]

# [Sample_Output]

  [3, 5] // The numbers could be ordered differently.

# Hints

# [Hint_1]

  The integers found in the first row or first column of the matrix can serve as a guideline for which integers potentially appear at least once in each row and each column of the matrix.

# [Hint_2]

  You can find the desired integers by relying on the ones in the first row or first column of the matrix and then traversing the entire matrix twice: once row by row, and once column by column. At each integer in each row and column, check if that integer's been found the correct amount of times leading up to that point. You'll have to somehow handle integers that appear more than once in a given row or column.

# [Optimal_Space_&_Time_Complexity]

  O(n) time | O(min(w, h)) space - where n is the total number of elements in the matrix and w and h are the width and height of the matrix, respectively
