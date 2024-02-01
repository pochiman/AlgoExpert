"""

[ Difficulty: Very Hard ]
[ Category: Searching ]

##### Optimal Assembly Line #####

One of the most efficient ways to run a factory is to use an assembly line, with 
multiple stations performing different assembling steps simultaneously in order 
to save time. But an assembly line is only as fast as its slowest station/step; 
for example, if an assembly line has 100 different steps performed by 100 
different stations, with 99 steps taking 1 minute each to complete and 1 step 
taking 1 hour to complete, then the entire assembly line is dramatically slowed 
down by the 1-hour-long step.

Write a function that takes in a non-empty array of positive integers 
stepDurations and a positive integer numStations. The input array of integers 
represents the times that the various steps in an assembly process take, and 
the input integer represents the number of stations that this assembly process 
has access to. For this particular assembly process, a single station can perform 
multiple steps, so long as these steps are performed in order, meaning that a 
single station can perform multiple steps whose times appear consecutively in the 
stepDurations array. Your function should return the longest duration of a single 
station in the assembly line after optimizing the assembly line (i.e., minimizing 
its slowest station/step).

You can assume that there will never be more stations than steps.


##### Sample Input #####
stepDurations = [15, 15, 30, 30, 45]
numStations = 3

##### Sample Output #####
60  // Station 1 does steps 0 and 1. Station 2 does steps 2 and 3. Station 3 does step 4.

##### Hints #####

Hint 1
First try considering what the range of possible solutions are. What is the 
smallest possible solution and the largest possible solution?

Hint 2
The smallest possible solution would be the largest duration in stepDurations 
in the case that this step was the only step done by its station. The largest 
possible solution would be the sum of all of the stepDurations if they were 
all done by one solution. 

Hint 3
Given this smallest and largest possible solution, you can do a binary search 
between the values to find the smallest potential solution that is actually 
valid.

Hint 4
You can check if a potential solution is valid by during a single iteration 
through the stepDurations array. If a step has a duration larger than the 
potential solution's max station duration, then that can't be a correct solution. 
Otherwise, combine that step with the previous steps if the combination of them 
is not larger than the potential solution's max station duration. If it can't be 
combined with previous steps, then it must require a new station. Keep track of 
how many stations are required and ensure it is less than or equal to numStations.

Optimal Space & Time Complexity
O(n * log(m)) time | O(1) space - where n is the length of steps, and m is the 
sum of all values in steps

"""





##### Solution 1 #####
# O(n * log(m)) time | O(1) space - where n is the length of stepDurations, and
# m is the sum of all values in stepDurations
def optimalAssemblyLine(stepDurations, numStations):
    left, right = max(stepDurations), sum(stepDurations)
    maxStationDuration = float("inf")

    while left <= right:
        potentialMaxStationDuration = (left + right) // 2

        if isPotentialSolution(stepDurations, numStations, potentialMaxStationDuration):
            maxStationDuration = potentialMaxStationDuration
            right = potentialMaxStationDuration - 1
        else:
            left = potentialMaxStationDuration + 1

    return maxStationDuration


def isPotentialSolution(stepDurations, numStations, potentialMaxStationDuration):
    stationsRequired = 1
    currentDuration = 0

    for stepDuration in stepDurations:
        if currentDuration + stepDuration > potentialMaxStationDuration:
            stationsRequired += 1
            currentDuration = stepDuration
        else:
            currentDuration += stepDuration

    return stationsRequired <= numStations
