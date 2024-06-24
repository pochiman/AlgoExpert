"""

[ Difficulty: Very Hard ]
[ Category: Searching ]

##### Median Of Two Sorted Arrays #####

You're given two sorted arrays of integers arrayOne and arrayTwo. Write a function 
that returns the median of these arrays.

You can assume both arrays have at least one value. However, they could be of 
different lengths. If the median is a decimal value, it should not be rounded 
(beyond the inevitable rounding of floating point math).


##### Sample Input #####
arrayOne = [1, 3, 4, 5]
arrayTwo = [2, 3, 6, 7]

##### Sample Output #####
3.5 // The combined array is [1, 2, 3, 3, 4, 5, 6, 7]


##### Hints #####

Hint 1
The median value of the combined array will always have the same number of 
integers to its left and its right. Therefore the goal is to find the element 
at the middle index (or the average of the middle indices if the array has an 
even length). 

Hint 2
A naive approach would be to iterate through both arrays simultaneously, with 
each iteration moving forward in the array with the lower current value until 
passing half of the total values. This solution would have a linear time 
complexity, but can you find a way to improve it to be logarithmic?

Hint 3
Try considering just the smaller of the two arrays. Start with the median of 
that array, and temporarily assume that all of the values to its left of that 
median are to the left of the overall median, and all of the values to the 
right are to the right of the overall median. Assuming this is correct, could 
you also place a dividing point in the larger array, to ensure there are the 
correct number of values on either side of the combined median? And now can 
you find a way to do a binary search with just the smaller array to find the 
actual correct dividing point?

Hint 4
The value at the dividing point in arrayOne must be smaller than the value at 
the index after the dividing point of arrayTwo. The value at the dividing point 
in arrayTwo must be smaller than the value at the index after the dividing 
point of arrayOne. If either of these conditions are not met, then the binary 
search must continue to either include more or less elements from that smaller 
array.

Optimal Space & Time Complexity
O(log(min(n, m)) time | O(1) space - where n is the length of arrayOne and m 
is the length of arrayTwo.

"""





##### Solution 1 #####
# O(n + m) time | O(1) space - where n is the length of arrayOne and
# m is the length of arrayTwo
def medianOfTwoSortedArrays(arrayOne, arrayTwo):
    idxOne, idxTwo = 0, 0
    middleIdx = (len(arrayOne) + len(arrayTwo) - 1) // 2

    while idxOne + idxTwo < middleIdx:
        if idxOne >= len(arrayOne):
            idxTwo += 1
        elif idxTwo >= len(arrayTwo):
            idxOne += 1
        elif arrayOne[idxOne] < arrayTwo[idxTwo]:
            idxOne += 1
        else:
            idxTwo += 1

    if (len(arrayOne) + len(arrayTwo)) % 2 == 0:
        areBothValuesArrayOne = idxTwo >= len(arrayTwo) or (
            idxOne + 1 < len(arrayOne) and arrayTwo[idxTwo] > arrayOne[idxOne + 1]
        )
        areBothValuesArrayTwo = idxOne >= len(arrayOne) or (
            idxTwo + 1 < len(arrayTwo) and arrayOne[idxOne] > arrayTwo[idxTwo + 1]
        )

        valueOne = arrayOne[idxOne + 1] if areBothValuesArrayOne else arrayTwo[idxTwo]
        valueTwo = arrayTwo[idxTwo + 1] if areBothValuesArrayTwo else arrayOne[idxOne]
        return (valueOne + valueTwo) / 2

    valueOne = arrayOne[idxOne] if idxOne < len(arrayOne) else float("inf")
    valueTwo = arrayTwo[idxTwo] if idxTwo < len(arrayTwo) else float("inf")
    return min(valueOne, valueTwo)





# Solution 2
# O(log(min(n, m)) time | O(1) space - where n is the length of arrayOne and
# m is the length of arrayTwo
def medianOfTwoSortedArrays(arrayOne, arrayTwo):
    smallArray = arrayOne if len(arrayOne) <= len(arrayTwo) else arrayTwo
    bigArray = arrayOne if len(arrayOne) > len(arrayTwo) else arrayTwo

    leftIdx = 0
    rightIdx = len(smallArray) - 1
    mergedLeftIdx = (len(smallArray) + len(bigArray) - 1) // 2

    while True:
        smallPartitionIdx = (leftIdx + rightIdx) // 2
        bigPartitionIdx = mergedLeftIdx - smallPartitionIdx - 1

        smallMaxLeftValue = (
            smallArray[smallPartitionIdx] if smallPartitionIdx >= 0 else float("-inf")
        )
        smallMinRightValue = (
            smallArray[smallPartitionIdx + 1]
            if smallPartitionIdx + 1 < len(smallArray)
            else float("inf")
        )
        bigMaxLeftValue = bigArray[bigPartitionIdx] if bigPartitionIdx >= 0 else float("-inf")
        bigMinRightValue = (
            bigArray[bigPartitionIdx + 1] if bigPartitionIdx + 1 < len(bigArray) else float("inf")
        )

        if smallMaxLeftValue > bigMinRightValue:
            rightIdx = smallPartitionIdx - 1
        elif bigMaxLeftValue > smallMinRightValue:
            leftIdx = smallPartitionIdx + 1
        else:
            if (len(smallArray) + len(bigArray)) % 2 == 0:
                return (
                    max(smallMaxLeftValue, bigMaxLeftValue)
                    + min(smallMinRightValue, bigMinRightValue)
                ) / 2
            return max(smallMaxLeftValue, bigMaxLeftValue)
