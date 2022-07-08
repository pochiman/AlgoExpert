""" 

##### Merge Sorted Arrays #####

Write a function that takes in a non-empty list of non-empty sorted arrays of 
integers and returns a merged list of all of those arrays.

The integers in the merged list should be in sorted order.


##### Sample Input #####
arrays = [
  [1, 5, 9, 21], 
  [-1, 0], 
  [-124, 81, 121], 
  [3, 6, 12, 20, 150], 
]

##### Sample Output #####
[-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150]


##### Hints #####

Hint 1
If you were given just two sorted lists of numbers in real life, what steps 
would you take to merge them into a single sorted list? Apply the same 
process to k sorted lists. 

Hint 2
The first element in each array is the smallest element in the respective 
array; to find the first element to add to the final sorted list, pick the 
smallest integer out of all of the smallest elements. Once you've found the 
smallest integer, move one position forward in the array that it came from 
and continue applying this logic until you run out of elements.

Hint 3
The approach described in Hint #2 involves repeatedly finding the smallest 
of k elements, since there are k arrays. Doing so can be naively implemented 
using a simple loop through the k relevant elements, which results in an O(k)-
time operation. Can you speed up this operation by using a specific data 
structure that lends itself to quickly finding the minimum value in a set of 
values?

Hint 4
Follow the approach described in Hint #2, using a Min Heap to store the k 
smallest elements at any given point in your algorithm.

Optimal Space & Time Complexity
O(nlog(k) + k) time | O(n + k) space - where n is the total number of 
array elements and k is the number of arrays

"""





##### Solution 1 #####
# O(nk) time | O(n + k) space - where n is the total
# number of array elements and k is the number of arrays
def mergeSortedArrays(arrays):
  sortedList = []
  elementIdxs = [0 for array in arrays]  
  while True:
    smallestItems = []
    for arrayIdx in range(len(arrays)):
      relevantArray = arrays[arrayIdx]    
      elementIdx = elementIdxs[arrayIdx]
      if elementIdx == len(relevantArray): 
        continue
      smallestItems.append({"arrayIdx": arrayIdx, "num": relevantArray[elementIdx]})  
    if len(smallestItems) == 0:
      break
    nextItem = getMinValue(smallestItems)    
    sortedList.append(nextItem["num"])
    elementIdxs[nextItem["arrayIdx"]] += 1
  return sortedList


def getMinValue(items):
  minValueIdx = 0
  for i in range(1, len(items)):
    if items[i]["num"] < items[minValueIdx]["num"]:
      minValueIdx = i
  return items[minValueIdx]





##### Solution 2 #####
# O(nlog(k) + k) time | O(n + k) space - where n is the total
# number of array elements and k is the number of arrays
def mergeSortedArrays(arrays):
  sortedList = []
  smallestItems = []
  for arrayIdx in range(len(arrays)):
    smallestItems.append({"arrayIdx": arrayIdx, "elementIdx": 0, "num": arrays[arrayIdx][0]})  
  minHeap = MinHeap(smallestItems)
  while not minHeap.isEmpty():
    smallestItem = minHeap.remove()
    arrayIdx, elementIdx, num = smallestItem["arrayIdx"], smallestItem["elementIdx"], smallestItem["num"]  
    sortedList.append(num)
    if elementIdx == len(arrays[arrayIdx]) - 1:
      continue
    minHeap.insert({"arrayIdx": arrayIdx, "elementIdx": elementIdx + 1, "num": arrays[arrayIdx][elementIdx + 1]}) 
  return sortedList


class MinHeap:
  def __init__(self, array):
    self.heap = self.buildHeap(array)

  def isEmpty(self):
    return len(self.heap) == 0

  def buildHeap(self, array):
    firstParentIdx = (len(array) - 2) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
      self.siftDown(currentIdx, len(array) - 1, array)  
    return array

  def siftDown(self, currentIdx, endIdx, heap):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
      childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1    
      if childTwoIdx != -1 and heap[childTwoIdx]["num"] < heap[childOneIdx]["num"]:
        idxToSwap = childTwoIdx
      else:
        idxToSwap = childOneIdx
      if heap[idxToSwap]["num"] < heap[currentIdx]["num"]:
        self.swap(currentIdx, idxToSwap, heap)
        currentIdx = idxToSwap
        childOneIdx = currentIdx * 2 + 1
      else:    
        return

  def siftUp(self, currentIdx, heap):
    parentIdx = (currentIdx - 1) // 2
    while currentIdx > 0 and heap[currentIdx]["num"] < heap[parentIdx]["num"]:  
      self.swap(currentIdx, parentIdx, heap)
      currentIdx = parentIdx
      parentIdx = (currentIdx - 1) // 2

  def remove(self):
    self.swap(0, len(self.heap) - 1, self.heap)
    valueToRemove = self.heap.pop()
    self.siftDown(0, len(self.heap) - 1, self.heap)
    return valueToRemove
      
  def insert(self, value):
    self.heap.append(value)
    self.siftUp(len(self.heap) - 1, self.heap)  

  def swap(self, i, j, heap):
    heap[i], heap[j] = heap[j], heap[i]
