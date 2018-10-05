def run(user_input="""100 200"""):
    params = [int(i) for i in user_input.split()]
    start = params[0]
    end = params[1]

    sum = 0
    for i in range(start, end+1):
        if i % 2 == 1:
            sum += i

    print(sum)
    return sum
