from helpers import extract


def find_spliced_motif(strand, motif):
    spliced_positions = []

    strand_position = 0
    for motif_nucleotide in motif:
        for strand_index in range(strand_position, len(strand)):
            strand_nucleotide = strand[strand_index]
            if motif_nucleotide == strand_nucleotide:
                spliced_positions.append(strand_index+1)
                strand_position = strand_index + 1
                break

    return spliced_positions


def run(user_input=""">Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA"""):
    strings = list(extract(user_input).values())
    strand = strings[0]
    motif = strings[1]
    positions = find_spliced_motif(strand, motif)

    print(positions)
    result = " ".join(str(position) for position in positions)
    return result

