# 4 - Memory

The bedrock of all data structures, memory is the underlying concept that you absolutely need to know in order to understand why data structures work the way they do.

Bits and bytes may keep me up all night,
But memory will never ail me!

# Key Terms

# [Bit]
Short for `binary digit`, a bit is a fundamental unit of information in Computer Science that represents a state with one of two values, typically `0` and `1`.

Any data stored in a computer is, at the most basic level, represented in bits.

# [Byte]
A group of eight `bits`. For example, `01101000` is a byte.

A single byte can represent up to `256` data values (`2⁸`).

Since a `binary number` is a number expressed with only two symbols, like `0` and `1`, 
a byte can effectively represent all of the numbers between 0 and 255, inclusive, in 
binary format.

The following bytes represent the numbers 1, 2, 3, and 4 in binary format.

  • 1: 00000001
  • 2: 00000010
  • 3: 00000011
  • 4: 00000100

# [Fixed-Width_Integer]
An integer represented by a fixed amount of `bits`. For example, a `32-bit integer` 
is an integer represented by 32 bits (4 bytes), and a `64-bit integer` is an integer 
represented by 64 bits (8 bytes).

The following is the 32-bit representation of the number 1, with clearly separated bytes:

  00000000 00000000 00000000 00000001
  
The following is the 64-bit representation of the number 10, with clearly separated bytes:

  00000000 00000000 00000000 00000000 00000000 00000000 00000000 00001010

  Regardless of how large an integer is, its fixed-width-integer representation
  is, by definition, made up of a constant number of bits.

  It follows that, regardless of how large an integer is, an operation performed
  on its fixed-width-integer representation consists of a constant number of bit
  manipulations, since the integer is made up of a fixed number of bits.

# [Memory]

  Broadly speaking, memory is the foundational layer of computing, where all
  data is stored.

  In the context of coding interviews, it's important to note the following
  points:

  • Data stored in memory is stored in bytes and, by extension, bits.

  • Bytes in memory can "point" to other bytes in memory, so as to store
    references to other data.
  
  • The amount of memory that a machine has is bounded, making it valuable to
    limit how much memory an algorithm takes up.
  
  • Accessing a byte or a fixed number of bytes (like 4 bytes or 8 bytes in the
    case of `32-bit` and `64-bit integers`) is an elementary operation, which can 
    be loosely treated as a single unit of operational work.
