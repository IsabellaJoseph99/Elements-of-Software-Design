#  File: TopoSort.py

#  Description: Program that performs a topological sort on a graph after determining there is no cycle.

#  Student Name: Isabella Joseph

#  Student UT EID: ij2799

#  Partner Name:  Kaitlyn Ng

#  Partner UT EID: kn8685

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 11/30/19

#  Date Last Modified: 12/2/19

#final


class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))

    def __str__(self):
        return str(self.queue)


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


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
        if not self.has_vertex(label):
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

    def get_adj_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if self.adjMat[v][i] > 0:
                return i
        return -1

    # get a copy of the list of vertices
    def get_vertices(self):
        return self.Vertices[:]

    # do a depth first search in a graph
    def dfs(self, v):
        dfs_list = []

        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        dfs_list.append(self.Vertices[v].get_label())
        theStack.push(v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                dfs_list.append(self.Vertices[u].get_label())
                theStack.push(u)

        # the stack is empty, let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

        return dfs_list

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
        for i in range(nVert - 1):
            del self.adjMat[i][vertex_idx]

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result

    def has_cycle_helper(self, v):

      # list of visited vertices
      visited_vertices = []

      # create new stack
      theStack = Stack()

      # append input vertex to list of visited vertices
      visited_vertices.append(v)

      # push vertex onto stack
      theStack.push(v)

      while (not theStack.is_empty()):

        # get adjacent vertex. All vertices are unvisited, so it gets any vertex
        u = self.get_adj_unvisited_vertex(theStack.peek())

        # if no adjacent vertices, then pop
        if (u == -1):
          u = theStack.pop()
          self.Vertices[u].visited = True  # We were missing this statement

          # checks if vertex u is in list of visited vertices, if yes, returns true bc cycle
        elif u in visited_vertices:
          return True

        # if not in list of visited, append to list of visited
        else:
          visited_vertices.append(u)
          theStack.push(u)

      nVert = len(self.Vertices)
      for i in range(nVert):
        (self.Vertices[i]).visited = False

      return False

    def has_cycle(self):
      return self.has_cycle_helper(0)

    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort(self):
        # create a queue
        theQueue = Queue()

        while len(self.Vertices) > 0:
            # determine in degree for all vertices
            in_degree_list = []
            for i in range(len(self.Vertices)):
                in_degree = 0
                for j in range(len(self.Vertices)):
                    in_degree += self.adjMat[j][i]
                in_degree_list.append(in_degree)

            # create a list of vertices for those with in degree of zero
            vertex_list = []

            for i in range(len(self.Vertices)):
                # add vertices with in degree of zero to a list
                if in_degree_list[i] == 0:
                    vertex_list.append(self.Vertices[i].get_label())

                    # remove edges from vertices with in degree of zero
                    for j in range(len(self.Vertices)):
                        self.adjMat[i][j] = 0

            # sort vertices alphabetically, enqueue, and delete from graph
            vertex_list.sort()
            for vertex in vertex_list:
                theQueue.enqueue(vertex)
                self.delete_vertex(vertex)

        # dequeue items in queue into a list
        topo_sort = []
        for i in range(theQueue.size()):
            topo_sort.append(theQueue.dequeue())
        return topo_sort


def main():
    # create graph object
    theGraph = Graph()

    # open file for reading
    in_file = open("topo.txt", "r")

    # read number of vertices
    num_vertices = int((in_file.readline()).strip())

    # read vertices in
    for i in range(num_vertices):
        vertex = (in_file.readline()).strip()
        theGraph.add_vertex(vertex)

    # read edges
    num_edges = int(in_file.readline().strip())

    # read each edge and put in adj matrix
    start_idx = ord(theGraph.Vertices[0].get_label())

    for i in range(num_edges):
        edge = in_file.readline().strip()
        edge = edge.split()
        start = ord(edge[0]) - start_idx
        finish = ord(edge[1]) - start_idx

        # assume default weight of one
        theGraph.add_directed_edge(start, finish)

    # test if a directed graph has a cycle
    if (theGraph.has_cycle()):
        print("The Graph has a cycle.")
    else:
        print("The Graph does not have a cycle.")

    # test topological sort
    if not theGraph.has_cycle():
        vertex_list = theGraph.toposort()
        print("\nList of vertices after toposort")
        print(vertex_list)
main()