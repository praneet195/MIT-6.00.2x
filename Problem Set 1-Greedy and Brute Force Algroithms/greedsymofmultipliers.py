
def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for
        the largest value in L then for the second largest, and so on to
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does
                not yield a set of multipliers such that the equation sums to 's'
    """
    summ=0
    oris=s
    multiplier=[]
    for i in L:
        j=s//i
        if i*j<=s :
            multiplier.append(j)
            s-=i*j
    for i in range(len(L)):
        j=multiplier[i]
        summ+=L[i]*j
    if summ==oris:
        return sum(multiplier)
    else:
        return "no Solution"
print(greedySum([5,4,3,2,1],109))
