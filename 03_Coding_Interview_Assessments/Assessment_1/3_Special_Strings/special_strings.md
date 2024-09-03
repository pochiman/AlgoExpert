# Special Strings

# [Difficulty:_Hard]
# [Category:_Tries]

  Write a function that takes in a list of non-empty strings and returns a list
  of all the special strings found in the input list.

  A string is said to be special if it's exactly made up of at least two
  instances of other strings in the input list of strings.

  In order for a string to be special, just containing two instances of other
  strings isn't sufficient; the string must be exactly made up of those other
  strings. For example, in the list `["a", "b", "abc"]`, the string
  `"abc"` isn't special, even though it contains `"a"` and `"b"`, because `"c"` 
   isn't a string in the list.

  Note that strings can be repeated to form a special string; for instance, in
  the list `["a", "aaa"],` the string `"aaa"` is a special
  string because it's made up of three repeated instances of `"a"`.

  Also note that you can't use language-built-in string-matching methods.

# [Sample_Input]

  strings = [
    "foobarbaz",
    "foo",
    "bar",
    "foobarfoo",
    "baz",
    "foobaz",
    "foofoofoo",
    "foobazar",
  ]

# [Sample_Output]

  ["foobarbaz", "foobarfoo", "foobaz", "foofoofoo"]

# Hints

# [Hint_1]

  You can solve this question optimally by using a trie.

# [Hint_2]

  Insert every string in a trie, and then, for each string, traverse both the string in question and the trie at the same time to see if at least two instances of other strings are contained in the string in question.

# [Optimal_Space_&_Time_Complexity]

  Average case: when there aren't too many strings with identical prefixes that are found in another string O(n * m) time | O(n * m) space - where n is the number of strings and m is the length of the longest string -------- See the Notes section in the Explanation tab for more info.
