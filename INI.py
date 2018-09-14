import matplotlib.pyplot as plt
from helpers import sort_dict
from Bio.Seq import Seq


def get_nucleotide_counts(dna_sequence):
    nucleotide_counts = {"A": 0, "G": 0, "T": 0, "C": 0}
    my_seq = Seq(dna_sequence)
    for key in list(nucleotide_counts.keys()):
        nucleotide_counts[key] = my_seq.count(key)
    return sort_dict(nucleotide_counts)


def show_bar_chart(input_dict={}):
    plt.bar(input_dict.keys(), input_dict.values(), color=['blue', 'red', 'green', 'yellow'])


def run(dna_sequence="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"):
    nucleotide_counts = get_nucleotide_counts(dna_sequence)
    print(nucleotide_counts)
    show_bar_chart(nucleotide_counts)

    result = f"{nucleotide_counts['A']} {nucleotide_counts['C']} {nucleotide_counts['G']} {nucleotide_counts['T']}"
    print(result)
    return result
