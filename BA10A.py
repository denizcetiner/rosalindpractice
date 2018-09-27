def extract(user_input:str, symbols_column_line:int, symbols_row_line:int, matrix_line:int, path0_index:int, path1_index:int):
    params:list[str] = user_input.splitlines()
    path_column: str = params[path0_index]
    path_row: str = params[path1_index]
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
    return path_dict, path_column, path_row


def solve(path_dict: {}, path: str):
    result = 0.5
    for i in range(len(path)-1):
        origin, destinaton = path[i], path[i+1]
        result = result * path_dict[origin][destinaton]
    return result


def run(user_input="""AABBBAABABAAAABBBBAABBABABBBAABBAAAABABAABBABABBAB
--------
A   B
--------
    A   B
A   0.194   0.806
B   0.273   0.727"""):
    root = {"root"}
    path_dict, path0, path0  = extract(user_input,2, 2, 5, 0, 0)
    print(path_dict)
    prob = solve(path_dict, path0)
    print(prob)
