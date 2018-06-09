def run(problem_name = ""):
    url = values["{0}_url".format(problem_name)]
    id = values["{0}_id".format(problem_name)]
    print(url)
    dataset_filename = "rosalind_{0}".format(id)
    with open("input/{0}.txt".format(dataset_filename), "r") as dataset_file:
        dataset_input = dataset_file.read().strip()
    module = __import__(problem_name)
    result = getattr(module, "run")(dataset_input)
    with open("output/{0}_result.txt".format(dataset_filename), "w") as dataset_result_file:
        dataset_result_file.write(result)
    return

values = {}
with open("url_dataset_names.txt") as file:
    for line in file:
        (key, val) = line.split()
        values[str(key)] = val

problem_name = input()
run(problem_name.upper())