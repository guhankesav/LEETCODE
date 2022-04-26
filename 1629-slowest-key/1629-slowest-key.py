class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_duration = releaseTimes[0]
        max_key = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            if (releaseTimes[i]-releaseTimes[i-1] > max_duration) or ( releaseTimes[i]-releaseTimes[i-1] == max_duration and keysPressed[i] >= max_key):
                max_key = keysPressed[i]
                max_duration = releaseTimes[i]-releaseTimes[i-1]
        return max_key