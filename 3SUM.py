def get3sum(array: []) -> []:
    ht1_sum_index = {}
    for i in range(0, len(array)):
        ht1_sum_index[array[i]] = [i]

    ht2_sum_indexes = {}
    for k in range(0, len(array)):
        check = array[k]
        for sums, indexes in ht1_sum_index.items():
            if k in indexes:
                continue
            else:
                new_sum = sums + check
                new_indexes = indexes + [k]
                ht2_sum_indexes[new_sum] = new_indexes

    for k in range(0, len(array)):
        check = array[k]
        if (-check not in ht2_sum_indexes) or (k in ht2_sum_indexes[-check]):
            continue
        else:
            indexes = ht2_sum_indexes[-check]
            indexes_3 = indexes + [k]
            print(
                f"{indexes_3[0]}:{array[indexes_3[0]]}, {indexes_3[1]}:{array[indexes_3[1]]}, {indexes_3[2]}:{array[indexes_3[2]]}")
            res = [str(i + 1) for i in (sorted(indexes + [k]))]
            return " ".join(res)

    return "-1"


def run(user_input="""4 5
2 -3 4 10 5
8 -6 4 -2 -8
-5 2 3 2 -4
2 4 -5 6 8"""):
    params = user_input.splitlines()
    arrays_string = [line.split() for line in params[1:]]
    arrays = [[int(i) for i in array_string] for array_string in arrays_string]

    results = []
    for array in arrays:
        res = get3sum(array)
        # print(res)
        results.append(res)

    output = "\n".join(results)
    return output
