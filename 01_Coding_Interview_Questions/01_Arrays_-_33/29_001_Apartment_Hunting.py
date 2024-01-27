""" 

[ Difficulty: Very Hard ]
[ Category: Arrays ]

##### Apartment Hunting #####

You're looking to move into a new apartment on specific street, and you're given 
a list of contiguous blocks on that street where each block contains an apartment 
that you could move into.

You also have a list of requirements: a list of buildings that are important to 
you. For instance, you might value having a school and a gym near your apartment. 
The list of blocks that you have contains information at every block about all of 
the buildings that are present and absent at the block in question. For instance, 
for every block, you might know whether a school, a pool, an office, and a gym are 
present.

In order to optimize your life, you want to pick an apartment block such that you 
minimize the farthest distance you'd have to walk from your apartment to reach any 
of your required buildings.

Write a function that takes in a list of contiguous blocks on a specific street 
and a list of your required buildings and that returns the location (the index) 
of the block that's most optimal for you.

If there are multiple most optimal blocks, your function can return the index of 
any one of them.


##### Sample Input #####
blocks = [
  {
    "gym": false, 
    "school": true, 
    "store": false, 
  }, 
  {
    "gym": true, 
    "school": false, 
    "store": false, 
  },
  {
    "gym": true, 
    "school": true, 
    "store": false, 
  },
  {
    "gym": false, 
    "school": true, 
    "store": false, 
  },
  {
    "gym": false, 
    "school": true, 
    "store": true, 
  }, 
]
reqs = ["gym", "school", "store"]

##### Sample Output #####
3 // at index 3, the farthest you'd have to walk to reach a gym, a school, 
or a store is 1 block; at any other index, you'd have to walk farther


##### Hints #####

Hint 1
For every block, you want to go through every requirement, and for every 
requirement, you want to find the closest other block with that requirement 
(or rather, the smallest distance to another block with that requirement). 
Once you've done that for every requirement and for every block, you want 
to pick, for every block, the distance of the farthest requirement. You can 
do this with three nested "for" loops.

Hint 2
Is there a way to optimize on the solution mentioned in Hint #1 (that uses 
three nested "for" loops) by precomputing the smallest distances of every 
requirement from every block?

Hint 3
For every requirement, you should be able to precompute its smallest distances 
from every block by doing two simple passes through the array of blocks: one 
pass from left to right and one pass from right to left. Once you have these 
precomputed values, you can iterate through all of the blocks and pick the 
biggest of all the precomputed distances at that block.

Optimal Space & Time Complexity
O(br) time | O(br) space - where b is the number of blocks and r is the 
number of requirements

"""





##### Solution 1 #####
# O(b^2*r) time | O(b) space - where b is the number of blocks and r is the number 
# of requirements
def apartmentHunting(blocks, reqs):
    maxDistancesAtBlocks = [float("-inf") for block in blocks]
    for i in range(len(blocks)):
        for req in reqs:
            closestReqDistance = float("inf")
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestReqDistance = min(closestReqDistance, distanceBetween(i, j))
            maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks[i], closestReqDistance)
    return getIdxAtMinValue(maxDistancesAtBlocks)


def getIdxAtMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i
    return idxAtMinValue


def distanceBetween(a, b):
    return abs(a - b)





##### Solution 2 #####
# O(br) time | O(br) space - where b is the number of blocks and r is the number 
# of requirements
def apartmentHunting(blocks, reqs):
    minDistancesFromBlocks = list(map(lambda req: getMinDistances(blocks, req), reqs))
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks)
    return getIdxAtMinValue(maxDistancesAtBlocks)


def getMinDistances(blocks, req):
    minDistances = [0 for block in blocks]
    closestReqIdx = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = distanceBetween(i, closestReqIdx)
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIdx))
    return minDistances


def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
    maxDistancesAtBlocks = [0 for block in blocks]
    for i in range(len(blocks)):
        minDistancesAtBlock = list(map(lambda distances: distances[i], minDistancesFromBlocks))
        maxDistancesAtBlocks[i] = max(minDistancesAtBlock)
    return maxDistancesAtBlocks


def getIdxAtMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i
    return idxAtMinValue


def distanceBetween(a, b):
    return abs(a - b)
