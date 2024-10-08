# 11 - Strings

Not a standalone data structure per se, strings are generally considered to be 
a data type that behaves like a data structure.

Nonetheless, they do possess a few interesting characteristics that earn them 
a dedicated video here in our course. Let’s dive in!

# Key Term

# [String]

  One of the fundamental data types in Computer Science, strings are stored in
  `memory` as `arrays` of integers, where each character in a given string is 
  mapped to an integer via some character-encoding standard like `ASCII`.

  Strings behave much like normal arrays, with the main distinction being that,
  in most programming languages (C++ is a notable exception), strings are
  `immutable`, meaning that they can't be edited after creation. This also
  means that simple operations like appending a character to a string are more
  expensive than they might appear.

  The canonical example of an operation that's deceptively expensive due to
  string immutability is the following:
  
    string = "this is a string"
    newString = ""

    for character in string:
        newString += character

  The operation above has a time complexity of `O(n²)` where n is the length of 
  `string`, because each addition of a character to `newString` creates an entirely 
  new string and is itself an `O(n)` operation. Therefore, n O(n) operations are 
  performed, leading to an O(n²) time-complexity operation overall.
