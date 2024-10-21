from collections import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        int_dict = defaultdict(int)
        for e in nums:
            int_dict[e] += 1
        return sorted(int_dict.keys(), key=lambda x: int_dict[x], reverse=True)[:k]