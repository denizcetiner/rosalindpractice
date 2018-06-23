def get_smallest_end_index(actives=[]):
    smallest_index = 0
    for index in range(len(actives)):
        if get_last_element(actives[index]) < get_last_element(actives[smallest_index]):
            smallest_index = index
    return smallest_index


def get_largest_end_index(actives=[]):
    largest_index = 0
    for index in range(len(actives)):
        if get_last_element(actives[index]) > get_last_element(actives[largest_index]):
            largest_index = index
    return largest_index


def get_largest_active(actives=[]):
    largest_active = actives[0]
    for active in actives:
        if len(active) >= len(largest_active):
            largest_active = active
    return largest_active


def get_last_element(active= []):
    return active[len(active)-1]


def get_longest_and_smaller_index(element, actives=[]):
    longest_and_smaller_index = -1
    for index in range(len(actives)):
        active = actives[index]
        longest_and_smaller = actives[longest_and_smaller_index]
        if element >= get_last_element(active):
            if longest_and_smaller_index == -1 or len(active) >= len(longest_and_smaller):
                longest_and_smaller_index = index
    return longest_and_smaller_index


def discard_other_same_lengths(longest_and_smaller=[], actives=[]):
    to_discards = []
    for index in range(len(actives)):
        active = actives[index]
        if active != longest_and_smaller and len(active) == len(longest_and_smaller):
            to_discards.append(active)
    for to_discard in to_discards:
        actives.remove(to_discard)


def get_longest_increasing_subsequence(sequence=[]):
    actives = [[sequence[0]]]

    for element in sequence[1:]:
        if element == 65:
            a=1
        smallest_index = get_smallest_end_index(actives)
        largest_index = get_largest_end_index(actives)
        smallest_element = get_last_element(actives[smallest_index])
        largest_element = get_last_element(actives[largest_index])
        if element < smallest_element:
            actives.append([element])
        elif element > largest_element:
            largest_active = get_largest_active(actives)
            new_active = largest_active[:]
            new_active.append(element)
            actives.append(new_active)
        else:
            longest_and_smaller_index = get_longest_and_smaller_index(element, actives)
            longest_and_smaller = actives[longest_and_smaller_index]
            discard_other_same_lengths(longest_and_smaller, actives)
            new_active = longest_and_smaller[:]
            new_active.append(element)
            actives.append(new_active)

    longest = actives[0]
    for active in actives:
        if len(active) > len(longest):
            longest = active

    return  longest


def run(user_input="""5
5 1 4 2 3"""):
    params = user_input.splitlines()
    sequence = params[1]
    sequence_str = [int(i) for i in sequence.split(" ")]
    longest_increasing = get_longest_increasing_subsequence(sequence_str)

    print(longest_increasing)

    longest_decreasing = get_longest_increasing_subsequence(sequence_str[::-1])
    longest_decreasing = longest_decreasing[::-1]

    print(longest_decreasing)

    result = " ".join(str(i) for i in longest_increasing) + "\n" + " ".join(str(i) for i in longest_decreasing)
    print(result)
    return result
