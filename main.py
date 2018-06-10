def run(problem_name=""):
    values = {}
    with open("url_dataset_names.txt") as file:
        for line in file:
            (key, val) = line.split()
            values[str(key)] = val

    url = values["{0}_url".format(problem_name)]
    id = values["{0}_id".format(problem_name)]
    print(url)
    dataset_filename = "rosalind_{0}".format(id)
    with open("input/{0}.txt".format(dataset_filename), "r") as dataset_file:
        dataset_input = dataset_file.read().strip()
    module = __import__(problem_name)
    result = getattr(module, "run")(dataset_input)
    with open("output/{0}_result.txt".format(dataset_filename), "w") as dataset_result_file:
        dataset_result_file.write(str(result))
    return


def main():
    problem_name_input = input()
    run(problem_name_input.upper())


main()
