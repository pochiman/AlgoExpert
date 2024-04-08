"""

[ Difficulty: Hard ]
[ Category: Famous Algorithms ]

##### Prim's Algorithm #####

You're given a list of edges representing a connected, weighted, undirected graph 
with at least one node.

The given list is what's called an adjacency list, and it represents a graph. The 
number of vertices in the graph is equal to the length of edges, where each index 
i in edges contains vertex i's siblings, in no particular order. Each of these 
siblings is an array of length two, with the first value denoting the index in the 
list that this vertex is connected to, and the second value denoting the weight of 
the edge. Note that this graph is undirected, meaning that if a vertex appears in 
the edge list of another vertex, then the inverse will also be true (along with 
the same weight).

Write a function implementing Prim's Algorithm to return a new edges array that 
represents a minimum spanning tree. A minimum spanning tree is a tree containing 
all of the vertices of the original graph and a subset of the edges. These edges 
should connect all of the vertices with the minimum total edge weight and without 
generating any cycles.

Note that the graph represented by edges won't contain any self-loops (vertices 
that have an outbound edge to themselves) and will only have positively weighted 
edges (i.e., no negative distances). The graph will always have at least one node.

If you're unfamiliar with Prim's algorithm, we recommend watching the Conceptual 
Overview section of this question's video explanation before starting to code.


##### Sample Input #####
edges = [ 
  [[1, 3], [2, 5]], 
  [[0, 3], [2, 10], [3, 12]], 
  [[0, 5], [1, 10]], 
  [[1, 12]]
]

##### Sample Output #####
[ 
  [[1, 3], [2, 5]], 
  [[0, 3], [3, 12]], 
  [[0, 5]], 
  [[1, 12]]
]

##### Hints #####

Hint 1
Prim's requires keeping track of all of the edges that have been discovered so 
far, with the ability to quickly retrieve the lowest distance edge. Is there a 
data structure that can be helpful here?

Hint 2
A good place to start is to implement a Min-Heap to hold all of the edges that 
have been found so far. This heap should prioritize edges based on their distance.

Hint 3
Prim's can start at any node. Start by choosing any arbitrary node and add all of 
its edges to the min heap.

Hint 4
Continue iterating through the heap until it is empty, meaning you have visited 
all of the potential edges in the minimum spanning tree. For each edge, if it 
connects to a previously unconnected vertex, add it to the output mst. Additionally, 
add all of the edges connected to this newly discovered vertex to the Min-Heap.

Optimal Space & Time Complexity
O(e * log(v)) time | O(e + v) space - where e is the number of edges in the input 
edges and v is the number of vertices

"""





##### Solution 1 #####
# O(e * log(v)) time | O(v + e) space - where e is the number
# of edges in the input edges and v is the number of vertices
def primsAlgorithm(edges):
    minHeap = MinHeap([[0, edge[0], edge[1]] for edge in edges[0]])

    mst = [[] for _ in range(len(edges))]
    while not minHeap.isEmpty():
        vertex, discoveredVertex, distance = minHeap.remove()

        if len(mst[discoveredVertex]) == 0:
            mst[vertex].append([discoveredVertex, distance])
            mst[discoveredVertex].append([vertex, distance])

            for neighbor, neighborDistance in edges[discoveredVertex]:
                if len(mst[neighbor]) == 0:
                    minHeap.insert([discoveredVertex, neighbor, neighborDistance])

    return mst


class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx][2] < heap[childOneIdx][2]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap][2] < heap[currentIdx][2]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx][2] < heap[parentIdx][2]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
