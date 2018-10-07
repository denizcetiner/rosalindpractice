from graphviz import Digraph


class Node:
    def __init__(self, name):
        self.name = name
        self.adjs = []

    def __eq__(self, other):
        if isinstance(other, int):
            return self.name == other
        elif isinstance(other, Node):
            return self.name == other.name
        else:
            return False

    def add_neigh(self, adj):
        if adj not in self.adjs:
            self.adjs.append(adj)


def resolve_edge(allNodes: dict, name1:int, name2:int):
    node1 : Node
    node2 : Node

    if name1 not in allNodes:
        node1 = Node(name1)
        allNodes[name1] = node1
    else:
        node1 = allNodes[name1]
    if name2 not in allNodes:
        node2 = Node(name2)
        allNodes[name2] = node2
    else:
        node2 = allNodes[name2]

    node1.add_neigh(node2)
    node2.add_neigh(node1)



def run(user_input="""6 7
1 2
2 3
6 3
5 6
2 5
2 4
4 1"""):
    allNodes = {}
    edges_string = user_input.splitlines()[1:]
    edges_list = [[int(e) for e in edge.split()] for edge in edges_string]

    for edge in edges_list:
        resolve_edge(allNodes, edge[0], edge[1])

    results = []
    for key in sorted([int(i) for i in allNodes.keys()]):
        print(key)
        results.append(len(allNodes[key].adjs))

    result = " ".join([str(i) for i in results])
    print(result)
    print(len(results))
    print(sum(results))
    return result
