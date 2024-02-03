""" 

[ Difficulty: Medium ]
[ Category: Arrays ]

##### Sweet And Savory #####

You're hosting an event at a food festival and want to showcase the best 
possible pairing of two dishes from the festival that complement each 
other's flavor profile.

Each dish has a flavor profile represented by an integer. A negative integer 
means a dish is sweet, while a positive integer means a dish is savory. The 
absolute value of that integer represents the intensity of that flavor. For 
example, a flavor profile of -3 is slightly sweet, one of -10 is extremely 
sweet, one of 2 is mildly savory, and one of 8 is significantly savory.

You're given an array of these dishes and a target combined flavor profile. 
Write a function that returns the best possible pairing of two dishes (the 
pairing with a total fl avor profi le that's closest to the targetone). Note 
that this pairing must include one sweet and one savory dish. You're also 
concerned about the dish being too savory, so your pairing should never be 
more savory than the target flavor profile.

All dishes will have a positive or negative flavor profile; there are no dishes 
with a 0 value. For simplicity, you can assume that there will be at most one 
best solution. If there isn't a valid solution, your function should return 
[0, 0]. The returned array should be sorted, meaning the sweet dish should 
always come first.


##### Sample Input #1 #####
dishes = [-3, -5, 1, 7]
target = 8

##### Sample Output #1 #####
[-3, 7] // The combined profile of 4 is closest without going over

##### Sample Input #2 #####
dishes = [3, 5, 7, 2, 6, 8, 1]
target = 10

##### Sample Output #2 #####
[0, 0] // There are no sweet dishes

##### Sample Input #3 #####
dishes = [2, 5, -4, -7, 12, 100, -25]
target = -20

##### Sample Output #3 #####
[-25, 5] // This pairing gets the exact combined profile of -20


##### Hints #####

Hint 1
The sweet and savory dishes are essentially two different lists that have been 
combined into one. It can be helpful to first separate them.

Hint 2
Looking at all possible pairs will be inefficient. Would sorting the lists first 
help improve the time complexity?

Hint 3
Try using a two pointer approach to find the best pairing. Start with a current 
pairing, and move the savory pointer until the pairing gets too savory. If the 
dish is too savory, then move the sweet pointer. Do this through the entire 
lists, keeping track of the best pairing you find.

Optimal Space & Time Complexity
O(n * log(n)) time | O(n) space - where n is number of dishes

"""





##### Solution 1 #####
# O(n * log(n)) time | O(n) space - where n is number of dishes
def sweetAndSavory(dishes, target):
    sweetDishes = sorted([dish for dish in dishes if dish < 0], key=abs)
    savoryDishes = sorted([dish for dish in dishes if dish > 0])

    bestPair = [0, 0]
    bestDifference = float("inf")
    sweetIndex, savoryIndex = 0, 0

    while sweetIndex < len(sweetDishes) and savoryIndex < len(savoryDishes):
        currentSum = sweetDishes[sweetIndex] + savoryDishes[savoryIndex]

        if currentSum <= target:
            currentDifference = target - currentSum
            if currentDifference < bestDifference:
                bestDifference = currentDifference
                bestPair = [sweetDishes[sweetIndex], savoryDishes[savoryIndex]]
            savoryIndex += 1
        else:
            sweetIndex += 1

    return bestPair        
