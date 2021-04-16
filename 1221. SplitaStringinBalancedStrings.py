# 1221. Split a String in Balanced Strings
# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it in the maximum amount of balanced strings.

# Return the maximum amount of split balanced strings.
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        count=0
        stack.append(s[0])
        for i in range(1,len(s)):
            if(len(stack)==0):
                stack.append(s[i])
            elif(s[i]==stack[-1]):
                stack.append(s[i])
            else:
                stack.pop()
            if(len(stack) == 0):
                count+=1
            i+=1
        return count
                
            

        


        
        
