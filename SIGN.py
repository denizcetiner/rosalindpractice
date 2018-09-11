import itertools


def get_all_combinations(list_input=[]):
    combinations = []
    for len_choice in range(1, len(list_input)+1):
        combinations.extend([list(comb) for comb in itertools.combinations(list_input, len_choice)])
    return combinations


def create_signed_perms(list_unsigned=[1,2]):
    sign_position_elements = [i for i in range(len(list_unsigned))]
    sign_pos_combinations = get_all_combinations(sign_position_elements)
    list_perms_signed = [list_unsigned]
    for positions in sign_pos_combinations:
        perm_signed = list_unsigned[:]
        for pos in positions:
            perm_signed[pos] = -perm_signed[pos]
        list_perms_signed.append(perm_signed)
    return list_perms_signed



def run(user_input="""2"""):
    len_signed = int(user_input)

    elements = [i for i in range(1, len_signed+1, 1)]

    unsigned_perms_list = [list(perm) for perm in itertools.permutations(elements, len_signed)]
    signed_perms_list = []
    for perm in unsigned_perms_list:
        signed_perms_of_perm = create_signed_perms(perm)
        print(signed_perms_of_perm)
        signed_perms_list.extend(signed_perms_of_perm)

    result = str(len(signed_perms_list)) + "\n"
    for signed_perm in signed_perms_list:
        result += " ".join(str(element) for element in signed_perm) + "\n"
    print(result)
    return result
