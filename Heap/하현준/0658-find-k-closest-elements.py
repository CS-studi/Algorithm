class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        q = []
        for i, a in enumerate(arr):
            val = abs(a - x) + (a / (10 ** 5))
            heapq.heappush(q, (-val, a))

        nlargest = heapq.nlargest(k, q)
        answer = [x[1] for x in nlargest]
        return sorted(answer)
