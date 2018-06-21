import random
from bokeh.palettes import Spectral8, Set3, Paired
CIRCLE_SIZE=35
WIDTH=750
HEIGHT=600
class Edge:
    def __init__(self, destination):
        self.destination = destination

class Vertex:
    def __init__(self, value, **pos):
        self.value = value
        self.color = 'white'
        self.pos = pos
        self.edges = []

class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('t1', x=40, y=40)
        debug_vertex_2 = Vertex('t2', x=140, y=140)
        debug_vertex_3 = Vertex('t3', x=240, y=340)
        debug_vertex_4 = Vertex('t4', x=340, y=240)
        debug_vertex_5 = Vertex('t5', x=440, y=140)

        debug_edge_1 = Edge(debug_vertex_2)
        debug_vertex_1.edges.append(debug_edge_1)

        edge2 = Edge(debug_vertex_3)
        debug_vertex_2.edges.append(edge2)

        edge3 = Edge(debug_vertex_5)
        debug_vertex_4.edges.append(edge3)

        self.vertexes += [debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4, debug_vertex_5]

    def randomize(self, width, height, probability=50):
        def connect_verts(v0, v1):
            v0.edges.append(Edge(v1))
            v1.edges.append(Edge(v0))

        random.seed()
        ## Method for generating random verts based on JS Graphs project
        # count = 0
        # #Build a grid of verts
        # grid = []
        # row = []
        # for j in range(height):
        #     for i in range(width):
        #         row.append(Vertex('t' + str(count), x=random.randrange(CIRCLE_SIZE, WIDTH - CIRCLE_SIZE, 1), y=random.randrange(CIRCLE_SIZE, HEIGHT - CIRCLE_SIZE, 1)))
        #         count += 1
        #     grid.append(row)
        #     row = []

        # for j, r in enumerate(grid):
        #     for i, vert in enumerate(r):
        #         if (random.randrange(100) < probability and j < height - 1):
        #             connect_verts(vert, grid[j+1][i])
        #         if (random.randrange(100) < probability and i < width - 1):
        #             connect_verts(vert, grid[j][i+1])
        #         self.vertexes.append(vert)

        # New and improved method for generating random verts
        N = height * width
        for i in range(N):
            self.vertexes.append(Vertex('t' + str(i), x=random.randrange(CIRCLE_SIZE//2, WIDTH - CIRCLE_SIZE//2, 1), y=random.randrange(CIRCLE_SIZE//2, HEIGHT - CIRCLE_SIZE//2, 1)))

        for vertex in self.vertexes:
            if (random.randrange(100) < probability):
                connect_verts(vertex, self.vertexes[random.randrange(N-1)])
            if (random.randrange(100) < probability):
                connect_verts(vertex, self.vertexes[random.randrange(N-1)])

    def BFS(self):
        to_be_checked = []
        for vertex in self.vertexes:
            if (vertex.color == 'white'):
                #color = Spectral8.pop()
                r = random.randrange(11)
                while (r > len(Set3[12]) - 1):
                    r = random.randrange(11)
                color = Set3[12].pop(r)
                vertex.color = color
                to_be_checked.append(vertex)
                while(len(to_be_checked) > 0):
                    v = to_be_checked.pop(0)
                    for edge in v.edges:
                        if (edge.destination.color == 'white'):
                            to_be_checked.append(edge.destination)
                            edge.destination.color = color