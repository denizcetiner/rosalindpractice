from helpers import transcribe_until_stop, get_protein_codon_dict


def run(rna_string="AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"):
    proteins = transcribe_until_stop(rna_string)
    proteins_nostop = [protein for protein in proteins if protein != "Stop"]
    d= get_protein_codon_dict()

    for protein in proteins_nostop:
        print("Codon: {0}, Aminoacid: {1}".format(d[protein], protein))
    result = "".join(proteins_nostop)
    print(result)
    return result


run()