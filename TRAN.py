from helpers import extract, get_complement_dict


complements = get_complement_dict()
purines = ["A", "G"]
pyrimidines = ["C", "T"]


def is_transition(nucleotide1="A", nucleotide2="G"):
    if nucleotide1 in purines and nucleotide2 in purines:
        return True
    elif nucleotide1 in pyrimidines and nucleotide2 in pyrimidines:
        return True
    else:
        return False


def run(user_input=""">Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT"""):
    strands = list(extract(user_input).values())
    strand1 = strands[0]
    strand2 = strands[1]

    transitions = []
    transversions =[]

    for strand_index in range(len(strand1)):
        nucleotide1 = strand1[strand_index]
        nucleotide2 = strand2[strand_index]
        if nucleotide1 == nucleotide2:
            continue
        elif is_transition(nucleotide1, nucleotide2):
            transitions.append(strand_index)
        else:
            transversions.append(strand_index)

    result = len(transitions) / len(transversions)
    print(result)
    return result

