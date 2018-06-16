from helpers import get_complement


def run(dna_strand = "AAAACCCGGT"):
    print(dna_strand)

    complement_strand = get_complement(dna_strand)
    complement_reversed = complement_strand[::-1]

    print(complement_reversed)
    return complement_reversed
