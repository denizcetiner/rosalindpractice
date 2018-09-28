def extract2(user_input:str, symbols_column_line:int, symbols_row_line:int, matrix_line:int, path0_index:int, path1_index:int):
    params:list[str] = user_input.splitlines()
    path0: str = params[path0_index]
    path1: str = params[path1_index]
    symbols_row:list[str] = params[symbols_row_line].split()
    symbols_column = params[symbols_column_line].split()

    path_dict = {}

    line_index = matrix_line
    for origin_index in range(len(symbols_row)):
        row_sym = symbols_row[origin_index]
        current_line = params[line_index]
        path_probs = current_line.split()[1:]

        path_dict[row_sym] = {}
        for path_prob_index in range(len(path_probs)):
            column_sym = symbols_column[path_prob_index]
            path_prob_val = path_probs[path_prob_index]

            path_dict[row_sym][column_sym] = float(path_prob_val)
        line_index += 1
    return path_dict, path0, path1


def solve(emission_dict:{}, first_path:str, second_path:str):
    result = 1
    for i in range(len(first_path)):
        p1 = first_path[i]
        p2 = second_path[i]
        result = result * emission_dict[p2][p1]
    return result

def run(user_input="""xxyzyxzzxzxyxyyzxxzzxxyyxxyxyzzxxyzyzxzxxyxyyzxxzx
--------
x   y   z
--------
BBBAAABABABBBBBBAAAAAABAAAABABABBBBBABAABABABABBBB
--------
A   B
--------
    x   y   z
A   0.612   0.314   0.074 
B   0.346   0.317   0.336"""):
    emission_dict, first_path, second_path = extract2(user_input, 2, 6, 9, 0, 4)
    print(emission_dict)
    output = solve(emission_dict, first_path, second_path)
    print(output)


run()
