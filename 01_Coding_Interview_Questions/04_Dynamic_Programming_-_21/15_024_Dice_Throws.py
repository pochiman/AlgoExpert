""" 

[ Difficulty: Hard ]
[ Category: Dynamic Programming ]

##### Dice Throws #####

You're given a set of numDice dice, each with numSides sides, and a target integer, 
which represents a target sum to obtain when rolling all of the dice and summing 
their values. Write a function that returns the total number of dice-roll 
permutations that sum up to exactly that target value.

All three input values will always be positive integers. Each of the dice has an 
equal probability of landing on any number from 1 to numSides. Identical total 
dice rolls obtained from different individual dice rolls (for example, [2, 3] vs. 
[3, 2]) count as different dice-roll permutations. If there's no possible dice-roll 
combination that sums up to the target given the input dice, your function should 
return 0.


##### Sample Input #####
numDice = 2
numSides = 6
target = 7

##### Sample Output #####
6 // [1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]


##### Hints #####

Hint 1
It can be helpful to start by thinking about simple cases. When do you know the 
answer will be 0 or -1?

Hint 2
If you had the solution of all simpler inputs, how would you find the solution 
for the given input?

Hint 3
The solution to diceThrows(numThrows, numSides, target) can be thought of as the 
sum of diceThrows(numThrows - 1, numSides, target) for all possible target values 
between target - numSides and target.

Optimal Space & Time Complexity
O(d * s * t) time | O(t) space - where d is the number of throws, s is the number 
of sides, and t is the target.

"""





##### Solution 1 #####
# O(d * s * t) time | O(d * t) space - where d is the number of dice, s is the
# number of sides, and t is the target.
def diceThrows(numDice, numSides, target):
    storedResults = [[-1] * (target + 1) for _ in range(numDice + 1)]
    return diceThrowsHelper(numDice, numSides, target, storedResults)


def diceThrowsHelper(numDice, numSides, target, storedResults):
    if numDice == 0:
        return 1 if target == 0 else 0

    if storedResults[numDice][target] > -1:
        return storedResults[numDice][target]

    numWaysToReachTarget = 0
    for currentTarget in range(max(0, target - numSides), target):
        numWaysToReachTarget += diceThrowsHelper(
            numDice - 1, numSides, currentTarget, storedResults
        )
    storedResults[numDice][target] = numWaysToReachTarget

    return numWaysToReachTarget





##### Solution 2 #####
# O(d * s * t) time | O(d * t) space - where d is the number of dice, s is the
# number of sides, and t is the target.
def diceThrows(numDice, numSides, target):
    storedResults = [[0] * (target + 1) for _ in range(numDice + 1)]
    storedResults[0][0] = 1

    for currentNumDice in range(1, numDice + 1):
        for currentTarget in range(target + 1):
            numWaysToReachTarget = 0
            for currentNumSides in range(1, min(currentTarget, numSides) + 1):
                numWaysToReachTarget += storedResults[currentNumDice - 1][
                    currentTarget - currentNumSides
                ]
            storedResults[currentNumDice][currentTarget] = numWaysToReachTarget

    return storedResults[numDice][target]





##### Solution 3 #####
# O(d * s * t) time | O(t) space - where d is the number of dice, s is the
# number of sides, and t is the target.
def diceThrows(numDice, numSides, target):
    storedResults = [[0] * (target + 1), [0] * (target + 1)]
    storedResults[0][0] = 1

    previousNumDiceIndex = 0
    newNumDiceIndex = 1
    for _ in range(numDice):
        for currentTarget in range(target + 1):
            numWaysToReachTarget = 0
            for currentNumSides in range(1, min(currentTarget, numSides) + 1):
                numWaysToReachTarget += storedResults[previousNumDiceIndex][
                    currentTarget - currentNumSides
                ]
            storedResults[newNumDiceIndex][currentTarget] = numWaysToReachTarget
        previousNumDiceIndex, newNumDiceIndex = newNumDiceIndex, previousNumDiceIndex

    return storedResults[previousNumDiceIndex][target]
