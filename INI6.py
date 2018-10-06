def run(user_input="""We tried list and we tried dicts also we tried Zen"""):
    dict_word_count = {}
    for word in user_input.split():
        if word in dict_word_count:
            dict_word_count[word] += 1
        else:
            dict_word_count[word] = 1

    result_keyvalues = []
    for key, value in dict_word_count.items():
        result_keyvalues.append(f"{key} {value}")

    result = "\n".join(result_keyvalues)
    print(result)
    return result