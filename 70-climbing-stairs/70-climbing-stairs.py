class Solution:
    def climbStairs(self, n: int) -> int:
        a=[]
        a.append(0)
        a.append(1)
        a.append(2)
        if n>2:
            for i in range(3,n+1):
                c=a[i-1]+a[i-2]
                a.append(c)
        return(a[n])