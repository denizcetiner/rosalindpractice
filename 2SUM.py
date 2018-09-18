def get2sum(array:[]) -> []:
    ht = {}
    for i in range(0, len(array)):
        ht[array[i]] = i

    for k in range(0, len(array)):
        check = array[k]
        if -check not in ht or ht[-check]==k:
            continue
        else:
            return " ".join([str(k+1), str(ht[-check]+1)])
    return str(-1)


def run(user_input="""4 5
2 -3 4 10 5
8 2 4 -2 -8
-5 2 3 2 -4
5 4 -5 6 8"""):
    params = user_input.splitlines()
    arrays_string = params[1:]
    arrays = []
    for array_string in arrays_string:
        array = [int(i) for i in array_string.split()]
        arrays.append(array)

    results = []
    for array in arrays:
        index_2sum = get2sum(array)
        print(index_2sum)
        results.append(index_2sum)
    return "\n".join(results)
