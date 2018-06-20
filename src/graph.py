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
