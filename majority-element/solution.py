from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for num, count in counts.items():
            if count > len(nums) // 2:
                return num

        # below is not my solution but cool to learn it 
        # really funny how it's still slower than the one above
        # per the leetcode ranker
        # count = 0
        # candidate = None
        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     count += (1 if num == candidate else -1)

        # return candidate
