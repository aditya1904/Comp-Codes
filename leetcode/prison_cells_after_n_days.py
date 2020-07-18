from typing import *

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        old = cells
        for i in range(N%14 + 14):
            new = [0]
            for i in range(1, 7):
                new.append(int(old[i-1] == old[i+1]))
            new.append(0)
            old = new
        return old

solution = Solution()
prison = list(map(int, input().split()))
N = int(input())
sol = solution.prisonAfterNDays(prison, N)

print("========================")
print("Solution", sol)