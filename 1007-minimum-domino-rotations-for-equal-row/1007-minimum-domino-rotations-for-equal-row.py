class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        x=tops[0]
        y=bottoms[0]
        res=-1
        fx=1
        fy=1
        for i in range(len(tops)):
            if tops[i]==x or bottoms[i]==x:
                continue
            else:
                fx=0
                break
        
        for i in range(len(tops)):
            if tops[i]==y or bottoms[i]==y:
                continue
            else:
                fy=0
                break
        
        if fx==0 and fy==0:
            return -1
        
        res=100000
        
        if fx==1:
            a=tops.count(x)
            b=bottoms.count(x)
            res=len(tops)-(max(a,b))
        if fy==1:
            a=tops.count(y)
            b=bottoms.count(y)
            res=min(res,len(tops)-(max(a,b)))
            
        
        return res