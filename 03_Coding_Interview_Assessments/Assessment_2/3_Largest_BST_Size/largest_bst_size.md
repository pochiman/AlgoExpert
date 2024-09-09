# Largest BST Size

# [Difficulty:_Hard]
# [Category:_Binary_Search_Trees]

  Write a function that takes in a Binary Tree and returns the size of the
  largest Binary Search Tree (BST) contained in it.

  Each `BinaryTree` node has an integer `value`, a `left` child node, and a `right` 
   child node. Children nodes can either be `BinaryTree` nodes themselves or `None` / `null`.

  A BST is a special type of Binary Tree whose nodes all satisfy the BST
  property. A node satisfies the BST property if its `value` is
  strictly greater than the values of every node to its left; its
  `value` is less than or equal to the values of every node to its
  right; and its children nodes are either valid `BST` nodes
  themselves or `None` / `null`.

# [Sample_Input]  
  
  tree =            20
            /                \ 
           7                 10
         /   \             /     \
        0     8           5      15
            /   \       /   \   /   \
           7     9     2     5 13   22
                     /           \
                    1             14

# [Sample_Output]

  9 // The subtree rooted at 10 is the largest BST in the tree, with 9 nodes.

# Hints

# [Hint_1]

  You'll need to have each node in tree pass information up to its parent node. What information does each node need from its children nodes?

# [Hint_1]

  At any given node in the tree, you can figure out if the subtree rooted at that node is a BST by checking if both of its subtrees are themselves BSTs and by also checking if the current node's value is strictly greater than the left subtree's max value and if the current node's value is less than or equal to the right subtree's min value.

# [Optimal_Space_&_Time_Complexity]

  Average case: when the tree is balanced O(n) time | O(h) space - where n is the number of nodes in the Binary Tree and h is the height of the Binary Tree
