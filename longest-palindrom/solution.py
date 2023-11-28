from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c_s = Counter(s)
        longest_pal = 0
        mark_odd = False
        # basically: all even counts
        # all odd counts - 1
        # all those left over extras, I can choose one of them
        for k, v in c_s.items():
            if v % 2 == 0:
                longest_pal += v
            else:
                longest_pal += v - 1
                mark_odd = True
        return longest_pal + 1 if mark_odd else longest_pal
