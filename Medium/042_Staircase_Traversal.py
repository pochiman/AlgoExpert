""" 

##### Staircase Traversal #####

You're given two positive integers representing the height of a staircase and the 
maximum number of steps that you can advance up the staircase at a time.  Write 
a function that returns the number of ways in which you can climb the staircase.

For example, if you were given a staircase of height = 3 and maxSteps = 2 
you could climb the staircase in 3 ways.  You could take 1 step, 1 step, 
then 1 step, you could also take 1 step, then 2 steps, and you could 
take 2 steps, then 1 step.

Note that maxSteps <= height will always be true.


##### Sample Input #####
height = 4
maxSteps = 2

##### Sample Output #####
5
// You can climb the staircase in the following ways:
// 1, 1, 1, 1
// 1, 1, 2
// 1, 2, 1
// 2, 1, 1
// 2, 2


##### Hints #####

Hint 1
If you can advance 2 steps at a time, how many ways can you reach a 
staircase of height 1 and of height 2?  Think recursively.

Hint 2
Continuing from Hint #1, if you know the number of ways to climb a 
staircase of height 1 and of height 2, how many ways are there to climb 
a staircase of height 3 (assuming the same max steps of 2)?

Hint 3
The number of ways to climb a staircase of height k with a max number of 
steps s is:
numWays[k - 1] + numWays[k - 2] + ... + numWays[k - s].
This is because if you can advance between 1 and s steps, then from 
each step k - 1, k - 2, ..., k - s, you can directly advance to the 
top of a staircase of height k.  By adding the number of ways to reach all 
steps that you can directly advance to the top step from, you determine how 
many ways there are to reach the top step.

Optimal Space & Time Complexity
O(n) time | O(n) space - where n is the height of the staircase

"""





##### Solution 1 #####
# O(k^n) time | O(n) space - where n is the height of the staircase and k is the number of allowed steps
def staircaseTraversal(height, maxSteps):
  return numberOfWaysToTop(height, maxSteps)


def numberOfWaysToTop(height, maxSteps):
  if height <= 1:
    return 1

  numberOfWays = 0
  for step in range(1, min(maxSteps, height) + 1):
    numberOfWays += numberOfWaysToTop(height - step, maxSteps)

  return numberOfWays





##### Solution 2 #####
# O(n * k) time | O(n) space - where n is the height of the staircase and k is the number of allowed steps
def staircaseTraversal(height, maxSteps):
  return numberOfWaysToTop(height, maxSteps, {0: 1, 1: 1})


def numberOfWaysToTop(height, maxSteps, memoize):
  if height in memoize:
    return memoize[height]

  numberOfWays = 0
  for step in range(1, min(maxSteps, height) + 1):
    numberOfWays += numberOfWaysToTop(height - step, maxSteps, memoize)

  memoize[height] = numberOfWays  

  return numberOfWays





##### Solution 3 #####
# O(n * k) time | O(n) space - where n is the height of the staircase and k is the number of allowed steps
def staircaseTraversal(height, maxSteps):
  waysToTop = [0 for _ in range(height + 1)]
  waysToTop[0] = 1
  waysToTop[1] = 1  

  for currentHeight in range(2, height + 1):
    step = 1
    while step <= maxSteps and step <= currentHeight:
      waysToTop[currentHeight] = waysToTop[currentHeight] + waysToTop[currentHeight - step]
      step += 1

  return waysToTop[height]





##### Solution 4 #####
# O(n) time | O(n) space - where n is the height of the staircase
def staircaseTraversal(height, maxSteps):
  currentNumberOfWays = 0
  waysToTop = [1]  

  for currentHeight in range(1, height + 1):
    startOfWindow = currentHeight - maxSteps - 1
    endOfWindow = currentHeight - 1
    if startOfWindow >= 0:
      currentNumberOfWays -= waysToTop[startOfWindow]

    currentNumberOfWays += waysToTop[endOfWindow]
    waysToTop.append(currentNumberOfWays)  

  return waysToTop[height]
  