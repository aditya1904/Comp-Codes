from math import sqrt

def is_perf_square(n):
    rt = sqrt(n)
    return True if rt == int(rt) else False

def is_zero(n):
    return 0 if n == 0 else 1

def numSquares(n: int) -> int :
    total = 0
    root = int(sqrt(n))
    for i in range(root, 0, -1):
        print("iter", i)
        if(is_perf_square(n%(i**2))):
            print("found a square", i**2)
            total += ((n//(i**2)) + is_zero(n%(i**2)))
            return total
    return total

print(numSquares(int(input())))