def get_monisotopic_mass_table(filename="""filename""") -> {}:
    values={}
    with open("monoisotopic_mass_table.txt") as file:
        for line in file:
            (key, val) = line.split()
            values[str(key)] = float(val)
    return values


def run(user_input="""SKADYEK"""):
    proteins = user_input

    mmt = get_monisotopic_mass_table()

    total_mass = 0
    for protein in proteins:
        total_mass += mmt[protein]

    print(total_mass)
    result = "{0:.3f}".format(total_mass)
    print(result)
    return result
