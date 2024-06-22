""" 

[ Difficulty: Hard ]
[ Category: Searching ]

##### Search For Range #####

Write a function that takes in a sorted array of integers as well as a target integer. 
The function should use a variation of the Binary Search algorithm to find a range 
of indices in between which the target number is contained in the array and should 
return this range in the form of an array.

The first number in the output array should represent the first index at which the 
target number is located, while the second number should represent the last index 
at which the target number is located. The function should return [-1, -1] if the 
integer isn't contained in the array.

If you're unfamiliar with Binary Search, we recommend watching the Conceptual Overview 
section of the Binary Search question's video explanation before starting to code.


##### Sample Input #####
array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
target = 45

##### Sample Output #####
[4, 9]


##### Hints #####

Hint 1
The Binary Search algorithm involves a left pointer and a right pointer and 
using those pointers to find the middle number in an array in an effort to 
find a target number. Unlike with normal Binary Search however, here you 
cannot simply find the middle number of the array, compare it to the target, 
and stop once you find it because you are looking for a range rather than a 
single number. Instead, realize that whenever you find the middle number in 
the array, the following two scenarios are possible: either the middle number 
is not equal to the target number, in which case you must proceed with normal 
Binary Search, or the middle number is equal to the target number, in which 
case you must figure out if this middle number is an extremity of the range 
or not.

Hint 2
Try applying an altered version of Binary Search twice: once to find the left 
extremity of the range and once to find the right extremity of the range. How 
can you accomplish this? What are the time complexity implications of this 
approach?

Hint 3
Can you implement this algorithm iteratively? Are there any advantages to 
doing so?

Optimal Space & Time Complexity
O(log(n)) time | O(1) space - where n is the length of the input array

"""





##### Solution 1 #####
# O(log(n)) time | O(log(n)) space
def searchForRange(array, target):
    finalRange = [-1, -1]
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, True)  
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, False)
    return finalRange


def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
    if left > right:
        return
    mid = (left + right) // 2
    if array[mid] < target:
        alteredBinarySearch(array, target, mid + 1, right, finalRange, goLeft)
    elif array[mid] > target:
        alteredBinarySearch(array, target, left, mid - 1, finalRange, goLeft)
    else:
        if goLeft:
            if mid == 0 or array[mid - 1] != target:
                finalRange[0] = mid
            else:
                alteredBinarySearch(array, target, left, mid - 1, finalRange, goLeft)
        else:
            if mid == len(array) - 1 or array[mid + 1] != target:
                finalRange[1] = mid
            else:
                alteredBinarySearch(array, target, mid + 1, right, finalRange, goLeft)





##### Solution 2 #####
# O(log(n)) time | O(1) space
def searchForRange(array, target):
    finalRange = [-1, -1]
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, True)  
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, False)
    return finalRange  


def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1 
        else:
            if goLeft:
                if mid == 0 or array[mid - 1] != target:
                    finalRange[0] = mid
                    return  
                else:
                    right = mid - 1
            else:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    finalRange[1] = mid
                    return  
                else:
                    left = mid + 1
