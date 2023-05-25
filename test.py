from graph import *
graph = Graph()
graph.create_graph(3)
graph.show_graph()
ruta = graph.find_way_between_two_nodes(1,3)
print(ruta)