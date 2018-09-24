def greedySum(L, s):
    
    mul = []
    rem = s
    for i in L:
        if i <= rem:
            multi = rem // i
            mul.append(multi)
            rem -= i * multi
        else:
            mul=.append(0)
    summ = 0
    for j in range(len(mul)):
        summ += L[j]*mul[j]
    if summ == s:
        return sum(mul)
    else:
        return 'no solution'

