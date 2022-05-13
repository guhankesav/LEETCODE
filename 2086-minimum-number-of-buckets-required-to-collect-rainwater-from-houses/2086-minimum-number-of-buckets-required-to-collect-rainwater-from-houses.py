class Solution:
    def minimumBuckets(self, s: str) -> int:
        return -1 if 'HHH' in s or s[:2] == 'HH' or s[-2:] == 'HH' or s == 'H' else s.count('H') - s.count('H.H')
        