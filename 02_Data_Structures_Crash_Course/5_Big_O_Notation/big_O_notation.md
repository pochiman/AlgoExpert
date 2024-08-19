# 5 - Big O Notation

The speed and memory usage of an algorithm aren't necessarily fixed; they might change depending on the input. So how do we express the performance of an algorithm then?

Enter Big O Notation, a powerful tool that allows us to generalize the space-time complexity of an algorithm as a function of its input size.

# Prerequisite

# [Time_Complexity]
A measure of how fast an algorithm runs, time complexity is a central concept in the field of algorithms and in coding interviews.

It's expressed using `Big O` notation.

# [Space_Complexity]
A measure of how much auxiliary memory an algorithm takes up, space complexity is a central concept in the field of algorithms and in coding interviews.

It's expressed using `Big O` notation.

# Key Term

# [Big_O_Notation]

  The notation used to describe the `time complexity` and `space complexity` of algorithms.

  Variables used in Big O notation denote the sizes of inputs to algorithms. For
  example, `O(n)` might be the time complexity of an algorithm that
  traverses through an array of length `n`; similarly,
  `O(n + m)` might be the time complexity of an algorithm that traverses
  through an array of length `n` and through a string of length `m`.

  The following are examples of common complexities and their Big O notations,
  ordered from fastest to slowest:

  • `Constant`: O(1)
  • `Logarithmic`: O(log(n))
  • `Linear`: O(n)
  • `Log-linear`: O(nlog(n))
  • `Quadratic`: O(n²)
  • `Cubic`: O(n³)
  • `Exponential`: O(2ⁿ)
  • `Factorial`: O(n!)

  Note that in the context of coding interviews, Big O notation is usually
  understood to describe the `worst-case` complexity of an algorithm, even though the worst-case complexity might differ from the `average-case` complexity.

  For example, some sorting algorithms have different time complexities
  depending on the layout of elements in their input array. In rare cases, their
  time complexity will be much worse than in more common cases. Similarly, an
  algorithm that takes in a string and performs special operations on uppercase
  characters might have a different time complexity when run on an input string
  of only uppercase characters vs. on an input string with just a few uppercase
  characters.

  Thus, when describing the time complexity of an algorithm, it can sometimes be
  helpful to specify whether the time complexity refers to the average case or
  to the worst case (e.g., "this algorithm runs in O(nlog(n)) time on average
  and in O(n²) time in the worse case").
