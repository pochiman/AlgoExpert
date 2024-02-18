""" 

[ Difficulty: Very Hard ]
[ Category: Binary Search Trees ]

##### Right Smaller Than #####

Write a function that takes in an array of integers and returns an array of the same 
length, where each element in the output array corresponds to the number of integers 
in the input array that are to the right of the relevant index and that are strictly 
smaller than the integer at that index.

In other words, the value at output[i] represents the number of integers that are to 
the right of i and that are strictly smaller than input[i].


##### Sample Input #####
array = [8, 5, 11, -1, 3, 4, 2]

##### Sample Output #####
[5, 4, 4, 0, 1, 1, 0]
// There are 5 integers smaller than 8 to the right of it.
// There are 4 integers smaller than 5 to the right of it.
// There are 4 integers smaller than 11 to the right of it.
// Etc..

##### Hints #####

Hint 1
The naive solution to this problem involves a simple pair of nested 
for loops and runs in O(n^2) time, where n is the length of the input 
array. This problem doesn't seem like it can be solved in linear time, 
so what time complexity could we realistically achieve if we somehow 
optimized our algorithm?

Hint 2
The only better complexity than the O(n^2) one of our naive solution 
that we could realistically achieve would be an O(nlog(n)) complexity. 
What data structure has log(n) operations, and how could it help for 
this problem?

Hint 3
A Binary Search Tree supports log(n) insertions and has the relevant 
property of every left-subtree-node having a smaller value than a given 
node's value; can we construct a BST from the input array in such a way 
that it leads us to the result array that we're looking for?

Hint 4
Construct a BST by inserting the input array's integers one by one, in 
reverse order (from right to left). At each insertion, once a new BST 
node is positioned in the BST, the number of nodes in its parent node's 
left subtree (plus the parent node itself, if its value is smaller than 
the inserted node's value) is the number of "right-smaller-than" 
elements for the element being inserted.

Hint 5
Going off of Hint #4, you can construct a special type of BST that stores 
the size of every node's left subtree. This value can then be used to 
obtain the right-smaller-than numbers for every element in the array.

Optimal Space & Time Complexity
Average case: when the created BST is balanced O(nlog(n)) time | O(n) space 
- where n is the length of the array --- 
Worst case: when the created BST is like a linked list O(n^2) time | O(n) space 

"""





##### Solution 1 #####
# O(n^2) time | O(n) space - where n is the length of the array
def rightSmallerThan(array):
    rightSmallerCounts = []
    for i in range(len(array)):
        rightSmallerCount = 0
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                rightSmallerCount += 1
        rightSmallerCounts.append(rightSmallerCount)
    return rightSmallerCounts





##### Solution 2 #####
# Average case: when the created BST is balanced
# O(nlog(n)) time | O(n) space - where n is the length of the array
# ---
# Worst case: when the created BST is like a linked list 
# O(n^2) time | O(n) space
def rightSmallerThan(array):
    if len(array) == 0:
        return []

    lastIdx = len(array) - 1
    bst = SpecialBST(array[lastIdx], lastIdx, 0)
    for i in reversed(range(len(array) - 1)):
        bst.insert(array[i], i)

    rightSmallerCounts = array[:]
    getRightSmallerCounts(bst, rightSmallerCounts)
    return rightSmallerCounts 


def getRightSmallerCounts(bst, rightSmallerCounts):
    if bst is None:
        return
    rightSmallerCounts[bst.idx] = bst.numSmallerAtInsertTime
    getRightSmallerCounts(bst.left, rightSmallerCounts)  
    getRightSmallerCounts(bst.right, rightSmallerCounts)  


class SpecialBST:
    def __init__(self, value, idx, numSmallerAtInsertTime):
        self.value = value
        self.idx = idx
        self.numSmallerAtInsertTime = numSmallerAtInsertTime
        self.leftSubtreeSize = 0
        self.left = None  
        self.right = None  

    def insert(self, value, idx, numSmallerAtInsertTime=0):
        if value < self.value:
            self.leftSubtreeSize += 1  
            if self.left is None:
                self.left = SpecialBST(value, idx, numSmallerAtInsertTime)
            else:
                self.left.insert(value, idx, numSmallerAtInsertTime)  
        else:
            numSmallerAtInsertTime += self.leftSubtreeSize
            if value > self.value:
                numSmallerAtInsertTime += 1
            if self.right is None:
                self.right = SpecialBST(value, idx, numSmallerAtInsertTime)  
            else:
                self.right.insert(value, idx, numSmallerAtInsertTime)





##### Solution 3 #####
# Average case: when the created BST is balanced
# O(nlog(n)) time | O(n) space - where n is the length of the array
# ---
# Worst case: when the created BST is like a linked list 
# O(n^2) time | O(n) space
def rightSmallerThan(array):
    if len(array) == 0:
        return []

    rightSmallerCounts = array[:]  
    lastIdx = len(array) - 1
    bst = SpecialBST(array[lastIdx])
    rightSmallerCounts[lastIdx] = 0  
    for i in reversed(range(len(array) - 1)):
        bst.insert(array[i], i, rightSmallerCounts)

    return rightSmallerCounts 


class SpecialBST:
    def __init__(self, value):
        self.value = value
        self.leftSubtreeSize = 0
        self.left = None  
        self.right = None  

    def insert(self, value, idx, rightSmallerCounts, numSmallerAtInsertTime=0):
        if value < self.value:
            self.leftSubtreeSize += 1  
            if self.left is None:
                self.left = SpecialBST(value)
                rightSmallerCounts[idx] = numSmallerAtInsertTime  
            else:
                self.left.insert(value, idx, rightSmallerCounts, numSmallerAtInsertTime)  
        else:
            numSmallerAtInsertTime += self.leftSubtreeSize
            if value > self.value:
                numSmallerAtInsertTime += 1
            if self.right is None:
                self.right = SpecialBST(value)
                rightSmallerCounts[idx] = numSmallerAtInsertTime  
            else:
                self.right.insert(value, idx, rightSmallerCounts, numSmallerAtInsertTime)
