def mod2(ias):
    return ias % 2


def merge_sort(array=[]):
    mid = int(len(array) / 2)
    if mid == 0:
        return array

    new_array = []
    array0 = merge_sort(array[0:mid])
    array1 = merge_sort(array[mid:])
    arrays = [array0, array1]
    indexes = [0, 0]

    incremented_array_switch = 0
    while indexes[0] < len(arrays[0]) or indexes[1] < len(arrays[1]):
        ias = incremented_array_switch

        array_inc = arrays[mod2(ias)]
        array_other = arrays[mod2(ias+1)]

        i_inc = indexes[mod2(ias)]
        i_other = indexes[mod2(ias+1)]

        if i_inc == len(array_inc):
            incremented_array_switch += 1
            continue

        element_inc = array_inc[i_inc % len(array_inc)]
        element_other = array_other[i_other % len(array_other)]

        if element_inc <= element_other or i_other == len(array_other):
            new_array.append(element_inc)
            indexes[mod2(ias)] += 1
        else:
            incremented_array_switch += 1
    return new_array




def run(user_input="""10
20 19 35 -18 17 -20 20 1 4 4"""):
    params = user_input.splitlines()
    array0 = [int(i) for i in params[1].split()]
    new_array = merge_sort(array0)
    print(new_array)
    result = " ".join([str(i) for i in new_array])
    return result


run()

