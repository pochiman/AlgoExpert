# Subtrees Within Range

# [Difficulty:_Medium]
# [Category:_Binary_Search_Trees]

  Write a function that takes in a Binary Search Tree (BST) and a range of
  integers and returns the number of subtrees in the BST that are only made up
  of nodes with values contained in the range.

  For example, if the range is `[10, 12]`, your function should
  return the number of subtrees in the BST that are only made up of nodes with
  values 10, 11, or 12.

  Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if and only if it satisfies the BST
  property: its `value` is strictly greater than the values of every
  node to its left; its `value` is less than or equal to the values
  of every node to its right; and its children nodes are either valid
  `BST` nodes themselves or `None` / `null`.

# [Sample_Input]

  tree =   10
         /     \
        5      15
      /   \   /   \
     2     8 13   22
   /      / \  \
  1      5   9  14
  targetRange = [5, 15]

# [Sample_Output]

  5
  // The 5 subtrees are:
  //   8    5    9    13    14
  //  / \               \
  // 5   9               14

# Hints

# [Hint_1]

  Can you come up with a recursive relation between whether a tree is within the target range and whether its subtrees are within the range?

# [Hint_2]

  A tree is within the target range if its root node's value is within the range and if its left and right subtrees are within the range.

# [Optimal_Space_&_Time_Complexity]

  Average case: when the tree is balanced O(n) time | O(h) space - where n is the number of nodes in the BST and h is the height of the BST
