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
    node2.add_neigh(node1)


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


def array_string_to_int(array_string):
    array_int = [int(i) for i in array_string]
    return array_int


def string_to_array_int(string:str):
    array_int = array_string_to_int(string.split())
    return array_int


def is_bipartite(all_nodes:[]):
    return color_all(list(all_nodes.values())[0], -1)


def color_all(source:Node, target:Node):
    heap_tree = [HeapNode(source,None)]
    i = 0
    heap_tree[0].node.Color = 0
    while i < len(heap_tree) and heap_tree[i].node != target:
        current_node = heap_tree[i].node
        current_node.Visited = True
        for node in current_node.Adjs:
            if node.Visited and node.Color == current_node.Color:
                    return -1
            elif not node.Visited:
                node.Color = (current_node.Color + 1) % 2
                heap_tree.append(HeapNode(node, heap_tree[i]))
        i += 1

    if i >= len(heap_tree):
        return 1


def clean_visited(all_nodes: []):
    for node in list(all_nodes.values()):
        node.visited = False


class HeapNode:
    def __init__(self, node:Node, parent_heap):
        self.node = node
        self.parent = parent_heap

    def __eq__(self, other):
        return self.node == other


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
        bip = is_bipartite(all_nodes)
        # print(bip)
        results.append(bip)
    return results


def init_all_nodes(node_count):
    all_nodes = {}
    for i in range(node_count):
        all_nodes[i+1] = Node(i+1)
    return all_nodes


def run(user_input="""2

3 3
1 2
3 2
3 1

4 3
1 4
3 1
1 2"""):
    results = extract_format(user_input)
    output = " ".join([str(i) for i in results])
    print(output)
    return output
