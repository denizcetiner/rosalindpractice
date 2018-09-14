graphs = []


def run(user_input="""10
1 2
2 8
4 10
5 9
6 10
7 9"""):
    user_input_lines = user_input.splitlines()
    node_count = user_input_lines[0]
    for n1, n2 in [line.split() for line in user_input_lines[1:]]:
        graph1 = []
        graph2 = []
        if len(graphs) == 0:
            graph = [n1, n2]
            graphs.append(graph)
        else:
            for graph in graphs:
                if graph is None:
                    aasdf = 1
                if n1 in graph:
                    graph1 = graph
                if n2 in graph:
                    graph2 = graph
            if len(graph1) == 0 and len(graph2) > 0:
                graph2.append(n1)
            elif len(graph2) == 0 and len(graph1) > 0:
                graph1.append(n2)
            elif len(graph1) > 0 and len(graph2) > 0:
                new_graph = graph1[:]
                new_graph.extend(graph2)
                graphs.append(new_graph)
                graphs.remove(graph1)
                graphs.remove(graph2)
            else:
                graphs.append([n1, n2])

    for n in range(1, int(node_count)+1, 1):
        str_n = str(n)
        graph_n = []
        for graph in graphs:
            if str_n in graph:
                graph_n = graph
        if len(graph_n) == 0:
            graphs.append([str_n])

    result = len(graphs) - 1
    print(result)
    return result
