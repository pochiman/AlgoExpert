""" 

[ Difficulty: Medium ]
[ Category: Arrays ]

##### Missing Numbers #####

You're given an unordered list of unique integers nums in the range [1, n], 
where n represents the length of nums + 2. This means that two numbers in this 
range are missing from the list.

Write a function that takes in this list and returns a new list with the two 
missing numbers, sorted numerically.


##### Sample Input #####
nums = [1, 4, 3]

##### Sample Output #####
[2, 5] // n is 5, meaning the completed list should be [1, 2, 3, 4, 5]


##### Hints #####

Hint 1
How would you solve this problem if there was only one missing number? 
Can that solution be applied to this problem with two missing numbers?

Hint 2
To efficiently find a single missing number, you can sum up all of the values 
in the array as well as sum up all of the values in the expected array (i.e. in 
the range [1, n]). The difference between these values is the missing number.

Hint 3
Using the same logic as for a single missing number, you can find the total 
of the two missing numbers. How can you then find which numbers these are?

Hint 4
If you take an average of the two missing numbers, one of the missing numbers 
must be less than that average, and one must be greater than the average.

Hint 5
Since we know there is one missing number on each side of the average, we can
treat each side of the list as its own problem to find one missing number in 
that list.

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the length of the input array

"""





##### Solution 1 #####
# O(n) time | O(n) space - where n is the length of the input array
def missingNumbers(nums):
    includedNums = set(nums)

    solution = []
    for num in range(1, len(nums) + 3):
        if not num in includedNums:
            solution.append(num)

    return solution          





##### Solution 2 #####
# O(n) time | O(1) space - where n is the length of the input array
def missingNumbers(nums):
    total = sum(range(1, len(nums) + 3))
    for num in nums:
        total -= num

    averageMissingValue = total // 2
    foundFirstHalf = 0
    foundSecondHalf = 0
    for num in nums:
        if num <= averageMissingValue:
            foundFirstHalf += num
        else:
            foundSecondHalf += num

    expectedFirstHalf = sum(range(1, averageMissingValue + 1))
    expectedSecondHalf = sum(range(averageMissingValue + 1, len(nums) + 3))

    return [expectedFirstHalf - foundFirstHalf, expectedSecondHalf - foundSecondHalf]





##### Solution 3 #####
# O(n) time | O(1) space - where n is the length of the input array
def missingNumbers(nums):
    solutionXOR = 0
    for i in range(0, len(nums) + 3):
        solutionXOR ^= i
        if i < len(nums):
            solutionXOR ^= nums[i]

    solution = [0, 0]
    setBit = solutionXOR & -solutionXOR
    for i in range(0, len(nums) + 3):
        if i & setBit == 0:
            solution[0] ^= i
        else:
            solution[1] ^= i

        if i < len(nums):
            if nums[i] & setBit == 0:
                solution[0] ^= nums[i]
            else:
                solution[1] ^= nums[i]

    return sorted(solution)
