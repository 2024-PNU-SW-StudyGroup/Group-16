from collections import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dict = defaultdict(int)
        for i in range(len(nums)):
            temp_dict[target-nums[i]] = i+1
        for i in range(len(nums)):
            if temp_dict[nums[i]] and i != temp_dict[nums[i]]-1:
                return [i, temp_dict[nums[i]]-1]
        return []
            