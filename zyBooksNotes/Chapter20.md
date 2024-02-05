# Graphs

## Graphs Introduction

Graph - Data structure for representing connections amoung items

Graphs consist of
1. Vertex (or node) - represents item in a graph
2. Edge - represents a connection between two vertices

Adjacent - Two vertices are adjacent if connected by an edge

Path - Sequence of edges leaading from a vertex to another vertex

Path Length - Number of edges in path

Distance - number of edges on the shortest path between two vertices

## Applications of Graphs

Graphs are often used to represent a geographic map.

Graphs can be used to represent relationships between products.

Graphs can represent relationships in social and professional networks

## Graph Representations: Adjacency Lists

Adjacency list - graphical represntation showing each vertex and its list of adjacent vertices

## Graph Representations: Adjacency Matrices

Adjacency Matrices - Graphical representation where each vertex is assigned to a matrix row and column and a matric element is 1 if the corresponding two vertices have an edge, or is 0 otherwise

## Graphs: Breadth-First Search

Breadth-First Search - is a traversal that visits a starting vertex, then all vertices of distance 1, then 2, and so on, without revisiting a vertex

BFS(startV) {
   Enqueue startV in frontierQueue
   Add startV to discoveredSet

   while ( frontierQueue is not empty ) {
      currentV = Dequeue from frontierQueue
      "Visit" currentV
      for each vertex adjV adjacent to currentV {
         if ( adjV is not in discoveredSet ) {
            Enqueue adjV in frontierQueue
            Add adjV to discoveredSet
         }
      }
   }
}

Discovered - Vertex that has been visited

Frontier - Vertices that have not been discovered yet

## Graphs: Depth-Frist Search

Depth-First Search - is a traversal that visits a starting index, then visits every vertex along each path starting from that vertex to the paths end before backtracking

DFS(startV) {
   Push startV to stack

   while ( stack is not empty ) {
      currentV = Pop stack
      if ( currentV is not in visitedSet ) {
         "Visit" currentV
         Add currentV to visitedSet
         for each vertex adjV adjacent to currentV
            Push adjV to stack
      }
   }
}

## Directed Graphs

Directed Graph (digraph) - consists of vertices connected by directed edges

Directed Edge - connection between a starting vertex and a terminating vertex

Path - Sequence of directed edges leading from a source vertex to a destination vertex

Cycle - Path that starts and ends at the same vertex
    1. Cyclic if the graph contains a cycle
    2. Acyclic if the graph does not contain a cycle 

## Weighted Graphs

Weighted graph - Associates a weight with each edge.

Weight / Cost - represents some numerical value between vertex items, such as cost between airports. Can be directed or undirected.

Path Length (weighted) - sum of edge weights in a path

Cycle Length - sum of edge weights in a cycle

Negative Edge Weight Cycle - has a cycle length less than 0

## Python: Graphs

[Python Code](../Graphs.py)

## Python: Breadth-First Search

[Python Code](../Trees.py)

## Python: Depth-First Search

[Python Code](../Trees.py)
 
## Python: Dijkstra's Shortest Path

Dijkstra's Algorithm computes shortest path from a given starting vertex to all other vertices in the graph

Vertex Class is extended to include two additional data members
1. Distance - Total sum of the edge weights on a path from some start vertex to the vertex
2. pred_vertex - A reference to the vertex that occurs immediatly vefore the vertex, on a path from some start vertex to the vertex

## Algorithm: Dijkstra's Shortest Path

DijkstraShortestPath(startV) {
   for each vertex currentV in graph {
      currentV⇢distance = Infinity
      currentV⇢predV = 0
      Enqueue currentV in unvisitedQueue
   }

   // startV has a distance of 0 from itself
   startV⇢distance = 0

   while (unvisitedQueue is not empty) {
      // Visit vertex with minimum distance from startV
      currentV = DequeueMin unvisitedQueue

      for each vertex adjV adjacent to currentV {
         edgeWeight = weight of edge from currentV to adjV
         alternativePathDistance = currentV⇢distance + edgeWeight
            
         // If shorter path from startV to adjV is found,
         // update adjV's distance and predecessor
         if (alternativePathDistance < adjV⇢distance) {
            adjV⇢distance = alternativePathDistance
            adjV⇢predV = currentV
         }
      }
   }
}

## Algorithm: Bellman-Ford's Shortest Path

Bellman-Ford's Shortest Path - Determines the shortest path from a start vertex to each vertex in a graph

Does not require specific order for visiting vertices during each main iteration.

## Python: Bellman-Ford's Shortest Path

def bellman_ford(graph, start_vertex):
    # Initialize all vertex distances to infinity and
    # and predecessor vertices to None.
    for current_vertex in graph.adjacency_list:
      current_vertex.distance = float('inf') # Infinity
      current_vertex.pred_vertex = None

    # start_vertex has a distance of 0 from itself
    start_vertex.distance = 0                

    # Main loop is executed |V|-1 times to guarantee minimum distances.
    for i in range(len(graph.adjacency_list)-1):
        # The main loop.
        for current_vertex in graph.adjacency_list:
            for adj_vertex in graph.adjacency_list[current_vertex]:
                edge_weight = graph.edge_weights[(current_vertex, adj_vertex)]
                alternative_path_distance = current_vertex.distance + edge_weight
                      
                # If shorter path from start_vertex to adj_vertex is found,
                # update adj_vertex's distance and predecessor
                if alternative_path_distance < adj_vertex.distance:
                   adj_vertex.distance = alternative_path_distance
                   adj_vertex.pred_vertex = current_vertex

    # Check for a negative edge weight cycle
    for current_vertex in graph.adjacency_list:
        for adj_vertex in graph.adjacency_list[current_vertex]:
             edge_weight = graph.edge_weights[(current_vertex, adj_vertex)]
             alternative_path_distance = current_vertex.distance + edge_weight

             # If shorter path from start_vertex to adj_vertex is still found,
             # a negative edge weight cycle exists
             if alternative_path_distance < adj_vertex.distance:
                return False

    return True

## Topological Sort

Topological Sort - sort of a directed, acyclic graph produces a list of the graphs vertices such that for every edge from a vertex x to a vertex y, x comes before y in the list.

Example - Course prerequisites

GraphTopologicalSort(graph) {
   resultList = empty list of vertices
   noIncoming = list of all vertices with no incoming edges
   remainingEdges = list of all edges in the graph

   while (noIncoming is not empty) {
      currentV = remove any vertex from noIncoming
      Add currentV to resultList
      outgoingEdges = remove currentV's outgoing edges from remainingEdges
      for each edge currentE in outgoingEdges {
         inCount = GraphGetIncomingEdgeCount(remainingEdges, currentE⇢toVertex)
         if (inCount == 0)
            Add currentE⇢toVertex to noIncoming
      }
   }
   return resultList
}

## Minimum Spanning Tree

Minimum Spanning Tree - Subset of the graphs edges that connect all vertices in the graph together with the minimim sum of edge weights.

Must be connected and weighted.

Kruskal's Minimum Spanning Tree Algorithm - determines subset of the graph's edges that connect all vertices in an undirected graph with the minimum sum of edge weights. Kruskal's minimum spanning tree algorithm uses 3 collections:
1. An edge list initialized with all edges in the graph.
2. A collection of vertex sets that represent the subsets of vertices connected by current set of edges in the minimum spanning tree. Initially, the vertex sets consists of one set for each vertex.
3. A set of edges forming the resulting minimum spanning tree.

## Python: Minimum Spanning Tree

class EdgeWeight:
    def __init__(self, from_vertex, to_vertex, weight):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight
    
    # Only edge weights are used in the comparisons that follow
    
    def __eq__(self, other):
        return self.weight == other.weight
    
    def __ge__(self, other):
        return self.weight >= other.weight
    
    def __gt__(self, other):
        return self.weight > other.weight

    def __le__(self, other):
        return self.weight <= other.weight
    
    def __lt__(self, other):
        return self.weight < other.weight
    
    def __ne__(self, other):
        return self.weight != other.weight

# Stores a collection of vertex sets, which collectively store all vertices in a
# graph. Each vertex is in only one set in the collection.
class VertexSetCollection:
    def __init__(self, all_vertices):
        self.vertex_map = dict()
        for vertex in all_vertices:
            vertex_set = set()
            vertex_set.add(vertex)
            self.vertex_map[vertex] = vertex_set

    def __len__(self):
        return len(self.vertex_map)

    # Gets the set containing the specified vertex
    def get_set(self, vertex):
        return self.vertex_map[vertex]

    # Merges two vertex sets into one
    def merge(self, vertex_set1, vertex_set2):
        # First create the union
        merged = vertex_set1.union(vertex_set2)
        # Now remap all vertices in the merged set
        for vertex in merged:
            self.vertex_map[vertex] = merged

# Returns a list of edges representing the graph's minimum spanning tree.
# Uses Kruskal's minimum spanning tree algorithm.
def minimum_spanning_tree(graph):
    # edge_list starts as a list of all edges from the graph
    edge_list = []
    for edge in graph.edge_weights:
        edge_weight = EdgeWeight(edge[0], edge[1], graph.edge_weights[edge])
        edge_list.append(edge_weight)
    # Turn edge_list into a priority queue (min heap)
    heapq.heapify(edge_list)

    # Initialize the collection of vertex sets
    vertex_sets = VertexSetCollection(graph.adjacency_list)

    # result_list is initially an empty list
    result_list = []

    while len(vertex_sets) > 1 and len(edge_list) > 0:
        # Remove edge with minimum weight from edge_list
        next_edge = heapq.heappop(edge_list)
        
        # set1 = set in vertex_sets containing next_edge's 'from' vertex
        set1 = vertex_sets.get_set(next_edge.from_vertex)
        # set2 = set in vertex_sets containing next_edge's 'to' vertex
        set2 = vertex_sets.get_set(next_edge.to_vertex)
        
        # If the 2 sets are distinct, then merge
        if set1 is not set2:
            # Add next_edge to result_list
            result_list.append(next_edge)
            # Merge the two sets within the collection
            vertex_sets.merge(set1, set2)

    return result_list

## All Pairs Shortest Path

All Pairs Shortest Path - Determines the shortest path between all possible paris of vertices in a graph

## Python: All Pairs Shortest Path

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}
    
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []
    
    def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)
    
    def add_undirected_edge(self, vertex_a, vertex_b, weight = 1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    # Returns the vertex in this graph with the specified label, or None
    # if no such vertex exists.
    def get_vertex(self, vertex_label):
        for vertex in self.adjacency_list:
            if vertex.label == vertex_label:
                return vertex
        return None

    # Returns a list of all vertices in this graph
    def get_vertex_list(self):
        return list(self.adjacency_list)

    # Returns a list of all edges incoming to the specified vertex
    # Each edge is a tuple of the form (from_vertex, to_vertex)
    def get_incoming_edges(self, vertex):
        incoming = []
        for edge in self.edge_weights:
            if edge[1] is vertex:
                incoming.append(edge)
        return incoming

# Implementation of Floyd-Warshall all-pairs shortest path
def all_pairs_shortest_path(graph):
    vertices = graph.get_vertex_list()
    num_vertices = len(vertices)

    # Initialize dist_matrix to a num_vertices x num_vertices matrix 
    # with all values set to infinity
    dist_matrix = []
    for i in range(0, num_vertices):
        dist_matrix.append([float("inf")] * num_vertices)

    # Set each distance for vertex to same vertex to 0
    for i in range(0, num_vertices):
        dist_matrix[i][i] = 0

    # Finish matrix initialization
    for edge in graph.edge_weights:
        dist_matrix[vertices.index(edge[0])][vertices.index(edge[1])] = graph.edge_weights[edge]

    # Loop through vertices
    for k in range(0, num_vertices):
        for toIndex in range(0, num_vertices):
            for fromIndex in range(0, num_vertices):
                currentLength = dist_matrix[fromIndex][toIndex]
                possibleLength = dist_matrix[fromIndex][k] + dist_matrix[k][toIndex]
                if possibleLength < currentLength:
                    dist_matrix[fromIndex][toIndex] = possibleLength

    return dist_matrix

def reconstruct_path(graph, start_vertex, end_vertex, dist_matrix):
    vertices = graph.get_vertex_list()
    start_index = vertices.index(start_vertex)
    path = []
    
    # Backtrack from the ending vertex
    current_index = vertices.index(end_vertex)
    while current_index != start_index:
        incoming_edges = graph.get_incoming_edges(vertices[current_index])
        
        found_next = False
        for current_edge in incoming_edges:
            expected = dist_matrix[start_index][current_index] - graph.edge_weights[current_edge]
            actual = dist_matrix[start_index][vertices.index(current_edge[0])]
            if expected == actual:
                # Update current vertex index
                current_index = vertices.index(current_edge[0])
                
                # Prepend current_edge to path
                path = [current_edge] + path
                
                # The next vertex in the path was found
                found_next = True
                
                # The correct incoming edge was found, so break the inner loop
                break

        if found_next == False:
            return None # no path exists

    return path