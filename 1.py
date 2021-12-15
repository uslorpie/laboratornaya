n  = int(input())
def H(n, a, c):

    if n <= 0:
        return
    b = a - c
    H(n-1, a, b)
    print (n, a, c)
    H(n-1, b, c)
print (*H(n, 1, 3))