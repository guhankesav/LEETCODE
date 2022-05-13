class Solution:
    def numberOfWays(self, s: str) -> int:
        ways = one = zero = onesAfterZero = zerosAfterOne = 0
        for i in s:
            if i == '0':
                zero += 1
                zerosAfterOne += one
                ways += onesAfterZero
            else:
                one += 1
                onesAfterZero += zero
                ways += zerosAfterOne
        return ways