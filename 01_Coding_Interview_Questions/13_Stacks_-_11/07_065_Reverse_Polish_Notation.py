"""

[ Difficulty: Medium ]
[ Category: Stacks ]

##### Reverse Polish Notation #####

You're given a list of string tokens representing a mathematical expression using 
Reverse Polish Notation. Reverse Polish Notation is a notation where operators come 
after operands, instead of between them. For example, 2 4 + would evaluate to 6.

Parenthesis are always implicit in Reverse Polish Notation, meaning an expression 
is evaluated from left to right. All of the operators for this problem take two 
operands, which will always be the two values immediately preceding the operator. 
For example, 18 4 - 7 / would evaluate to ((18 - 4) / 7) or 2.

Write a function that takes this list of tokens and returns the result. Your 
function should support four operators: +, -, *, and / for addition, subtraction, 
multiplication, and division respectively.

Division should always be treated as integer division, rounding towards zero. For 
example, 3 / 2 evaluates to 1 and -3 / 2 evaluates to -1. You can assume the input 
will always be valid Reverse Polish Notation, and it will always result in a valid 
number. Your code should not edit this input list.


##### Sample Input #####
tokens = ["50", "3", "17", "+", "2", "-", "/"]

##### Sample Output #####
2 // (50 / ((3 + 17) -2)))

##### Hints #####

Hint 1
Operators always operate on the two previous values. Is there a data structure 
that would assist in finding the two most recent values? 

Hint 2
It can be helpful to create a stack that contains all of the previously found 
or calculated values.

Optimal Space & Time Complexity
O(n) time | O(n) space - where n is the number of tokens

"""





##### Solution 1 #####
# O(n) time | O(n) space - where n is the number of tokens
def reversePolishNotation(tokens):
    stack = []

    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            firstNum = stack.pop()
            stack.append(stack.pop() - firstNum)
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "/":
            firstNum = stack.pop()
            stack.append(int(stack.pop() / firstNum))
        else:
            stack.append(int(token))

    return stack.pop()