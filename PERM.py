import itertools


def run(user_input="""3"""):
    permutation_length = int(user_input)
    permutation_source = []
    for i in range(permutation_length):
        permutation_source.append(i+1)
    permutations = itertools.permutations(permutation_source, permutation_length)
    permutations_list = []
    for combination in permutations:
        permutations_list.append(combination)

    result = "{0}\n".format(len(permutations_list))
    for combination in permutations_list:
        line = " ".join(str(content) for content in combination)
        print(line)
        result += "{0}\n".format(line)

    return result
