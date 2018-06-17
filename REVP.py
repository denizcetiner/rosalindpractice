from helpers import extract, get_dict_pos_substring, get_complement


def is_reverse_palindrome(strand=""):
    revc = get_complement(strand)[::-1]
    if strand == revc:
        return True
    else:
        return False

def run(user_input=""">Rosalind_24
TCAATGCATGCGGGTCTATATGCAT"""):
    strand = list(extract(user_input).values())[0]

    dict_pos_substrings = get_dict_pos_substring(strand)
    print(dict_pos_substrings)

    reverse_palindromes = []

    for position, substrings in dict_pos_substrings.items():
        substrings_to_check = [y for y in substrings if 4 <= len(y) <= 12 and len(y) % 2 == 0]
        for substring in substrings_to_check:
            if is_reverse_palindrome(substring):
                reverse_palindromes.append([position, len(substring), substring])

    results = ""
    for reverse_palindrome in reverse_palindromes:
        position = reverse_palindrome[0]+1
        length = reverse_palindrome[1]
        substring = reverse_palindrome[2]
        print("Start position: {0} \nLength: {1} Substring: {2}\n".format(position, length, substring))
        results += "{0} {1}\n".format(position, length)

    print(results)
    return results

