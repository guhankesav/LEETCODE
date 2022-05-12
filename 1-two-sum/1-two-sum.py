class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in hashmap:
                return [hashmap[m], i]
            hashmap[n] = i