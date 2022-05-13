class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        leng = len(questions)
        dp = [0 for i in range(leng+1)]
        print(len(dp))
        for i in range(leng-1,-1,-1):
            point, bp = questions[i]
            dp[i] = max(dp[i+1],(point + dp[min(leng,i + bp  + 1)]))
        print(dp)
        return dp[0]
        