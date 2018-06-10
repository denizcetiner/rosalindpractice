def codon_name_table():
    codon_dict = {}
    with open("rna_codon_table", "r") as codon_file:
        codons_names = codon_file.read().split()
    for i in range(0, len(codons_names), 2):
        codon = codons_names[i]
        name = codons_names[i+1]
        codon_dict[codon] = name
    # print(codon_dict)
    return codon_dict

def run(rna_string="AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"):
    codon_name_dict = codon_name_table()
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