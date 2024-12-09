from collections import *
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = defaultdict(int)
        for c in s:
            char_dict[c] += 1
        for i in range(len(s)):
            if char_dict[s[i]] == 1:
                return i
        return -1