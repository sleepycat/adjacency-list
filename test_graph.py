from graph import add_directed_edge, add_relationship, create_graph_from_file

def test_add_directed_edge():
    graph = add_directed_edge({}, 0, 1)
    assert graph == {0: [1]}

def test_add_relationship():
    graph = add_relationship({}, (0, 1))
    assert graph == {0: [1], 1: [0]}

def test_create_graph():
    graph = create_graph_from_file('./test_data')
    assert graph == [('0', ['1']), ('1', ['0', '2', '8']), ('2', ['1', '3']), ('8', ['1']), ('3', ['2'])]
