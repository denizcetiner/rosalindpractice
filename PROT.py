from helpers import get_codon_protein_dict

def run(rna_string="AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"):
    codon_name_dict = get_codon_protein_dict()
    aminoacids = []
    for i in range(0, len(rna_string), 3):
        print(i)
        codon = rna_string[i:i+3]
        aminoacid = codon_name_dict[codon]
        print("Codon: {0}, Aminoacid: {1}".format(codon, aminoacid))
        if  aminoacid != "Stop":
            aminoacids.append(aminoacid)
        else:
            break
    result = "".join(aminoacids)
    print(result)
    return result