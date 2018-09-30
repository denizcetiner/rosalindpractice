def binary_search(search_list:[], begin, end, target):
    mid_index = int((begin + end) / 2)
    mid_element = search_list[mid_index]
    if mid_element == target:
        return mid_index

    if begin == end or begin+1 == end:
        return -2

    if mid_element < target:
        return binary_search(search_list, mid_index, end, target)
    elif mid_element > target:
        return binary_search(search_list, begin, mid_index, target)


def run(user_input="""5
6
10 20 30 40 50
40 10 35 15 40 20"""):
    params = user_input.splitlines()
    search_list = [int(i) for i in params[2].split()]
    search_targets = [int(i) for i in params[3].split()]

    search_results = []
    for target in search_targets:
        search_result = binary_search(search_list, 0, len(search_list)-1, target) + 1
        search_results.append(str(search_result))

    result = " ".join(search_results)
    print(result)
    return result
