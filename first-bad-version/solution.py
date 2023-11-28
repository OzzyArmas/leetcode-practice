# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # binary search
        if n == 1:
            return 1
        
        mid = n // 2
        high = n
        low = 1
        while low < high:
            if isBadVersion(mid): 
                high = mid
                mid = (low + high) // 2
            else:
                low = mid + 1
                mid = (low + high) // 2
        return mid
