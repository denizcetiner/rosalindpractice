from helpers import get_protein_codon_dict, get_codon_protein_dict


def get_possible_rnas(protein_codons=[]):
    rna_possibilities = []
    possibility_count = 1
    for codons in protein_codons:
        possibility_count *= len(codons)

    for codon_counter in range(possibility_count):
        rna_possibility = []
        modulus = 1
        for codons in protein_codons:
            modulus = len(codons)
            codon = codons[codon_counter % modulus]
            rna_possibility.append(codon)
        rna_possibilities.append(rna_possibility)
    return rna_possibilities


def get_possible_rna_count(possible_codons=[], fast=True):
    modulus = 1000000
    possible_rna_count = 0
    if fast:
        possible_rna_count = 1
        for codons in possible_codons:
            possible_rna_count = (possible_rna_count * len(codons)) % modulus
    else:
        possible_rnas = get_possible_rnas(possible_codons)
        possible_rna_count = len(possible_rnas)

    return possible_rna_count


def run(user_input="MA"):
    dict_protein_codon = get_protein_codon_dict()
    dict_codon_protein = get_codon_protein_dict()

    possible_codons = []
    for protein in user_input:
        possible_codons.append(dict_protein_codon[protein])
    possible_codons.append(dict_protein_codon["Stop"])

    for codons in possible_codons:
        protein = dict_codon_protein[codons[0]]
        print("Protein: {0}".format(protein))
        print("Codon  : {0}".format(codons))

    possible_rna_count = get_possible_rna_count(possible_codons)

    print(possible_rna_count)
    return possible_rna_count

