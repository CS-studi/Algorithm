class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        q = []
        medal = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        for i, s in enumerate(score):
            heapq.heappush(q, (-s, i))
        answer = ["" for _ in range(len(score))]

        i = 0
        while q:
            now, ni = heapq.heappop(q)
            if i < 3:
                answer[ni] = medal[i]
            else:
                answer[ni] = str(i + 1)
            i += 1
        return answer
