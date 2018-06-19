import itertools


def run(user_input="""A C G T
2"""):
    params = user_input.splitlines()
    list_nucleotide = str(params[0]).split()
    formed_length = int(params[1])
    list_nucleotide.extend(list_nucleotide * formed_length)

    perms = itertools.permutations(list_nucleotide, formed_length)
    list_perms = []
    for perm in perms:
        str_perm = "".join(perm)
        if str_perm not in list_perms:
            list_perms.append(str_perm)
    list_perms = sorted(list_perms)

    result = "\n".join(list_perms)
    print(result)
    return result

