import re
from helpers import find_motif


def run(user_input="""GATATATGCATATACTT
ATAT"""):
    params = user_input.splitlines()
    dna = params[0]
    motif = params[1]
    to_search = dna
    positions = find_motif(dna, motif)

    print(positions)
    result = " ".join(str(position+1) for position in positions.keys())
    print(result)
    return result

run()