def mate(inv1=[1, 0], inv2=[1, 0]):
    results = []
    for allele_inv1 in inv1:
        for allele_inv2 in inv2:
            results.append([allele_inv1, allele_inv2])
    print("inv1: {0}, inv2: {1} \n Results: {2}".format(inv1, inv2, results))
    return results

def mate_pairs(pairs=[]):
    results = []
    for pair in pairs:
        inv1 = pair[0]
        inv2 = pair[1]
        mate_result = mate(inv1, inv2)
        results.extend(mate_result)
    return results

def get_found_list(search_list=[], looking_for=[[]]):
    found_list = []
    for element in search_list:
        if element in looking_for:
            found_list.append(element)
    return found_list

def run(inputs="1 0 0 1 0 1", looking_for=[[0, 1], [1, 0], [1, 1]]):
    input_params = inputs.split(" ")
    homo_d = 2
    hetero = 2
    homo_r = 2

    traits = {"homo_d" : [1, 1],
              "hetero" : [1, 0],
              "homo_r" : [0, 0]}
    invs = []
    for i in range(homo_d):
        invs.append(traits["homo_d"])
    for i in range(hetero):
        invs.append(traits["hetero"])
    for i in range(homo_r):
        invs.append(traits["homo_r"])
    print(invs)

    selected_mating_pairs = []
    pair_index = 0
    all_mating_pairs = []
    for index_inv1 in range(len(invs) - 1):
        for index_inv2 in range(index_inv1 + 1, len(invs)):
            inv1 = invs[index_inv1]
            inv2 = invs[index_inv2]
            pair = [inv1, inv2]
            if pair not in all_mating_pairs:
                all_mating_pairs.append(pair)
                for i in range(int(input_params[pair_index])):
                    selected_mating_pairs.append(pair)
                pair_index += 1
    print("{0} pairs: {1}".format(len(selected_mating_pairs), selected_mating_pairs))
    expected = 0
    for pair in selected_mating_pairs:
        child_probabilities = mate(pair[0], pair[1])
        found = get_found_list(child_probabilities, looking_for)
        expected += len(found) / len(child_probabilities) * 2
    print(expected)

    return expected


run()