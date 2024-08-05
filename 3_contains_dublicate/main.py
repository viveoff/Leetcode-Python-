from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for n in nums:  # going through every value of input array
            if n in hashSet:
                return True
            hashSet.add(n)
        return False

# 1
"""
nums = [1, 2, 3, 1]
hashSet = set() # 1, 2, 
for 1 in nums:
		if 1 in hashSet(no)
		hashSet.add(1)
return False

for 2 in nums:
		if 2 in hashset(no)
		hashSet.add(2)
return False

for 3 in nums:
		if 3 in hashset(no)
		hashSet.add(3)
return False

for 1 in nums:
		if 2 in hashSet(yes)
			return True
"""
