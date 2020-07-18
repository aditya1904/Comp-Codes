from typing import *
from collections import defaultdict
from copy import copy

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        y = defaultdict(lambda: 0)
        for num in nums:
            y[num] += 1
        result = []
        for i in range(len(nums)):
            first_num = nums[i]
            second_num = 0 - first_num
            temp = copy(y)
            for j in range(i+1 , len(nums)):
                temp[first_num] -= 1
                possible = [first_num]
                third_num = second_num - nums[j]
                temp[nums[j]] -= 1
                if temp[third_num] > 0:
                    possible.append(nums[j])
                    possible.append(third_num)
                    temp[third_num] -= 1
                    result.append(sorted(possible))
        return result

nums = list(map(int, input().split()))
solution = Solution()
print(solution.threeSum(nums))

