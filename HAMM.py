def run(dna_strings_str = """GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT"""):
    dna_strings = dna_strings_str.splitlines()

    hamming_distance = 0
    dna_0 = dna_strings[0]
    dna_1 = dna_strings[1]
    for i in range(len(dna_0)):
        if dna_0[i] != dna_1[i]:
            hamming_distance += 1
    print(hamming_distance)
    return hamming_distance
