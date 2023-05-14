import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = [i for i in range(len(score))]
        q = []
        for idx, score in enumerate(score):
            heapq.heappush(q, [-score, idx])
        
        
        for i in range(len(q)):
            score, idx = heapq.heappop(q)
            
            if i == 0:
                rank[idx] = "Gold Medal"
            elif i == 1:
                rank[idx] = "Silver Medal"
            elif i == 2:
                rank[idx] = "Bronze Medal"
            else:
                rank[idx] = str(i+1)
        return rank
