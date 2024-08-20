# 6 - Logarithm

That scary-looking word you know you should understand but just really...don’t? Yeah, that one. It’s time to make it your best friend.

Warning: a logarithmless way of life will seem inconceivable after watching this video.

# Key Term

# [Logarithm]

A mathematical concept that's widely used in Computer Science and that's defined by the following equation:

`logₐ(x) = y` if and only if `aʸ = x`

In the context of coding interviews, the logarithm is used to describe the complexity analysis of algorithms, and its usage always implies a logarithm of base `2`. In other words, the logarithm used in the context of coding interviews is defined by the following equation:

`log(n) = y` if and only if `2ʸ = n`

In plain English, if an algorithm has a logarithmic time complexity (`O(log(n))`, where n is the size of the input), then whenever the algorithm's input doubles in size (i.e., whenever 
`n` doubles), the number of operations needed to complete the algorithm only increases by one unit. Conversely, an algorithm with a linear time complexity would see its number of operations double if its input size doubled.

As an example, a linear-time-complexity algorithm with an input of size 1,000 might take roughly 1,000 operations to complete, whereas a logarithmic-time-complexity algorithm with the same input would take roughly 10 operations to complete, since `2¹⁰ ~= 1,000`.
