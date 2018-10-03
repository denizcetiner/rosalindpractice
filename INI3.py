def run(user_input="""HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102"""):
    params = user_input.splitlines()
    input_string = params[0]
    indices = [int(i) for i in params[1].split()]

    words = []
    for i in range(0, len(indices), 2):
        indice0 = indices[i]
        indice1 = indices[i+1]
        word = input_string[indice0:indice1+1]
        words.append(word)

    result = " ".join(words)
    return result
