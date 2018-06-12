def extract(dna_strings=""):
    dna_dict = {}
    current_dna_name = ""
    for line in dna_strings.splitlines():
        if line.startswith(">"):
            current_dna_name = line.replace(">", "")
            dna_dict[current_dna_name] = ""
        else:
            dna_dict[current_dna_name] += line.strip()
    return dna_dict


class Node:

    def __init__(self, name, strand):
        self.dna_name = name
        self.dna_strand = strand
        self.links = []
        self.first_char = strand[0]
        self.last_char = strand[len(strand)-1]


def check_overlap(n1: Node, n2: Node, k):
    strand_length = len(n1.dna_strand)
    if n1.dna_strand[0:k] == n2.dna_strand[-k:]:
        n2.links.append(n1)
    if n2.dna_strand[0:k] == n1.dna_strand[-k:]:
        n1.links.append(n2)


def overlap_graphs(nodes, k=3):
    for first in range(len(nodes)-1):
        first_node = nodes[first]
        for second in range(first+1, len(nodes)):
            second_node = nodes[second]
            check_overlap(first_node, second_node, k)


def reset_node_visit(nodes):
    for node in nodes:
        node.visited = False


def get_edges(nodes):
    edges = []
    for node in nodes:
        for link in node.links:
            edges.append([node, link])
    return edges

def run(input=""">Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG"""):
    dna_name_strings = extract(input)
    nodes = []
    for name, strand in dna_name_strings.items():
        n = Node(name, strand)
        nodes.append(n)
    reset_node_visit(nodes)
    overlap_graphs(nodes)
    edges = get_edges(nodes)
    result = ""
    for n1, n2 in edges:
        line = "{0} {1}".format(n1.dna_name, n2.dna_name)
        print("{0} {2} {1} {3}".format(n1.dna_name, n2.dna_name, n1.last_char, n2.first_char))
        result += line + "\n"
    return result
