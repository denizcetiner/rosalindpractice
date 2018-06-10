def wabbits(months=5, given_birth=3):
    rabbit_pairs_by_month = [[1,0]] # [immature, mature] list by months.
    for month in range(1, months):  # first month is known, 1 immature, 0 mature pair
        pairs_prev = rabbit_pairs_by_month[month-1]
        pairs_new = [pairs_prev[1] * given_birth, pairs_prev[0]+pairs_prev[1]]
        rabbit_pairs_by_month.append(pairs_new)
    for i in range(len(rabbit_pairs_by_month)):
        pair = rabbit_pairs_by_month[i]
        print("month:{0}, immature:{1}, mature:{2}".format(i, pair[0], pair[1]))
    return  rabbit_pairs_by_month


def run(input="5 3"):
    params = input.split()
    months = int(params[0])
    pairs = int(params[1])
    rabbits_monthly = wabbits(months, pairs)
    return rabbits_monthly[months-1][0] + rabbits_monthly[months-1][1]