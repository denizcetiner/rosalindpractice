from helpers import extract

def run(dna_strings=""">Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""):
    dna_dict = extract(dna_strings)
    dna_gc_dict = {}
    for dna_name, dna_string in dna_dict.items():
        g_count = dna_string.count("G")
        c_count = dna_string.count("C")
        ratio = (g_count + c_count) * 100 / len(dna_string)
        dna_gc_dict[dna_name] = float("{0:.6f}".format(ratio))
    print(dna_gc_dict)
    max_gc_dna = max(dna_gc_dict, key=dna_gc_dict.get)
    result = ("{0}\n{1}".format(max_gc_dna, dna_gc_dict[max_gc_dna]))
    print(result)
    return result
