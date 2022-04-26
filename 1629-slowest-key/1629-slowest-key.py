class Solution:
    def slowestKey(self, t, k):
        return max(zip(map(sub,t,[0]+t),k))[1]