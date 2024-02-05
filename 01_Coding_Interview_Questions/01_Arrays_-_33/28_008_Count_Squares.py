""" 

[ Difficulty: Hard ]
[ Category: Arrays ]

##### Count Squares #####

Write a function that takes in a list of Cartesian coordinates (i.e., (x, y) 
coordinates) and returns the number of squares that can be formed by these 
coordinates.

A square must have its four corners amongst the coordinates in order to be counted. 
A single coordinate can be used as a corner for multiple different squares.

You can also assume that no coordinate will be farther than 100 units from the 
origin.


##### Sample Input #####
points = [ 
  [1, 1], 
  [0, 0], 
  [-4, 2], 
  [-2, -1], 
  [0, 1], 
  [1, 0], 
  [-1, 4]
]
 
##### Sample Output #####
   // [1, 1], [0, 0], [0, 1], and [1, 0] makes a square,
2 // as does [1, 1], [-4, 2], [-2, -1], and [-1, 4]


##### Hints #####

Hint 1
Given any two points, there are exactly three pairs of points that would make 
a square.

Hint 2
If two points are assumed to be diagonally across from each other in a square, 
there is only one pair of points that would complete the square.

Hint 3
All four points of a square will always be equidistant from the midpoint.

Hint 4
The slopes of the two diagonals of a square are always negative reciprocals of
each other.

Optimal Space & Time Complexity
O(n^2) time | O(n) space - where n is the number of points

"""





##### Solution 1 #####
# O(n^2) time | O(n) space - where n is the number of points
def countSquares(points):
    pointsSet = set()
    for point in points:
        pointsSet.add(pointToString(point))

    count = 0
    for pointA in points:
        for pointB in points:
            if pointA == pointB:
                continue

            midpoint = [(pointA[0] + pointB[0]) / 2, (pointA[1] + pointB[1]) / 2]
            xDistanceFromMid = pointA[0] - midpoint[0]
            yDistanceFromMid = pointA[1] - midpoint[1]

            pointC = [midpoint[0] + yDistanceFromMid, midpoint[1] - xDistanceFromMid]
            pointD = [midpoint[0] - yDistanceFromMid, midpoint[1] + xDistanceFromMid]

            if pointToString(pointC) in pointsSet and pointToString(pointD) in pointsSet:
                count += 1

    return count / 4


def pointToString(point):
    if point[0] % 1 == 0 and point[1] % 1 == 0:
        point = [int(coordinate) for coordinate in point]
    return ",".join([str(coordinate) for coordinate in point])
