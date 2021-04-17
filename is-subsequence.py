class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1=list(s)
        t1=list(t)
        if(len(s)==0):
            return True
        i =0
        for j in t1:
            if j==s1[i]:
                i+=1
                if(i==len(s)):
                    return True
            
        return False    
       
