""" 

[ Difficulty: Medium ]
[ Category: Arrays ]

##### Majority Element #####

Write a function that takes in a non-empty, unordered array of positive integers 
and returns the array'smajority element without sorting the array and without 
using more than constant space.

An array's majority element is an element of the array that appears in over half 
of its indices. Note that themost common element of an array (the element that 
appears the most times in the array) isn't necessarily the array's majority 
element; for example, the arrays [3, 2, 2, 1] and [3, 4, 2, 2, 1] both have 2 as 
their most common element, yet neither of these arrays have a majority element, 
because neither 2 nor any other element appears in over half of the respective 
arrays' indices.

You can assume that the input array will always have a majority element.


##### Sample Input #####
array = [1, 2, 3, 2, 2, 1, 2]

##### Sample Output #####
2 // 2 occurs in 4/7 array indices, making it the majority element


##### Hints #####

Hint 1
If the array were sorted, the middle element would have to be the majority element. 
However, this does not produce an optimal algorithm. Can you find a solution that 
does not require sorting?

Hint 2
Try to first guess that the first element in the array is the majority element. 
From here, iterate through the array, incrementing a counter for each copy of 
that candidate element that is found, and decrementing the counter for each other 
element that is found. If the counter ends greater than 1, then that element must 
be the majority element. Can you generalize this idea to work for cases where the 
majority element isn't the first element?

Hint 3
Instead of iterating all the way to the end of the array, try stopping once the 
counter hits 0. At this point, the guessed majority element must not be the 
majority element in the subarray of the array that you have already looked at. 
Moreover, the actual majority element must still be the majority element in the 
remaining subarray of the array, since at most half of the values in the first 
subarray were the majority element (otherwise it would have had a negative count). 
With this intuition, you can just repeat this process, only using the remaining 
subarray.

Hint 4
This problem can also be solved using bit manipulation. Consider each of the bits 
used to store an integer. For each of these bits, if over half of the elements in 
the array have the bit set, then that bit must be set in the majority element as 
well. Doing this for each bit can determine which bits are set in the majority 
element, and thus what the majority element is.

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the number of elements in the array

"""





##### Solution 1 #####
# O(n) time | O(1) space - where n is the number of elements in the array
def majorityElement(array):
    count = 0
    answer = None

    for value in array:
        if count == 0:
            answer = value

        if value == answer:
            count += 1
        else:
            count -= 1

    return answer         





##### Solution 2 #####
# O(n) time | O(1) space - where n is the number of elements in the array
def majorityElement(array):
    answer = 0

    for currentBit in range(32):
        currentBitValue = 1 << currentBit
        onesCount = 0

        for num in array:
            if (num & currentBitValue) != 0:
                onesCount += 1

        if onesCount > len(array) / 2:
            answer += currentBitValue

    return answer
