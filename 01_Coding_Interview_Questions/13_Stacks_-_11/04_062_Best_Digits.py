"""

[ Difficulty: Medium ]
[ Category: Stacks ]

##### Best Digits #####

Write a function that takes a positive integer represented as a string number 
and an integer numDigits. Remove numDigits from the string so that the number 
represented by the string is as large as possible afterwards.

Note that the order of the remaining digits cannot be changed. You can assume 
numDigits will always be less than the length of number and greater than or 
equal to 0.


##### Sample Input #####
number = "462839"
numDigits = 2

##### Sample Output #####
"6839" // remove digits 4 and 2

##### Hints #####

Hint 1
If we want the number to be as large as possible then which digits would we want 
to remove? Consider the importance of place values. For example if we're given 
number = "191" and numDigits = 1 then which 1 would we remove?

Hint 2
It's most important that the largest place values have the highest value digits. 
If you traverse the string from left to right then you will be traversing the 
place values in order of importance. If you still have digits to remove then you 
need to remove smaller digits in higher place values. The question then becomes 
how can you know what comes later on in the string? If you want to solve this 
problem in linear time what data structure might help you in this situation?

Hint 3
Use a stack to push digits onto while traversing the string from left to right. 
That way top of the stack will always have the digit in the last highest place 
value. Compare the top of the stack to the current digit and if the current digit 
is greater than the top of the stack, then pop from the stack. Utilizing a stack 
allows you to replace small digits with largest digits that come later in the 
string because you can pop off of the stack in order of importance. You will 
need to build a string to return from the final stack.

Optimal Space & Time Complexity
O(n) time | O(n) space - where n is the length of the input string

"""





##### Solution 1 #####
# O(n) time | O(n) space - where n is the length of the input string
def bestDigits(number, numDigits):
    stack = []

    for digit in number:
        while numDigits > 0 and len(stack) > 0 and digit > stack[len(stack) - 1]:
            numDigits -= 1
            stack.pop()

        stack.append(digit)

    while numDigits > 0:
        numDigits -= 1
        stack.pop()

    return "".join(stack)
