import sys

n = int(input())
res = [1]
i = j = k = 0
ugly2 = 2 * res[i]
ugly3 = 3 * res[i]
ugly5 = 5 * res[i]
for m in range(1, n):
    next_ugly = min(ugly2, ugly3, ugly5)
    res.append(next_ugly)
    if next_ugly == ugly2:
        i += 1
        ugly2 = 2 * res[i]
    if next_ugly == ugly3:
        j += 1
        ugly3 = 3 * res[j]
    if next_ugly == ugly5:
        k += 1
        ugly5 = 5 * res[k]
print(res)