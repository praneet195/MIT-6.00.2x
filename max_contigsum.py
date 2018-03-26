


def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE
    N = len(L)
    max = 0
    largest = []
    sub = []
    for i in range(len(L)):
        for j in range(i,len(L)+1):
            if len(L[i:j])!=0:
                sub.append(L[i:j])
    largest = []
    for i in range(len(sub)):
        summ = 0
        for j in sub[i]:
            summ += j
        if summ > max:
            max = summ
            largest = sub[i][:]
    return (largest, max)
print(max_contig_sum([5, -7, 1,6]))
