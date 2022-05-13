class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while True:
            check = numbers[left] + numbers[right]
            if check == target:
                return [left + 1, right + 1]
            elif check < target:
                left += 1
            else:
                right -= 1