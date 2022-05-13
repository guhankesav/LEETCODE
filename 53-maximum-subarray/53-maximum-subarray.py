class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]
        currmaz = 0
        for i in nums:
            if(currmaz < 0):
                currmaz = 0
            currmaz += i
            maxx = max(maxx,currmaz)
        return maxx
        