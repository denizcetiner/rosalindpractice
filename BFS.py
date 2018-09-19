class Node:
    def __init__(self, name):
        self.name = name
        self.adjs = []
        self.visited = False

    def insert_adj(self, other):
        if other not in self.adjs:
            self.adjs.append(other)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.name == other
        elif isinstance(other, Node):
            return self.name == other.name
        return False


class HeapNode:
    def __init__(self, node:Node, parent_heap):
        self.node = node
        self.parent = parent_heap

    def __eq__(self, other):
        return self.node == other


def resolve_directed_edge(all_nodes:{}, n1:Node, n2:Node):
    if n1.name not in all_nodes:
        all_nodes[n1.name] = n1
    if n2.name not in all_nodes:
        all_nodes[n2.name] = n2
    n1.insert_adj(n2)


def target_distance(source:Node, target:Node):
    heap_tree = [HeapNode(source,None)]
    i = 0
    while i < len(heap_tree) and heap_tree[i].node != target:
        current_node = heap_tree[i].node
        current_node.visited = True
        for node in current_node.adjs:
            if not node.visited:
                heap_tree.append(HeapNode(node, heap_tree[i]))
        i += 1

    if i >= len(heap_tree) or heap_tree[i].node.visited:
        return -1
    else:
        target_heap_node = heap_tree[i]
        parent = target_heap_node
        depth = 0
        while parent.node != source:
            depth += 1
            parent = parent.parent
        return depth


def clean_visited(all_nodes:{}):
    for node in list(all_nodes.values()):
        node.visited = False


def run(user_input="""6 6
4 6
6 5
4 3
3 5
2 1
1 4"""):
    params = user_input.splitlines()
    node_count = int(params[0].split()[0])
    all_nodes = {}
    for i in range(node_count):
        all_nodes[i+1] = Node(i+1)

    edges = [[int(i) for i in line.split()] for line in params[1:]]

    for edge in edges:
        resolve_directed_edge(all_nodes, all_nodes[edge[0]], all_nodes[ edge[1]])

    results = []
    for i in range(node_count):
        clean_visited(all_nodes)
        res = target_distance(all_nodes[1], all_nodes[i+1])
        results.append(str(res))
    result = " ".join(results)
    print(result)
    return result

run()