""" 

[ Difficulty: Hard ]
[ Category: Dynamic Programming ]

##### Juice Bottling #####

You're given an array of integers prices of length n with the retail prices of 
various quantities of juice. Each index in this array corresponds to the price 
of that amount of juice. For example, prices[2] would be the retail price of 2 
units of juice.

You have n - 1 total units of juice. For example, if the length of prices is 5, 
then you would have 4 total units of juice. Write a function to determine the 
optimal way to bottle the juice such that it maximizes revenue. This function 
should return a list of all of the juice quantities required in ascending order.

Note that the first value in the prices array will always be 0, because there is 
no value in no juice. All other values will be positive integers. Additionally, 
a larger quantity of juice will not always be more expensive than a smaller 
quantity. For simplicity, all of the test cases only have one possible solution.


##### Sample Input #####
prices = [0, 1, 3, 2]

##### Sample Output #####
       // We have 3 total units of juice,
       // because the length of prices is 4.
       // To maximize revenue, we split the juice into
[1, 2] // quantities of 1 and 2, giving a revenue of 1 + 3 = 4


##### Hints #####

Hint 1
If there were only 2 units of juice, how would you decide if it needs to be 
broken up?

Hint 2
If we add a third unit of juice, can you use the price of that entire unit and 
the solution for only 2 units to find the new solution?

Hint 3
The maximum profit at n can be modeled as the greater value of prices[n] and 
profit[size - m] + size[m] for every value m.

Optimal Space & Time Complexity
(n^2) time | O(n) space - where n is the length of prices

"""





##### Solution 1 #####
# O(n^3) time | O(n^2) space - where n is the length of prices
def juiceBottling(prices):
    numSizes = len(prices)
    maxProfit = [0] * numSizes
    solutions = [[]] * numSizes

    for size in range(numSizes):
        for dividingPoint in range(size + 1):
            possibleProfit = maxProfit[size - dividingPoint] + prices[dividingPoint]

            if possibleProfit > maxProfit[size]:
                maxProfit[size] = possibleProfit
                solutions[size] = [dividingPoint] + solutions[size - dividingPoint]

    return solutions[numSizes - 1]





##### Solution 2 #####
# O(n^2) time | O(n) space - where n is the length of prices
def juiceBottling(prices):
    numSizes = len(prices)
    maxProfit = [0] * numSizes
    dividingPoints = [0] * numSizes

    for size in range(numSizes):
        for dividingPoint in range(size + 1):
            possibleProfit = maxProfit[size - dividingPoint] + prices[dividingPoint]

            if possibleProfit > maxProfit[size]:
                maxProfit[size] = possibleProfit
                dividingPoints[size] = dividingPoint

    solution = []
    currentDividingPoint = numSizes - 1
    while currentDividingPoint > 0:
        solution.append(dividingPoints[currentDividingPoint])
        currentDividingPoint -= dividingPoints[currentDividingPoint]

    return solution
