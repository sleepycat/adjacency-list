def create_graph_from_file(path):
    graph = {}
    file = open(path, 'r')
    for line in file.readlines():
        vertices = line.strip().split(' ')
        if len(vertices) == 2:
            graph = add_relationship(graph, (vertices[0], vertices[1]))
    return list(graph.items())

def add_directed_edge(graph, origin, destination):
    if origin in graph:
        graph[origin].append(destination)
    else:
        graph[origin] = [destination]
    return graph

def add_relationship(graph, relation):
    origin, destination = relation
    graph = add_directed_edge(graph, origin, destination)
    graph = add_directed_edge(graph, destination, origin)
    return graph

