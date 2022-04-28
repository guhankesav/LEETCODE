class Solution:
    def jump(self, nums: List[int]) -> int:
        pos = 0
        moves = 0
        
        while pos < len(nums) - 1:
            k = pos + nums[pos]     #position's max_reach, and range for sub-testings (for loop)
            
            if k >= len(nums) - 1:  #one more move can go to the end, just return moves + 1
                return moves + 1
            
            max_reach = 0   
            max_reach_pos = 0
            
            for j in range(pos+1, k + 1):
                if j < len(nums):           #prevent out of index
                    temp = j + nums[j]      #max_reach subtesting
                    if temp > max_reach:    # >= works the same, but will increase Runtime
                        max_reach = temp
                        max_reach_pos = j
            #found the single move that will bring the maximum reach
            
            pos = max_reach_pos             #push the position forward
            moves += 1
        
        return moves
