from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            dif = target - nums[i]
            if dif in hashMap:
                return [hashMap[dif],i]
            hashMap[n] = i
        return []

# nums = [2,7,11,15]
# target = 9

# for i = 0, n = 2:
#   dif = 9 - 2 => 7
#   if 7 in hashMap (NO)
#   hashMap = {2: 0}





