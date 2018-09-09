factorials = {0:1, 1:1}


def get_factorial(n=5):
    if n not in factorials:
        factorials[n] = n * get_factorial(n-1)
    return factorials[n]


def get_permutation(len_elements=3, len_choose=2):
    top = get_factorial(len_elements)
    bottom = get_factorial(len_elements - len_choose)
    return top / bottom


def run(user_input="""21 7"""):
    params = user_input.split()
    len_elements = int(params[0])
    len_choose = int(params[1])
    perms_count = int(get_permutation(len_elements, len_choose))
    perms_count = perms_count % 1000000
    print(perms_count)
    return perms_count
