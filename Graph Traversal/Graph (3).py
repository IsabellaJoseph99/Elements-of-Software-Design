#  File: Graph.py

#  Description: Program that adds functions to the graph class

#  Student Name: Isabella Joseph

#  Student UT EID: ij2799

#  Partner Name: Kaitlyn Ng

#  Partner UT EID: kn8685

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 11/23/19

#  Date Last Modified: 11/25/19

#final

class Stack (object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append (item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return (len (self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len (self.stack))


class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty (self):
        return (len (self.queue) == 0)

    # return the size of the queue
    def size (self):
        return (len (self.queue))

    def __str__(self):
        return str(self.queue)


class Vertex (object):
    def __init__ (self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited (self):
        return self.visited

    # determine the label of the vertex
    def get_label (self):
        return self.label

    # string representation of the vertex
    def __str__ (self):
        return str (self.label)


class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == (self.Vertices[i]).get_label():
                return True
        return False

    # get index from vertex label
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == (self.Vertices[i]).get_label():
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if (not self.has_vertex(label)):
            self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight(self, fromVertexLabel, toVertexLabel):
        if self.has_vertex(fromVertexLabel) and self.has_vertex(toVertexLabel):
            from_idx = self.get_index(fromVertexLabel)
            to_idx = self.get_index(toVertexLabel)
            edge_weight = self.adjMat[from_idx][to_idx]
            return edge_weight
        return -1

    # get a list of immediate neighbors that you can go to from a vertex
    # return empty list if there are none
    def get_neighbors(self, vertexLabel):
        neighbors = []
        nVert = len(self.Vertices)
        if self.has_vertex(vertexLabel):
            idx = self.get_index(vertexLabel)
            for i in range(nVert):
                if self.adjMat[idx][i] != 0:
                    neighbor_idx = i
                    neighbors.append(neighbor_idx)
        return neighbors

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # get a copy of the list of vertices
    def get_vertices(self):
        return self.Vertices[:]

    # do a depth first search in a graph
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)

        # the stack is empty, let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # do a breadth first search in a graph
    def bfs(self, v):
        # create the Stack
        theQueue = Queue()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theQueue.enqueue(v)

        curr = v
        # visit all the other vertices according to depth
        while not theQueue.is_empty():
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(curr)
            if u == -1:
                curr = theQueue.dequeue()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theQueue.enqueue(u)

        # the stack is empty, let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # delete an edge from the adjacency matrix
    def delete_edge(self, fromVertexLabel, toVertexLabel):
        from_idx = self.get_index(fromVertexLabel)
        to_idx = self.get_index(toVertexLabel)
        self.adjMat[from_idx][to_idx] = 0
        self.adjMat[to_idx][from_idx] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex(self, vertexLabel):
        vertex_idx = self.get_index(vertexLabel)
        nVert = len(self.Vertices)

        # delete from list of vertices
        del self.Vertices[vertex_idx]

        # delete row
        del self.adjMat[vertex_idx]

        # delete column
        for i in range(nVert-1):
            del self.adjMat[i][vertex_idx]


def main():
    # create graph object
    cities = Graph()

    # open file for reading
    in_file = open("graph.txt", "r")

    # read number of vertices
    num_vertices = int((in_file.readline()).strip())

    # read vertices in
    for i in range(num_vertices):
        city = (in_file.readline()).strip()
        cities.add_vertex(city)

    # read edges
    num_edges = int(in_file.readline().strip())

    # read each edge and put in adj matrix
    for i in range (num_edges):
        edge = in_file.readline().strip()
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])

        cities.add_directed_edge(start, finish, weight)

    # read starting vertex for bfs and dfs
    start_vertex = in_file.readline().strip()

    # get start index
    start_index = cities.get_index(start_vertex)

    # test depth first search
    print('\nDepth First Search')
    cities.dfs(start_index)

    # test breadth first search
    print('\nBreadth First Search')
    cities.bfs(start_index)

    # test deletion of an edge
    print('\nDeletion of an edge')
    cities.delete_edge('Atlanta', 'Dallas', )
    cities.delete_edge('Kansas City', 'Chicago')
    cities.delete_edge('San Francisco', 'New York')

    print('\nAdjacency Matrix')
    for i in range (num_vertices):
        for j in range (num_vertices):
            print(cities.adjMat[i][j], end=' ')
        print()
    print()

    # test deletion of a vertex
    print('Deletion of a vertex')
    cities.delete_vertex('Denver')

    print('\nList of Vertices')
    for vertex in cities.get_vertices():
        print(vertex.get_label())

    print('\nAdjacency Matrix')
    for i in range (num_vertices-1):
        for j in range (num_vertices-1):
            print(cities.adjMat[i][j], end=' ')
        print()


if __name__ == "__main__":
    main()