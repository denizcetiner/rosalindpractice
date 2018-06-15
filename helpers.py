import re


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


def find_motif(strand="GATATATGCATATACTT", motif="ATAT"):
    positions = {}
    strand_index = 0
    while re.search(motif, strand[strand_index:]) is not None:
        m = re.search(motif, strand[strand_index:])
        start = strand_index + m.start()
        content = m.group()
        if start not in positions:
            positions[start] = content
        strand_index = start+1
    return positions
