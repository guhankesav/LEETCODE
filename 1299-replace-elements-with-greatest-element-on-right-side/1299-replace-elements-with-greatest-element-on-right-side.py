class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        out = [-1]*len(arr)
        max = arr[len(arr)-1]
        for i in range(len(arr)-2,-1,-1):
            out[i] = max
            if max < arr[i]:
                max = arr[i]
            
        return out
            
        