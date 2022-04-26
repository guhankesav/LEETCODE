class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
            key, maxDur = keysPressed[0], releaseTimes[0]

            for i in range(1, len(releaseTimes)):
                dur = releaseTimes[i] - releaseTimes[i-1]
                if dur > maxDur: key = keysPressed[i]
                elif dur == maxDur: key = max(key, keysPressed[i])
                maxDur = max(dur, maxDur)

            return key