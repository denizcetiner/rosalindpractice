import itertools
from helpers import extract
import math


def check_overlap_directional(head="", tail=""):
    count = 0
    for i in range(len(tail), 0, -1):
        tail_control = tail[0:i]
        if head.endswith(tail_control):
            count = i
            break
    return count


def check_overlap(string1="", string2=""):
    forward_overlap = check_overlap_directional(string1, string2)
    backward_overlap = check_overlap_directional(string2, string1)
    return max(forward_overlap, backward_overlap)


def combine_pair(string1="", string2=""):
    forward_overlap = check_overlap_directional(string1, string2)
    backward_overlap = check_overlap_directional(string2, string1)
    part1 = ""
    overlap = ""
    part2 = ""
    result = ""
    if forward_overlap > backward_overlap:
        head_pos = string1.rfind(string2[0:forward_overlap-1])
        part1 = string1[0:head_pos]
        overlap = string1[head_pos:]
        part2 = string2[len(overlap):]
        result = part1 + overlap + part2
    else:
        head_pos = string2.rfind(string1[0:backward_overlap-1])
        part1 = string2[0:head_pos]
        overlap = string2[head_pos:]
        part2 = string1[len(overlap):]
        result = part1 + overlap + part2
    print(part1)
    print(overlap)
    print(part2)
    print(result + "\n")
    return result


def combine_overlaps(strings=[]):
    perms = list([list(perm) for perm in itertools.combinations(range(len(strings)), 2)])
    max_overlap_pair = []
    max_overlap_count = 0
    while len(perms) > 0:
        for index_1, index_2 in perms:
            string_1 = strings[index_1]
            string_2 = strings[index_2]
            overlap_count = check_overlap(string_1, string_2)
            if overlap_count > max_overlap_count:
                max_overlap_count = overlap_count
                max_overlap_pair = [index_1, index_2]
        max_string_1 = strings[max_overlap_pair[0]]
        max_string_2 = strings[max_overlap_pair[1]]
        new_string = combine_pair(max_string_1, max_string_2)
        # print("{0}\n{1}\n{2}\n\n".format(max_string_1, max_string_2, new_string))
        for remove_index in sorted([max_overlap_pair[0], max_overlap_pair[1]], reverse=True):
            strings.pop(remove_index)
        strings.append(new_string)
        perms = list([list(perm) for perm in itertools.combinations(range(len(strings)), 2)])
        max_overlap_pair = []
        max_overlap_count = 0
    return strings[0]


def run(user_input=""">Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC"""):
    dict_name_strand = extract(user_input)
    strands = list(dict_name_strand.values())
    result = combine_overlaps(strands)
    print(result)
    return result
