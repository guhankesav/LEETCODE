class Solution:
    def slowestKey(self, times, keys):
        durations = [times[i]-times[i-1] if i>0 else times[i] for i in range(len(times))]
        slowestKeys = [keys[i] for i in range(len(durations)) if durations[i] == max(durations)]
        return max(slowestKeys)