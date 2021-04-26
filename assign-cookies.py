class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        
        j=0
        count=0
        s.sort()
        g.sort()
        for i in s:
            if(len(g)==0):
                break
            if i >=g[j]:
                g.pop(0)
                count+=1
        return count
                
