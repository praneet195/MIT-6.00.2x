def greedy_cow_transport(cowdict, maxweight):
    retlist = []
    cowsCopy = cowdict.copy()
    sortedCows = sorted(cowsCopy.items(), key=lambda x: x[1], reverse=True)
    while sum(cowsCopy.values()) > 0:
        ship = []
        total = 0
        for cow, value in sortedCows:
            if cowsCopy[cow] != 0 and value + total <= maxweight:
                ship.append(cow)
                total += value
                cowsCopy[cow] = 0
        retlist.append(ship)
    return retlist