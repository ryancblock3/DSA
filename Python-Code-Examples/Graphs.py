class Graph:
    def __init__(self):
        # Initialize an empty adjacency list to store the graph structure
        self.adj_list = {}

    def print_graph(self):
        # Print the graph by iterating over each vertex and its adjacent vertices
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
    
    def add_vertex(self, vertex):
        # Add a new vertex to the graph if it doesn't already exist
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True  # Return True to indicate that the vertex was added
        return False  # Return False if the vertex already exists
    
    def add_edge(self, v1, v2):
        # Add an undirected edge between two vertices if they both exist in the graph
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True  # Return True to indicate that the edge was added
        return False  # Return False if any of the vertices doesn't exist
    
    def remove_edge(self, v1, v2):
        # Remove an edge between two vertices if it exists
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                # Try to remove the vertices from each other's adjacency lists
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
                return True  # Return True to indicate that the edge was removed
            except ValueError:
                pass
        return False  # Return False if the edge doesn't exist
    
    def remove_vertex(self, vertex):
        # Remove a vertex and its associated edges from the graph if it exists
        if vertex in self.adj_list.keys():
            # Iterate over the adjacent vertices and remove the current vertex from their lists
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]  # Delete the vertex from the graph
            return True  # Return True to indicate that the vertex was removed
        return False  # Return False if the vertex doesn't exist
    
#Testing Constructor & Add Vertex

# my_graph = Graph()
# my_graph.add_vertex('A')
# my_graph.print_graph()
    
# Testing Add Edge
    
# my_graph = Graph()
# my_graph.add_vertex(1)
# my_graph.add_vertex(2)
# my_graph.add_edge(1,2)
# my_graph.print_graph()
    
# Testing Remove Edge
    
# my_graph = Graph()
# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_edge('A','B')
# my_graph.add_edge('B','C')
# my_graph.add_edge('C','A')
# my_graph.print_graph() 
# my_graph.remove_edge('A','B')
# my_graph.print_graph()
    
# Testing Remove Vertex
    
# my_graph = Graph()
# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_vertex('D')
# my_graph.add_edge('A','B')
# my_graph.add_edge('A','C')
# my_graph.add_edge('A','D')
# my_graph.add_edge('B','D')
# my_graph.add_edge('C','D')
# my_graph.print_graph()
# my_graph.remove_vertex('D')
# my_graph.print_graph()


