print("http://rosalind.info/problems/ini/")
dataset_filename = "rosalind_ini"
with open( "{0}.txt".format(dataset_filename), "r") as dataset_input:
    dna_sequence = dataset_input.read().strip()
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
with open("{0}_result.txt".format(dataset_filename), "w") as text_file:
    text_file.write(result)
    print(result)
