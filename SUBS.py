def run(input="""GATATATGCATATACTT
ATAT"""):
    params = input.splitlines()
    dna = params[0]
    motif = params[1]
    to_search = dna
    positions = []
    found = 0
    while to_search.find(motif, found) > 0:
        found = to_search.find(motif, found) + 1
        positions.append(found)
    print(positions)
    result = " ".join(str(position) for position in positions)
    print(result)
    return result
