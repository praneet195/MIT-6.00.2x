
def brute_force_cow_transport(cows,limit):
    trips = []
    # create power list using helper function, and sort it - shortest first!
    power_list = sorted(get_partitions(cows), key = len)
    # Note that this returns a list of names (strings), and we will need to do
    # dictionary lookup later
    # Now time to filter the power list:
    possibilities = []
    for i in power_list:
        ship = []
        for j in i:
            ship_weights = []
            for k in j:
                ship_weights.append(cows[k])
            ship.append(sum(ship_weights))
        if all(d <= limit for d in ship):
            possibilities.append(i)
    # possibiliies now contains some duplicates, which need to be removed
    pruned_possibilities = []
    for k in possibilities:
        if k not in pruned_possibilities:
            pruned_possibilities.append(k)
    # now find the minimum list length:
    min_list_len = min(map(len, pruned_possibilities))
    for l in pruned_possibilities:
        if len(l) == min_list_len:
            return l