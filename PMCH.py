from helpers import extract


factorials = {0: 1, 1: 1}


def factorial(n: int):
    if n in factorials:
        return factorials[n]
    else:
        factorials[n] = n * factorial(n-1)
        return factorials[n]


def run(user_input=""">Rosalind_23
AGCUAGUCAU"""):
    dict_name_strand = extract(user_input)
    strand = ""
    strand = str(list(dict_name_strand.values())[0])
    gc_pairs = min(strand.count("G"), strand.count("C"))
    au_pairs = min(strand.count("A"), strand.count("U"))
    pmch_count = factorial(gc_pairs) * factorial(au_pairs)
    print(pmch_count)
    return pmch_count
