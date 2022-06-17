""" 

##### Array Of Products #####

Write a function that takes in a non-empty array of integers and returns an array 
of the same length, where each element in the output array is equal to the 
product of every other number in the input array.

In other words, the value at output[i] is equal to the product of every number 
in the input array other than input[i].

Note that you're expected to solve this problem without using division.


##### Sample Input #####
array = [5, 1, 4, 2]

##### Sample Output #####
[8, 40, 10, 20]
// 8 is equal to 1 x 4 x 2
// 40 is equal to 5 x 4 x 2
// 10 is equal to 5 x 1 x 2
// 20 is equal to 5 x 1 x 4


##### Hints #####

Hint 1
Think about the most naive approach to solving this problem.  How can we 
do exactly what the problem wants us to do without focusing at all on time 
and space complexity?

Hint 2
Understand how output[i] is being calculated.  How can we calculate the 
product of every element other than the one at the current index?  Can we 
do this with just one loop through the input array, or do we have to do 
multiple loops?

Hint 3
For each index in the input array, try calculating the product of every 
element to the left and the product of every element to the right.  You can do 
this with two loops through the array: one from left to right and one from 
right to left.  How can these products help us?

Optimal Space & Time Complexity
O(n) time | O(n) space - where n is the length of the input array

"""





##### Solution 1 #####
# O(n^2) time | O(n) space - where n is the length of the input array
def arrayOfProducts(array):
  products = [1 for _ in range(len(array))]

  for i in range(len(array)):
    runningProduct = 1
    for j in range(len(array)):
      if i != j:
        runningProduct *= array[j]
    products[i] = runningProduct

  return products      





##### Solution 2 #####
# O(n) time | O(n) space - where n is the length of the input array
def arrayOfProducts(array):
  products = [1 for _ in range(len(array))]
  leftProducts = [1 for _ in range(len(array))]
  rightProducts = [1 for _ in range(len(array))]

  leftRunningProduct = 1
  for i in range(len(array)):
    leftProducts[i] = leftRunningProduct
    leftRunningProduct *= array[i]

  rightRunningProduct = 1
  for i in reversed(range(len(array))):
    rightProducts[i] = rightRunningProduct
    rightRunningProduct *= array[i]

  for i in range(len(array)):
    products[i] = leftProducts[i] * rightProducts[i]

  return products





##### Solution 3 #####
# O(n) time | O(n) space - where n is the length of the input array
def arrayOfProducts(array):
  products = [1 for _ in range(len(array))]

  leftRunningProduct = 1
  for i in range(len(array)):
    products[i] = leftRunningProduct
    leftRunningProduct *= array[i]

  rightRunningProduct = 1
  for i in reversed(range(len(array))):
    products[i] *= rightRunningProduct
    rightRunningProduct *= array[i]

  return products
