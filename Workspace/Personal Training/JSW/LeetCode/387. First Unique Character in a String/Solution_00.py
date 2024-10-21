from collections import *
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = defaultdict(int)
        for c in s:
            char_dict[c] += 1
        target = None
        for k, v in char_dict.items():
            if v == 1:
                target = k
                break
        
        for i in range(len(s)):
            if s[i] == target:
                return i
        return -1