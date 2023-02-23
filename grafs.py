import networkx as nx
import matplotlib.pyplot as plt
from networkx import Graph
from networkx import get_edge_attributes
from networkx import spring_layout
from networkx import draw_networkx_nodes
from networkx import draw_networkx_labels
from networkx import draw_networkx_edges
from networkx import draw_networkx_edge_labels


grafs = Graph()

grafs.add_edge("0","2",weight=3)
grafs.add_edge("1","0",weight=5)
grafs.add_edge("1","2",weight=6)
grafs.add_edge("2","3",weight=8)

poz = spring_layout(grafs)
svari=get_edge_attributes(grafs, "weight")

draw_networkx_nodes(grafs, poz)
draw_networkx_labels(grafs, poz)
draw_networkx_edges(grafs, poz)
draw_networkx_edge_labels(grafs, poz, svari)


plt.show()