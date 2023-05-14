class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score,reverse=True)
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        i = -1
        for n in sorted_score:
            i+=1
            idx = score.index(n)
            if i < 3:
                score[idx] = medal[i]
                continue
            score[idx] = str(i+1)
        return score