def C(n, r):
    if r == 0:
        return 1
    if r == n:
        return 1
    return C(n-1, r) + C(n-1, r-1)
C(900,40)