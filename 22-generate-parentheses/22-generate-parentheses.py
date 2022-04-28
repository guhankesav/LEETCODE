class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        else:
            l2 = self.generateParenthesis(n-1)
            l3 = set(i[:j]+'()'+i[j:] for i in l2 for j in range(0,len(l2)+1))
            return list(l3)