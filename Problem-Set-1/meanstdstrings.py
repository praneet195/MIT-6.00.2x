def getMeanAndStd(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    std = (tot / len(X)) ** 0.5
    return mean, std


def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if not L:
        return float("NaN")
    else:
        simdict = {}
        summ=0
        for i in L:
            simdict[i]=len(i)
            summ+=len(i)
        mean=summ/len(L)
        variance=0
        for i in L:
            variance+=(simdict[i]-mean)**2/len(L)
        return round(variance**0.5,4)



print(stdDevOfLengths( []))