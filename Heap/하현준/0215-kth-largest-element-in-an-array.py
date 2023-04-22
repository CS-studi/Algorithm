class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify([-x for x in nums])
        return heapq.nlargest(k, nums)[-1]
