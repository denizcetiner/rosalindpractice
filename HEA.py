offset = 1


def parent(pos:int):
    if pos == 1 or pos == 2:
        return 0
    else:
        return int((pos - 1) / 2)


def swap(array:[], pos0:int, pos1):
    temp = array[pos0]
    array[pos0] = array[pos1]
    array[pos1] = temp


def max_heapify(max_heap_array:[], check_pos:int):
    largest = check_pos
    left = (2 * check_pos) + 1
    right = (2 * check_pos) + 2

    if left < len(max_heap_array) and max_heap_array[check_pos] < max_heap_array[left]:
        largest = left

    if right < len(max_heap_array) and max_heap_array[largest] < max_heap_array[right]:
        largest = right

    if largest != check_pos:
        swap(max_heap_array, largest, check_pos)
        max_heapify(max_heap_array, largest)


def build_max_heap(array:[]):
    max_heap_array = []

    for element in array:
        max_heap_array.append(element)
        max_heapify(max_heap_array, len(max_heap_array))


def run(user_input="""5
1 3 5 7 2"""):
    params = user_input.splitlines()
    array = [int(i) for i in params[1].split()]

    for i in range(len(array)-1, -1, -1):
        max_heapify(array, i)

    print(array)
    return " ".join([str(i) for i in array])
run()