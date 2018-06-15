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


def sort_dict(input_dict={}):
    result = {}
    for key in sorted(input_dict.keys()):
        result[key] = input_dict[key]
    return result


def get_codon_protein_dict():
    dict_codon_protein = {}
    with open("rna_codon_table", "r") as codon_file:
        codons_names = codon_file.read().split()
    for i in range(0, len(codons_names), 2):
        codon = codons_names[i]
        name = codons_names[i+1]
        dict_codon_protein[codon] = name
    # print(codon_dict)
    return dict_codon_protein

def get_protein_codon_dict():
    dict_protein_codon = {}
    with open("rna_codon_table", "r") as codon_file:
        codons_names = codon_file.read().split()
    for i in range(0, len(codons_names), 2):
        codon = codons_names[i]
        protein = codons_names[i+1]
        if protein in dict_protein_codon:
            dict_protein_codon[protein].append(codon)
        else:
            dict_protein_codon[protein] = [codon]
    # print(codon_dict)
    return dict_protein_codon
