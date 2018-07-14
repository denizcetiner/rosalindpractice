from helpers import extract, get_all_substrings


def find_shortest_values_name(name_strand_dict={}):
    shortest_name = list(name_strand_dict.keys())[0]
    shortest_length = len(name_strand_dict[shortest_name])

    for name, strand in name_strand_dict.items():
        if len(strand) < shortest_length:
            shortest_name = name
            shortest_length = len(strand)
    return shortest_name


def exists_in_all(name_strand_dict={}, substrings=[]):
    names = list(name_strand_dict.keys())
    names_count = len(names)
    for substring in substrings:
        existing_count = 0
        for name in names:
            strand = name_strand_dict[name]
            if substring in strand:
                existing_count += 1
            else:
                break
        # print("names_count: {0}, existing_count: {1}".format(names_count, existing_count))
        if existing_count == names_count:
            return substring



def run(input_strands=""">Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""):
    name_strand_dict = extract(input_strands)
    shortest_name = find_shortest_values_name(name_strand_dict)
    shortest_strand = name_strand_dict[shortest_name]
    substrings = get_all_substrings(shortest_strand)
    substrings.sort(key=len, reverse=True)
    # print(substrings)
    result = exists_in_all(name_strand_dict, substrings)
    print(result)
    return result
