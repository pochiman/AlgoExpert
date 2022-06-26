""" 

##### Laptop Rentals #####

You're given a list of time intervals during which students at a school need a 
laptop.  These time intervals are represented by pairs of integers [start, end], 
where 0 <= start < end.  However, start and end don't represent real times; 
therefore, they may be greater than 24.

No two students can use a laptop at the same time, but immediately after a student 
is done using a laptop, another student can use that same laptop.  For example, if 
one student rents a laptop during the time interval [0, 2], another student can 
rent the same laptop during any time interval starting with 2.

Write a function that returns the minimum number of laptops that the school needs to 
rent such that all students will always have access to a laptop when they need one.


##### Sample Input #####
times = 
[
  [0, 2], 
  [1, 4], 
  [4, 6], 
  [0, 4], 
  [7, 8], 
  [9, 11], 
  [3, 10], 
]

##### Sample Output #####
3


##### Hints #####

Hint 1
There are many different ways to solve this problem, but only a few of them 
run in the optimal time.  Can you come up with an algorithm that solves this 
problem in O(nlog(n)) time?

Hint 2
Suppose that you're given two time intervals: [s1, e1] and [s2, e2], where 
s1 < s2.  If e1 <= s2, then the second time interval can use the same laptop 
as the first time interval.

One method to solve this problem with an optimal time complexity is to use 
a Min Heap.  If you loop through time intervals that have been sorted by 
their start times and keep track of the smallest end time of time intervals 
for laptops that have already been rented out, you can determine how many 
laptops are required.  Use the Min Heap to efficiently determine if any 
previous rental time intervals have ended as you loop through all the time 
intervals.  If a rental time interval is done and another one starts after 
it, no extra laptop is required.

Hint 3
Another way to efficiently solve this problem is to realize that we don't 
need to know what start time corresponds with what end time.  So long as 
we know all start times and all end times, we can determine the number of 
laptops required.

Hint 4
Start by creating two arrays--one for start times and one for end times--
and sort them both in ascending order.  We can simply loop through the start 
times and end times at the same time and compare the current start time to 
the current end time.  If the current start time is greater than the current 
end time, then that means a laptop that was previously used is no longer being 
used and can be given to the student renting a laptop at this starting time.  
Thus, we can increment both our start-time and end-time pointers and continue 
without needing an additional laptop.  If the current start time is smaller 
than the current end time, then another rental has started before a previous 
rental has ended, and we thus require another laptop, so we increment the 
start pointer and a variable keeping track of the number of laptops required.  
See the Conceptual Overview section of this question's video explanation for 
a more in-depth explanation.

Optimal Space & Time Complexity
O(nlog(n)) time | O(n) space - where n is the number of times

"""





##### Solution 1 #####
# O(nlog(n)) time | O(n) space - where n is the number of times
def laptopRentals(times):
  if len(times) == 0:
    return 0

  times.sort(key=lambda x: x[0])

  timesWhenLaptopIsUsed = [times[0]]
  heap = MinHeap(timesWhenLaptopIsUsed)

  for idx in range(1, len(times)):
    currentInterval = times[idx]
    if heap.peek()[1] <= currentInterval[0]:
      heap.remove()

    heap.insert(currentInterval)

  return len(timesWhenLaptopIsUsed)


class MinHeap:
  def __init__(self, array):
      self.heap = self.buildHeap(array)

  # O(n) time | O(1) space
  def buildHeap(self, array):
    firstParentIdx = (len(array) - 2) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
      self.siftDown(currentIdx, len(array) - 1, array)
    return array

  # O(log(n)) time | O(1) space
  def siftDown(self, currentIdx, endIdx, heap):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
      childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
      if childTwoIdx != -1 and heap[childTwoIdx][1] < heap[childOneIdx][1]:
        idxToSwap = childTwoIdx
      else:
        idxToSwap = childOneIdx
      if heap[idxToSwap][1] < heap[currentIdx][1]:
        self.swap(currentIdx, idxToSwap, heap)
        currentIdx = idxToSwap
        childOneIdx = currentIdx * 2 + 1
      else:
        return
            
  # O(log(n)) time | O(1) space
  def siftUp(self, currentIdx, heap):
    parentIdx = (currentIdx - 1) // 2
    while currentIdx > 0 and heap[currentIdx][1] < heap[parentIdx][1]:
      self.swap(currentIdx, parentIdx, heap)
      currentIdx = parentIdx
      parentIdx = (currentIdx - 1) // 2

  # O(1) time | O(1) space
  def peek(self):
    return self.heap[0]

  # O(log(n)) time | O(1) space
  def remove(self):
    self.swap(0, len(self.heap) - 1, self.heap)
    valueToRemove = self.heap.pop()
    self.siftDown(0, len(self.heap) - 1, self.heap)
    return valueToRemove

  # O(log(n)) time | O(1) space
  def insert(self, value):
    self.heap.append(value)
    self.siftUp(len(self.heap) - 1, self.heap)
      
  def swap(self, i, j, heap):
    heap[i], heap[j] = heap[j], heap[i]





##### Solution 2 #####
# O(nlog(n)) time | O(n) space - where n is the number of times
def laptopRentals(times):
  if len(times) == 0:
    return 0

  usedLaptops = 0
  startTimes = sorted([interval[0] for interval in times])  
  endTimes = sorted([interval[1] for interval in times])  

  startIterator = 0
  endIterator = 0

  while startIterator < len(times):
    if startTimes[startIterator] >= endTimes[endIterator]:
      usedLaptops -= 1
      endIterator += 1

    usedLaptops += 1
    startIterator += 1

  return usedLaptops
