"""

[ Difficulty: Very Hard ]
[ Category: Stacks ]

##### Largest Park #####

A city wants to build a new public park, and you've been tasked with finding the 
largest park they can build without disturbing existing infrastructure.

Write a function that takes in a two-dimensional array (a matrix) land representing 
the total land of the city from a top-down view. Each value in land is a boolean; 
false values are pieces of land not currently in use, while true values are pieces 
of land currently in use by other infrastructure. Return the area of the largest 
possible park.

The largest possible park will be placed exclusively on unused land (false values). 
Moreover, the city wants the park to be a perfect rectangle. If there is no available 
land, your function should return 0.


##### Sample Input #####
land = [
  [false, true, true, true, false],
  [false, false, false, true, false],
  [false, false, false, false, false],
  [false, true, true, true, true]
]

##### Sample Output #####
6  // The park would go from row 1 to row 2 in columns 0 to 3, giving a total 
      area of 6.

##### Hints #####

Hint 1
Try first breaking this problem down into smaller problems. If you had only a 
single row, how would you find the largest rectangle of available land in that 
single row?

Hint 2
If a second row is added below the first row, now each column has a height. This 
essentially forms a histogram, where you need to find the largest rectangle within 
that histogram.

Hint 3
To find the area of the largest rectangle in one of these histograms, you need 
to find the width and the height of the rectangles. Since they must be perfect 
rectangles, the height is constrained to the lowest height of the histogram bars 
in the span. The width is then the number of bars in the span.

Hint 4
As you iterate through the histogram, think about how you can identify the start 
and end of a potential rectangle. When you encounter a bar that is shorter than 
the previous bars, it means the current rectangle has ended. Can you use this 
observation to find the largest rectangle in the histogram?

Hint 5
To keep track of the bars that are part of the same rectangle, try using a 
monotonic stack to maintain the column indices in increasing order based on 
heights.

Hint 6
Iterate through each column of the historgram. While the stack is not empty and 
the height at the current column index is less than the height at the index on 
top of the stack, pop column indices off of the stack, calculating the rectangle's 
width and height using the popped index and current index. Check if this area is 
larger than the largest area seen so far, and if it is then save it. After this 
process, append the current index to the stack. After this iteration, make sure 
to also process any remaining values in the stack. 

Hint 7
Repeat this process with every row, finding the largest possible rectangle of the 
histogram where this row is the bottom row. The largest rectangle found in any of 
these rows will be the final solution.

Optimal Space & Time Complexity
O(w * h) time | O(w) space - where w is the width of the input matrix and h is 
the height of the input matrix

"""





##### Solution 1 #####
# O(w * h) time | O(w) space - where w is the width of the input matrix and
# h is the height of the input matrix
def largestPark(land):
    heights = [0] * len(land[0])
    maxArea = 0

    for row in land:
        for columnIndex in range(len(land[0])):
            heights[columnIndex] = heights[columnIndex] + 1 if row[columnIndex] == False else 0
        maxArea = max(maxArea, largestRectangleHistogram(heights))

    return maxArea


def largestRectangleHistogram(heights):
    stack = []
    maxArea = 0

    for columnIndex in range(len(heights)):
        while len(stack) > 0 and heights[columnIndex] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = columnIndex if len(stack) == 0 else columnIndex - stack[-1] - 1
            maxArea = max(maxArea, width * height)
        stack.append(columnIndex)

    while len(stack) > 0:
        height = heights[stack.pop()]
        width = len(heights) if len(stack) == 0 else len(heights) - stack[-1] - 1
        maxArea = max(maxArea, width * height)

    return maxArea