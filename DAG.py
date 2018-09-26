class Node:
    def __init__(self,name):
        self.Name = name
        self.Color = -1
        self.Visited = False
        self.Adjs = []

    def __eq__(self, other):
        if isinstance(other, int):
            return self.Name == other
        elif isinstance(other, Node):
            return self.Name == other.Name
        else:
            return False

    def add_neigh(self, adj):
        self.Adjs.append(adj)


class HeapNode:
    def __init__(self, node:Node, parent_heap):
        self.node = node
        self.parent = parent_heap

    def __eq__(self, other):
        return self.node == other


def resolve_edge(all_nodes:dict, name1:int, name2:int):
    node1 : Node
    node2 : Node

    if name1 not in all_nodes:
        node1 = Node(name1)
        all_nodes[name1] = node1
    else:
        node1 = all_nodes[name1]
    if name2 not in all_nodes:
        node2 = Node(name2)
        all_nodes[name2] = node2
    else:
        node2 = all_nodes[name2]

    node1.add_neigh(node2)


def check_cycle_for_visited(source: Node, adj: Node):
    parent = source
    while parent is not None:
        if parent == adj:
            return True
        else:
            parent = parent.parent
    return False


def check_cycle_for_adjs(source: HeapNode,  to_append:[]):
    for adj in source.node.Adjs:
        if adj.Visited and check_cycle_for_visited(source, adj):
            return True
        else:
            to_append.append(HeapNode(adj, source))


def is_acyclic(all_nodes={}):
    for key, first in all_nodes.items():
        heap = [HeapNode(first,None)]
        index_heap = 0
        while index_heap < len(heap):
            current_heap = heap[index_heap]
            current_heap.node.Visited = True
            to_append = []
            cycle = check_cycle_for_adjs(current_heap, to_append)
            if cycle:
                return False
            else:
                heap.extend(to_append)
                index_heap += 1
    return True


def extract_format(user_input:str):
    params = user_input.split("\n\n")
    graph_count = params[0]
    graphs = params[1:]

    results = []
    for graph in graphs:
        node_count = int(graph[0].split()[0])
        all_nodes = init_all_nodes(node_count)

        for graph_line in graph.splitlines()[1:]:
            elements = [int(i) for i in graph_line.split()]
            resolve_edge(all_nodes, elements[0], elements[1])

        acyclic = is_acyclic(all_nodes)
        print(acyclic)
        results.append(acyclic)
    return results


def init_all_nodes(node_count):
    all_nodes = {}
    for i in range(node_count):
        all_nodes[i+1] = Node(i+1)
    return all_nodes


def run(user_input="""3

2 1
1 2

4 4
4 1
1 2
2 3
3 1

4 3
4 3
3 2
2 1"""):
    results = extract_format(user_input)
    results_str = []
    for result in results:
        results_str.append("1" if result else "-1")
    output = " ".join(results_str)
    print(output)
    return output
