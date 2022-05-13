class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        print(hashset)
        longest = 0
        for i in nums:
            if i - 1 not in hashset:
                long = 0
                while i + long in hashset:
                    long+=1
                longest = max(long,longest)
        return longest