""" 

[ Difficulty: Very Hard ]
[ Category: Famous Algorithms ]

##### A* Algorithm #####

You're given a two-dimensional array containing 0s and 1s, where each 0 
represents a free space and each 1 represents an obstacle (a space that cannot 
be passed through). You can think of this array as a grid-shaped graph. You're 
also given four integers startRow, startCol, endRow, and endCol, representing 
the positions of a start node and an end node in the graph.

Write a function that finds the shortest path between the start node and the 
end node using the A* search algorithm and returns it.

The shortest path should be returned as an array of node positions, where each 
node position is an array of two elements: the [row, col] of the respective node 
in the graph. The output array should contain the start node's position, the end 
node's position, and all of the positions of the remaining nodes in the shortest 
path, and these node positions should be ordered from start node to end node.

If there is no path from the start node to the end node, your function should 
return an empty array.

Note that:

  * From each node in the graph, you can only travel in four directions: up, 
    left, down and right; you can't travel diagonally.

  * The distance between all neighboring nodes in the graph is the same; you 
    can treat it as a distance of 1.

  * The start node and end node are guaranteed to be located in empty spaces 
    (cells containing 0).

  * The start node and end node will never be out of bounds and will never 
    overlap.

  * There will be at most one shortest path from the start node to the end node.

If you're unfamiliar with A*, we recommend watching the Conceptual Overview 
section of this question's video explanation before starting to code.


##### Sample Input #####
startRow = 0
startCol = 1
endRow = 4
endCol = 3
graph = [
  [0, 0, 0, 0, 0], 
  [0, 1, 1, 1, 0], 
  [0, 0, 0, 0, 0], 
  [1, 0, 1, 1, 1], 
  [0, 0, 0, 0, 0], 
]

##### Sample Output #####
[[0, 1], [0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1], [4, 2], [4, 3]]

// The shortest path can be clearly seen here:
// [
//   [., ., 0, 0, 0], 
//   [., 1, 1, 1, 0], 
//   [., ., 0, 0, 0], 
//   [1, ., 1, 1, 1], 
//   [0, ., ., ., 0], 
// ]


##### Hints #####

Hint 1
A* works by visiting nodes in the graph, one by one, all the while keeping track 
of their shortest estimated distance to the end node and continuously updating 
these distances. More specifically, the algorithm keeps track of unvisited nodes 
and visits the unvisited node with the shortest estimated distance to the end 
node at any point in time, naturally starting with the start node. Whenever the 
algorithm visits an unvisited node, it looks at all of its neighboring nodes and 
tries to update their shortest estimated distance to the end node, using the 
current shortest distance to the current node as a base and using a special 
heuristic to estimate the remaining distance to the end node. In a grid-shaped 
graph, the heuristic used is often the Manhattan Distance (i.e., the number of 
naive vertical and horizontal steps between the current node and the end node). 
Once the algorithm has reached the end node, it is guaranteed to have found the 
shortest path to it. How can you implement this algorithm?

Hint 2
The most challenging part of A* is determining how to efficiently find the 
node with the current shortest estimated distance to the end. Can you think 
of a data structure that could be used to keep track of the distances and to 
efficiently retrieve the node with the current shortest estimated distance 
to the end at each step?

Hint 3
Create a min-heap that will hold all of the unvisited nodes and their current 
shortest estimated distance to the end node. Initialize all nodes except for 
the start node as having a shortest estimated distance to the end node of 
infinity and also a shortest distance from the start node to themselves of 
infinity; the start node will have a distance to itself of 0 and an estimated 
distance to the end node of its Manhattan Distance to the end node. Next, 
write a while loop that will run until the min-heap is empty or until the end 
node is reached. At every iteration in the loop, remove the node from the top 
of the heap (the node with the shortest estimated distance to the end node), 
loop through all of its neighboring nodes, and for each neighbor, update its 
two distances if reaching the neighbor from the current node yields a shorter 
distance than whatever's already stored on the neighbor. Once you reach the 
end node, you'll have found the shortest path to it from the start node. Note 
that you'll have to keep track of which node each node came from whenever you 
update node distances; this is so that you can reconstruct the shortest path 
once you reach the end node.

Optimal Space & Time Complexity
O(w * h * log(w * h)) time | O(w * h) space - where w is the width of the graph 
and h is the height

"""





##### Solution 1 #####
class Node:
    def __init__(self, row, col, value):
        self.id = str(row) + "-" + str(col)
        self.row = row  
        self.col = col  
        self.value = value  
        self.distanceFromStart = float("inf")  
        self.estimatedDistanceToEnd = float("inf")  
        self.cameFrom = None  


# O(w * h * log(w * h)) time | O(w * h) space - where 
# w is the width of the graph and h is the height      
def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    nodes = initializeNodes(graph)

    startNode = nodes[startRow][startCol]
    endNode = nodes[endRow][endCol]

    startNode.distanceFromStart = 0
    startNode.estimatedDistanceToEnd = calculateManhattanDistance(startNode, endNode)  

    nodesToVisit = MinHeap([startNode])

    while not nodesToVisit.isEmpty():
        currentMinDistanceNode = nodesToVisit.remove()  
  
        if currentMinDistanceNode == endNode:
            break

        neighbors = getNeighboringNodes(currentMinDistanceNode, nodes)    
        for neighbor in neighbors:
            if neighbor.value == 1:
                continue  

            tentativeDistanceToNeighbor = currentMinDistanceNode.distanceFromStart + 1

            if tentativeDistanceToNeighbor >= neighbor.distanceFromStart:
                continue

            neighbor.cameFrom = currentMinDistanceNode    
            neighbor.distanceFromStart = tentativeDistanceToNeighbor    
            neighbor.estimatedDistanceToEnd = tentativeDistanceToNeighbor + calculateManhattanDistance(    
                neighbor, endNode    
            )  

            if not nodesToVisit.containsNode(neighbor):
                nodesToVisit.insert(neighbor)    
            else:
                nodesToVisit.update(neighbor)  

    return reconstructPath(endNode)  


def initializeNodes(graph):
    nodes = []

    for i, row in enumerate(graph):
        nodes.append([])
        for j, value in enumerate(row):
            nodes[i].append(Node(i, j, value))  
    
    return nodes


def calculateManhattanDistance(currentNode, endNode):
    currentRow = currentNode.row
    currentCol = currentNode.col
    endRow = endNode.row
    endCol = endNode.col

    return abs(currentRow - endRow) + abs(currentCol - endCol)  


def getNeighboringNodes(node, nodes):
    neighbors = []  

    numRows = len(nodes)
    numCols = len(nodes[0])

    row = node.row
    col = node.col  

    if row < numRows - 1:  # DOWN
        neighbors.append(nodes[row + 1][col])  

    if row > 0:  # UP
        neighbors.append(nodes[row - 1][col])   

    if col < numCols - 1:  # RIGHT
        neighbors.append(nodes[row][col + 1]) 

    if col > 0:  # LEFT
        neighbors.append(nodes[row][col - 1])   

    return neighbors


def reconstructPath(endNode):    
    if not endNode.cameFrom:
        return []

    currentNode = endNode
    path = []

    while currentNode is not None:
        path.append([currentNode.row, currentNode.col])  
        currentNode = currentNode.cameFrom

    return path[::-1]  # reverse path so it goes from start to end


class MinHeap:
    def __init__(self, array):
        # Holds the position in the heap that each node is at
        self.nodePositionsInHeap = {node.id: idx for idx, node in enumerate(array)}  
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    # O(n) time | O(1) space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)  
        return array

    # O(log(n)) time | O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if (
                childTwoIdx != -1
                and heap[childTwoIdx].estimatedDistanceToEnd < heap[childOneIdx].estimatedDistanceToEnd  
            ):  
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx  
            if heap[idxToSwap].estimatedDistanceToEnd < heap[currentIdx].estimatedDistanceToEnd:  
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    # O(log(n)) time | O(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx].estimatedDistanceToEnd < heap[parentIdx].estimatedDistanceToEnd: 
            self.swap(currentIdx, parentIdx, heap)       
            currentIdx = parentIdx  
            parentIdx = (currentIdx - 1) // 2

    # O(log(n)) time | O(1) space
    def remove(self):
        if self.isEmpty():
            return

        self.swap(0, len(self.heap) - 1, self.heap)    
        node = self.heap.pop()
        del self.nodePositionsInHeap[node.id]
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return node

    # O(log(n)) time | O(1) space
    def insert(self, node):
        self.heap.append(node)  
        self.nodePositionsInHeap[node.id] = len(self.heap) - 1
        self.siftUp(len(self.heap) - 1, self.heap)         

    def swap(self, i, j, heap):
        self.nodePositionsInHeap[heap[i].id] = j    
        self.nodePositionsInHeap[heap[j].id] = i    
        heap[i], heap[j] = heap[j], heap[i]

    def containsNode(self, node):
        return node.id in self.nodePositionsInHeap

    def update(self, node):
        self.siftUp(self.nodePositionsInHeap[node.id], self.heap)
