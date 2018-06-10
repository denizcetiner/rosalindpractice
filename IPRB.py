def mate(inv1=[1, 0], inv2=[1, 0]):
    results = []
    for allele_inv1 in inv1:
        for allele_inv2 in inv2:
            results.append([allele_inv1, allele_inv2])
    print("inv1: {0}, inv2: {1} \n Results: {2}".format(inv1, inv2, results))
    return results


def run(inputs="2 2 2", looking_for=[[0, 1], [1, 0], [1, 1]]):
    input_params = inputs.split(" ")
    homo_d = int(input_params[0])
    hetero = int(input_params[1])
    homo_r = int(input_params[2])

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

    results = []
    for index_inv1 in range(len(invs) - 1):
        for index_inv2 in range(index_inv1 + 1, len(invs)):
            inv1 = invs[index_inv1]
            inv2 = invs[index_inv2]
            mate_result = mate(inv1, inv2)
            results.extend(mate_result)

    print(results)

    found = 0
    for result in results:
        if result in looking_for:
            found += 1
    probability = found / len(results)
    print("Found {0} in {1} results, probability: {2}".format(found,
                                                              len(results),
                                                              probability))
    return probability

