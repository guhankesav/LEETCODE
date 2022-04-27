class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(p[0]**2 + p[1]**2, p) for p in points]
        print(points)
        heapify(points)
        print(points)
        return [heappop(points)[1] for _ in range(k)]