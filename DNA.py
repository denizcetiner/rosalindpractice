def run(dna_sequence="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"):
    nucleotide_counts = {"A": 0, "G": 0, "T": 0, "C": 0}
    for nucleotide in dna_sequence:
        if nucleotide in nucleotide_counts:
            nucleotide_counts[nucleotide] += 1
        else:
            nucleotide_counts[nucleotide] = 1
    print(nucleotide_counts)
    result = "{0} {1} {2} {3}".format(nucleotide_counts["A"],
                                      nucleotide_counts["C"],
                                      nucleotide_counts["G"],
                                      nucleotide_counts["T"])
    return result
