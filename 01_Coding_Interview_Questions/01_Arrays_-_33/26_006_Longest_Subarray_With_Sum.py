""" 

[ Difficulty: Hard ]
[ Category: Arrays ]

##### Longest Subarray With Sum #####

Write a function that takes in a non-empty array of non-negative integers and a 
non-negative integer representing a target sum. The function should find the longest 
subarray where the values collectively sum up to equal the target sum. Return an 
array containing the starting index and ending index of this subarray, both inclusive.

If there is no subarray that sums up to the target sum, the function should return 
an empty array. You can assume that the given inputs will only ever have one answer.


##### Sample Input #####
array = [1, 2, 3, 4, 3, 3, 1, 2, 1, 2]
targetSum = 10

##### Sample Output #####
[4, 8] // The longest subarray that sums to 10 starts at index 4 and ends at index 8


##### Hints #####

Hint 1
Using intuition you can develop a brute force approach. If you are trying to find 
the longest subarray that sums to equal the target sum, then look at every possible 
subarray. Calculate the sum of each subarray, and when the sum is equal to the 
target sum, check the length against the current maximum.

Hint 2
Since the array contains only non-negative numbers, once a subarray sum is greater 
than the target sum, there is no possible way adding more numbers to that subarray 
will get its sum to equal the target sum. Can you use this information to optimize 
the solution?

Hint 3
Looking at every possible subarray is very time consuming. However, you can use a 
sliding window approach to improve the time complexity. Think about how a sliding 
window might work in this case. You should look at different subarrays while you 
traverse the array. How might you update a sliding window if you are looking for 
subarrays with a sum that is equal to the target sum?

Hint 4

Add elements to the sliding window when the current subarray sum is less than the 
target sum,and remove elements when the current subarray sum is greater than the 
target sum. When you finda current subarray sum in the sliding window that is equal 
to the target sum, then you can check and see if you found a new longest subarray. 
If that is the case then update the result, otherwise continue traversing.

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the length of the input array

"""





##### Solution 1 #####
# O(n^2) time | O(1) space - where n is the length of the input array
def longestSubarrayWithSum(array, targetSum):
    indices = []

    for startingIndex in range(len(array)):
        currentSubarraySum = 0

        for endingIndex in range(startingIndex, len(array)):
            currentSubarraySum += array[endingIndex]

            if currentSubarraySum == targetSum:
                if len(indices) == 0 or indices[1] - indices[0] < endingIndex - startingIndex:
                    indices = [startingIndex, endingIndex]

    return indices





##### Solution 2 #####
# O(n) time | O(1) space - where n is the length of the input array
def longestSubarrayWithSum(array, targetSum):
    indices = []

    currentSubarraySum = 0
    startingIndex = 0
    endingIndex = 0

    while endingIndex < len(array):
        currentSubarraySum += array[endingIndex]
        while startingIndex < endingIndex and currentSubarraySum > targetSum:
            currentSubarraySum -= array[startingIndex]
            startingIndex += 1

        if currentSubarraySum == targetSum:
            if len(indices) == 0 or indices[1] - indices[0] < endingIndex - startingIndex:
                indices = [startingIndex, endingIndex]

        endingIndex += 1

    return indices
