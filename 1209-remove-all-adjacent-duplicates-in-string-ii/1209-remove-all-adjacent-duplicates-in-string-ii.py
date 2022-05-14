class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # [char , continours prev count]
        
        for char in s:
            if stack and stack[-1][0] is char:
                c, pc = stack.pop()
                if pc + 1 == k:
                    continue
                else:
                    stack.append([char,pc+1])
            else:
                stack.append([char,1])
        out = ""
        for c , n in stack:
            out += (c * n)
        print(out)
        return out
                
        