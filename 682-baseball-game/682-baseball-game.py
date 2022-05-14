class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for i in ops:
            if i is "D":
                stack.append(stack[-1]*2)
            elif i is "C":
                stack.pop()
            elif i is "+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(i))
        print(stack)
        res = 0
        for i in stack:
            res += i
        return res
        
            
        