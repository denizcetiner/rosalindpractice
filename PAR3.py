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

    #partition_left = partition(left)
    #partition_right = partition(right)

    left.extend(mid)
    left.extend(right)
    return left


def run(user_input="""9
7 2 5 6 1 3 9 4 8"""):
    params = user_input.splitlines()
    array = [int(i) for i in params[1].split()]
    array = partition(array)
    print(array)
    return " ".join([str(i) for i in array])
