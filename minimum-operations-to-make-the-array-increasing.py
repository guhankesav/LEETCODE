class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sum =0
        for i in range(len(nums)-1):
            if nums[i+1]<=nums[i]:
                k = nums[i]+1-nums[i+1]
                nums[i+1]+=k
                sum+=k
        return sum
