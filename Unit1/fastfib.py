def fastfib(n,memo={}):
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result=fastfib(n-1,memo)+fastfib(n-2,memo)
        memo[n]=result
    return result
print(fastfib(36))