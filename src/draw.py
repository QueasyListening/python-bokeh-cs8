import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, ColumnDataSource, LabelSet
from bokeh.palettes import Spectral8
from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()

N = len(graph_data.vertexes)

for i, vertex in enumerate(graph_data.vertexes):
    vertex.index = i

node_indices = list(range(N))

color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)

plot = figure(title='Graph Layout Demonstration', x_range=(0, 500), y_range=(0, 500),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Oval(height=10, width=10, fill_color='color')

# graph.edge_renderer.data_source.data = dict(
#     start=[0]*N,
#     end=node_indices)

###this is drawing the edges from start to end
edge_start=[]
edge_end=[]
for vertex in graph_data.vertexes:
    for edge in vertex.edges:
        edge_start.append(vertex.index)
        edge_end.append(edge.destination.index)        

graph.edge_renderer.data_source.data = dict(
    start=edge_start,
    end=edge_end
)
### start of layout code
x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]
vertex_values = []
for vertex in graph_data.vertexes:
    vertex_values.append(vertex.value)

source = ColumnDataSource(data=dict(x_pos=x, y_pos=y, values=vertex_values))

labels = LabelSet(x='x_pos', y='y_pos', text='values', level='glyph', x_offset=5, y_offset=5, source=source, render_mode='canvas')

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)
plot.add_layout(labels)

output_file('graph.html')
show(plot)