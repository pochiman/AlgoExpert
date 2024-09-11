# Words In Phone Number

# [Difficulty:_Hard]
# [Category:_Tries]

  If you open the keypad of your mobile phone, it'll likely look like this:

   ----- ----- -----
  |     |     |     |
  |  1  |  2  |  3  |
  |     | abc | def |
   ----- ----- -----
  |     |     |     |
  |  4  |  5  |  6  |
  | ghi | jkl | mno |
   ----- ----- -----
  |     |     |     |
  |  7  |  8  |  9  |
  | pqrs| tuv | wxyz|
   ----- ----- -----
        |     |
        |  0  |
        |     |
         -----
  Almost every digit is associated with some letters in the alphabet; this
  allows certain phone numbers to spell out actual words. For example, the phone
  number `2536368` can be written as `clement`; similarly,
  the phone number `2686463` can be written as
  `antoine` or as `ant6463`.

  It's important to note that a phone number doesn't represent a single sequence
  of letters, but rather multiple combinations of letters. For instance, the
  digit `2` can represent three different letters (a, b, and c).

  You're given a stringified phone number of any non-zero length and a non-empty
  list of lowercase english-alphabet words.

  Write a function that returns the list of words that can be found in the phone
  number. The final words don't need to be in any particular order.

  Note that you should rely on the keypad illustrated above for digit-letter
  associations.

# [Sample_Input]

  phoneNumber = "3662277"
  words = ["foo", "bar", "baz", "foobar", "emo", "cap", "car", "cat"]

# [Sample_Output]

  ["bar", "cap", "car", "emo", "foo", "foobar"]
  // The words could be ordered differently.

# Hints

# [Hint_1]

  You can solve this question optimally by using a trie.

# [Hint_2]

  You can either insert all of the words in a normal trie or the phone number in a suffix trie. If you insert all of the words in a normal trie, you'll have to check if any of the many string combinations that can be formed in the phone number are contained in the trie. If you insert the phone number in a suffix trie, you'll just have to check if the numbers that the words map to (one number per word) are contained in the trie.

# [Optimal_Space_&_Time_Complexity]

  O(n^2 + m * w) time | O(n^2 + m * w) space - where n is the length of the phone number, m is the number of words, and w is the length of the longest word
