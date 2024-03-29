""" 

[ Difficulty: Hard ]
[ Category: Dynamic Programming ]

##### Knapsack Problem #####

You're given an array of arrays where each subarray holds two integer values and 
represents an item; the first integer is the item's value, and the second integer is 
the item's weight. You're also given an integer representing the maximum capacity 
of a knapsack that you have.

Your goal is to fit items in your knapsack without having the sum of their weights 
exceed the knapsack's capacity, all the while maximizing their combined value. 
Note that you only have one of each item at your disposal.

Write a function that returns the maximized combined value of the items that you 
should pick as well as an array of the indices of each item picked.

If there are multiple combinations of items that maximize the total value in the 
knapsack, your function can return any of them.


##### Sample Input #####
items = [[1, 2], [4, 3], [5, 6], [6, 7]]
capacity = 10

##### Sample Output #####
[10, [1, 3]] // items [4, 3] and [6, 7]


##### Hints #####

Hint 1
Try building a two-dimensional array of the maximum values that knapsacks of 
all capacities between 0 and c inclusive could hold, given one, two, three, 
etc., items. Let columns represent capacities and rows represent items.

Hint 2
Build up the array mentioned in Hint #1 one row at a time. In other words, 
find the maximum values that knapsacks of all capacities between 0 and c can 
hold with only one item, then with two, etc., until you use all items. Find a 
formula that relates the maximum value at any given point to previous values.

Hint 3
Backtrack your way through the two-dimensional array mentioned in Hint #1 to 
find which items are in your knapsack. Start at the final index in the array 
and check whether or not the value stored at that index is equal to the value 
located one row above. If it isn't, then the item represented by the current 
row is in the knapsack.

Optimal Space & Time Complexity
O(nc) time | O(nc) space - where n is the number of items and c is the capacity

"""





##### Solution 1 #####
# O(nc) time | O(nc) space
def knapsackProblem(items, capacity):
    knapsackValues = [[0 for x in range(0, capacity + 1)] for y in range(0, len(items) + 1)]
    for i in range(1, len(items) + 1):
        currentWeight = items[i - 1][1]
        currentValue = items[i - 1][0]
        for c in range(0, capacity + 1):
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i - 1][c]
            else:
                knapsackValues[i][c] = max(
                    knapsackValues[i - 1][c], knapsackValues[i - 1][c - currentWeight] + currentValue
                )
    return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]


def getKnapsackItems(knapsackValues, items):
    sequence = []
    i = len(knapsackValues) - 1
    c = len(knapsackValues[0]) - 1
    while i > 0:
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))
