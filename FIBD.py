def wabbits(months=5, given_birth=3, death_after=3):
    rabbit_pairs_by_month = [[1,0]] # [immature, mature] list by months.
    for month in range(1, months):  # first month is known, 1 immature, 0 mature pair
        pairs_prev = rabbit_pairs_by_month[month-1]
        dead_rabbits = 0
        if month >= death_after:
            dead_rabbits = rabbit_pairs_by_month[month-death_after][0]
        pairs_new = [pairs_prev[1] * given_birth, pairs_prev[0]+pairs_prev[1]-dead_rabbits]
        rabbit_pairs_by_month.append(pairs_new)
    for i in range(len(rabbit_pairs_by_month)):
        pair = rabbit_pairs_by_month[i]
        print("month:{0}, immature:{1}, mature:{2}".format(i, pair[0], pair[1]))
    return rabbit_pairs_by_month


def run(input="6 3"):
    params = input.split()
    months = int(params[0])
    death_after = int(params[1])
    rabbits_monthly = wabbits(months, 1, death_after)
    result = rabbits_monthly[months-1][0] + rabbits_monthly[months-1][1]
    print(result)
    return result


run()
