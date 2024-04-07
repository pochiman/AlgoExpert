"""

[ Difficulty: Hard ]
[ Category: Famous Algorithms ]

##### Kruskal's Algorithm #####

You're given a list of edges representing a weighted, undirected graph with at 
least one node.

The given list is what's called an adjacency list, and it represents a graph. The 
number of vertices in the graph is equal to the length of edges, where each index 
i in edges contains vertex i's siblings, in no particular order. Each of these 
siblings is an array of length two, with the first value denoting the index in the 
list that this vertex is connected to, and the second value denoting the weight of 
the edge. Note that this graph is undirected, meaning that if a vertex appears in 
the edge list of another vertex, then the inverse will also be true (along with 
the same weight).

Write a function implementing Kruskal's Algorithm to return a new edges array that 
represents a minimum spanning tree. A minimum spanning tree is a tree containing 
all of the vertices of the original graph and a subset of the edges. These edges 
should connect all of the vertices with the minimum total edge weight and without 
generating any cycles.

If the graph is not connected, your function should return the minimum spanning 
forest (i.e. all of the nodes should be able to reach the same nodes as they could 
in the initial edge list).

Note that the graph represented by edges won't contain any self-loops (vertices 
that have an outbound edge to themselves) and will only have positively weighted 
edges (i.e., no negative distances).

If you're unfamiliar with Kruskal's algorithm, we recommend watching the Conceptual 
Overview section of this question's video explanation before starting to code. If 
you're unfamiliar with the Union Find data structure, we recommend completing that 
problem before attempting this one.


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
A good place to start is to transform the adjacency list into a list of all of 
the edges, sorted by weight.

Hint 2
To check if adding a given edge creates a cycle, try using a disjoint set. Start 
by thinking of each node as its own set. Then with each added edge, combine the 
sets of the connected nodes.

Optimal Space & Time Complexity
O(e * log(e)) time | O(e + v) space - where e is the number of edges in the input 
edges and v is the number of vertices

"""





##### Solution 1 #####
# O(e * log(e)) time | O(e + v) space - where e is the number
# of edges in the input edges and v is the number of vertices
def kruskalsAlgorithm(edges):
    edgeList = []
    for sourceIndex, vertex in enumerate(edges):
        for edge in vertex:
            if edge[0] > sourceIndex:
                edgeList.append([sourceIndex, edge[0], edge[1]])
    sortedEdges = sorted(edgeList, key=lambda edge: edge[2])

    parents = [vertex for vertex in range(len(edges))]
    ranks = [0 for _ in range(len(edges))]
    mst = [[] for _ in range(len(edges))]
    for edge in sortedEdges:
        vertex1Root = find(edge[0], parents)
        vertex2Root = find(edge[1], parents)
        if vertex1Root != vertex2Root:
            mst[edge[0]].append([edge[1], edge[2]])
            mst[edge[1]].append([edge[0], edge[2]])
            union(vertex1Root, vertex2Root, parents, ranks)

    return mst


def find(vertex, parents):
    if vertex != parents[vertex]:
        parents[vertex] = find(parents[vertex], parents)

    return parents[vertex]


def union(vertex1Root, vertex2Root, parents, ranks):
    if ranks[vertex1Root] < ranks[vertex2Root]:
        parents[vertex1Root] = vertex2Root
    elif ranks[vertex1Root] > ranks[vertex2Root]:
        parents[vertex2Root] = vertex1Root
    else:
        parents[vertex2Root] = vertex1Root
        ranks[vertex1Root] += 1
