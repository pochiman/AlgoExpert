""" 

##### Max Subset Sum No Adjacent #####

Write a function that takes in an array of positive integers and returns the 
maximum sum of non-adjacent elements in the array.

If the input array is empty, the function should return 0.


##### Sample Input #####
array = [75, 105, 120, 75, 90, 135]

##### Sample Output #####
330 // 75 + 120 + 135


##### Hints #####

Hint 1
Try building an array of the same length as the input array. At each index in 
this new array, store the maximum sum that can be generated using no adjacent 
numbers located between index 0 and the current index.

Hint 2
Can you come up with a formula that relates the max sum at index i to the 
max sums at indices i - 1 and i - 2?

Hint 3
Do you really need to store the entire array mentioned in Hint #1, or can you 
somehow store just the max sums that you need at any point in time?

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the length of the input array

"""





##### Solution 1 #####
# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
  if not len(array):
    return 0
  elif len(array) == 1:
    return array[0]
  maxSums = array[:]
  maxSums[1] = max(array[0], array[1])
  for i in range(2, len(array)):
    maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])
  return maxSums[-1]





##### Solution 2 #####
# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
  if not len(array):
    return 0
  elif len(array) == 1:
    return array[0]
  second = array[0]
  first = max(array[0], array[1])
  for i in range(2, len(array)):
    current = max(first, second + array[i])
    second = first
    first = current
  return first
