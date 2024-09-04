from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub 


""" 
nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSub = -2
curSum = 0

for -2 in nums:
    if 0 < 0:
        0 = 0
    0 + (-2) = -2
    maxSub = max(-2, 0)
return -2

for 1 in nums:
    if -2 < 0:
        -2 = 0
    0 + 1 = 1
    maxSub = max(1, -2)
    
"""


