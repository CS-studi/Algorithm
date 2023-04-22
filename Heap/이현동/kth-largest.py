import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for i in nums:
            heapq.heappush(q, -i)
        
        while k:
            k -= 1
            if k == 0:
                break
            heapq.heappop(q)

        return heapq.heappop(q)*-1