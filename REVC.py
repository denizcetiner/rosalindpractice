def run(dna_strand = "AAAACCCGGT"):


    complements = {"A": "T", "G": "C"}
    revd = dict()
    for i in complements.items():
        revd[i[1]] = i[0]
    complements.update(revd)

    complement_strand = []
    for nt in dna_strand:
        complement_strand.append(complements[nt])
    complement_reversed = complement_strand[::-1]

    print(dna_strand)
    print("".join(complement_strand))
    str_complement_reversed = "".join(complement_reversed)
    print(str_complement_reversed)
    return str_complement_reversed
