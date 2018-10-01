def run(user_input="""3 5"""):
    result = 0
    params = user_input.split()
    for param in params:
        result += int(param) ** 2
    return result