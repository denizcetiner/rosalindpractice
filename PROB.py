import math


def run(user_input="""ACGATACAA
0.129 0.287 0.423 0.476 0.641 0.742 0.783"""):
    params = user_input.splitlines()
    strand = params[0]
    gc_contents = [float(y) for y in params[1].split()]

    strand_probs = []
    for gc_content in gc_contents:
        strand_prob = 0
        for nucleotide in strand:
            if nucleotide in ["G","C"]:
                prob = gc_content / 2
                strand_prob += math.log10(prob)
            else:
                prob = (1-gc_content) /2
                strand_prob += math.log10(prob)
        print("{0} : {1}".format(gc_content, strand_prob))
        strand_probs.append(strand_prob)
    result = " ".join(str(y) for y in strand_probs)
    print(result)
    return result
