""" 

##### Find Three Largest Numbers #####

Write a function that takes in an array of at least three integers and, without 
sorting the input array, returns a sorted array of the three largest integers in the 
input array.

The function should return duplicate integers if necessary; for example, it should 
return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].


##### Sample Input #####
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

##### Sample Output #####
[18, 141, 541]


##### Hints #####

Hint 1
Can you keep track of the three largest numbers in an array as you traverse 
the input array?

Hint 2
Following the suggestion in Hint #1, try traversing the input array and 
updating the three largest numbers if necessary by shifting them accordingly.

Hint 3
Can you implement this algorithm iteratively?  Are there any advantages to 
doing so?

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the length of the input array

"""





##### Solution 1 #####
# O(n) time | O(1) space
def findThreeLargestNumbers(array):
  threeLargest = [None, None, None]
  for num in array:
    updateLargest(threeLargest, num)
  return threeLargest


def updateLargest(threeLargest, num):
  if threeLargest[2] is None or num > threeLargest[2]:
    shiftAndUpdate(threeLargest, num, 2)
  elif threeLargest[1] is None or num > threeLargest[1]:
    shiftAndUpdate(threeLargest, num, 1)
  elif threeLargest[0] is None or num > threeLargest[0]:
    shiftAndUpdate(threeLargest, num, 0)


def shiftAndUpdate(array, num, idx):
  for i in range(idx + 1):
    if i == idx:
      array[i] = num
    else:
      array[i] = array[i + 1]  
