import matplotlib.pyplot as plt


def get_nucleotide_counts(dna_sequence):
    nucleotide_counts = {"A": 0, "G": 0, "T": 0, "C": 0}
    for nucleotide in dna_sequence:
        if nucleotide in nucleotide_counts:
            nucleotide_counts[nucleotide] += 1
        else:
            nucleotide_counts[nucleotide] = 1
    return sort_dict(nucleotide_counts)


def sort_dict(input_dict={}):
    result = {}
    for key in sorted(input_dict.keys()):
        result[key] = input_dict[key]
    return result


def show_bar_chart(input_dict={}):
    plt.bar(input_dict.keys(), input_dict.values(), color=['blue', 'red', 'green', 'yellow'])


def run(dna_sequence="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"):
    nucleotide_counts = get_nucleotide_counts(dna_sequence)
    print(nucleotide_counts)
    show_bar_chart(nucleotide_counts)

    result = "{0} {1} {2} {3}".format(nucleotide_counts["A"],
                                      nucleotide_counts["C"],
                                      nucleotide_counts["G"],
                                      nucleotide_counts["T"])
    return result
