#https://leetcode.com/problems/shuffle-string/submissions/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = list(s)
        len_of_input=(len(indices))
        ind = [i for i in range(len_of_input)]
        print(ind)
        # i just created ind to explore th initialization
        print(indices)


        
        i=0
        while i< len(s):
            if(i==indices[i]):
                i+=1
            else:
                swap = indices.index(i)
                temp1 = indices[i]
                temp2 = l[i]
                indices[i] = indices[swap]
                l[i] = l[swap]
                indices[swap]=temp1
                l[swap] = temp2
                

                i+=1
                
                
                
        str1 = (str(l).strip('[]'))
        str1 = str1.replace(",","")
        str1 = str1.replace("'","")
        str1 = str1.replace(" ","")


        print(str1)
        print(ind)
        return str1
