class Solution:
    def maxScore(self, nums: List[int]) -> int:
        h=[(gcd(nums[a],nums[b]), 1<<a|1<<b ) for a,b in combinations(range(len(nums)),2)]     
        @cache
        def dfs(n,m):
            if not n:return 0
            res=0
            for x,mm in h:
                if not mm&m:
                    res=max(res,n*x+dfs(n-1,m|mm))
            return res
        return dfs(len(nums)//2 , 0)