def partition(array=[]):
    if len(array) == 1 or len(array) == 0:
        return array

    pivot = array[0]
    left = []
    mid = []
    right = []
    new_array = []
    for element in array:
        if element < pivot:
            left.append(element)
        elif element == pivot:
            mid.append(element)
        else:
            right.append(element)

    partition_left = partition(left)
    partition_right = partition(right)

    partition_left.extend(mid)
    partition_left.extend(partition_right)
    return partition_left


def run(user_input="""11
2 36 5 21 8 13 11 20 5 4 1
8"""):
    params = user_input.splitlines()
    array = [int(i) for i in params[1].split()]
    sorted_array = partition(array)

    nth = int(params[2])
    i = 1
    index = 0
    minimum = sorted_array[index]
    while i < nth:
        checking = sorted_array[index]
        index += 1
        if index != min:
            minimum = checking
            i += 1
    res = sorted_array[index]
    print(res)
    return res
