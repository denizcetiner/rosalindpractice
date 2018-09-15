import os, sys


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
    run = getattr(module, "run")
    result = run(dataset_input)
    with open("output/{0}_result.txt".format(dataset_filename), "w") as dataset_result_file:
        dataset_result_file.write(str(result))
    return


def run_test(problem_name: str):
    problem_directory = f"test_datas/{problem_name}"
    inputs_directory = f"{problem_directory}/inputs"
    outputs_directory = f"{problem_directory}/outputs"

    if not os.path.exists(inputs_directory):
        os.makedirs(inputs_directory)
    if not os.path.exists(outputs_directory):
        os.makedirs(outputs_directory)

    results = []
    dir_files = os.listdir(inputs_directory)
    for file in dir_files:
        with open(f"{inputs_directory}/{file}", "r") as dataset_file:
            dataset_input = dataset_file.read().strip()

        module = __import__(f"{problem_name}")
        result = getattr(module, "run")(dataset_input)


        with open(f"{outputs_directory}/result_{file}","r") as result_file:
            success_result = result_file.read()


        if str(result).strip() == str(success_result).strip():
            results.append(f"{file} successfull")
        else:
            results(f"{file} failed, {result} {success_result}")

    print("\n".join(results))


def main():
    params = input().split()
    command = params[0]
    problem_name = params[1].upper()

    if command == "run":
        run(problem_name)
    elif command == "test":
        run_test(problem_name)


main()
