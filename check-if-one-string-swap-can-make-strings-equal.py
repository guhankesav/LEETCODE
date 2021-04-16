#https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if (s1==s2):
            return True
        else:
            
            t1=-1
            t2=-1
            co =0
            for i in range(len(s1)):
                if s1[i] !=s2[i]:
                    if co ==0:

                        t1=i
                        co = 1
                    else:
                        temp1 = s2[i]
                        start = s2[:t1]
                        mid = s2[t1+1:i]
                        end = s2[i+1:]
                        s3  = start +s2[i] +mid + s2[t1] + end
                        print(s3)
                        if(s1==s3):
                            return True
                        else:
                            return False
        
