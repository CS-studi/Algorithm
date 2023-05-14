class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []

        def bt(num, part_sum, part):
            if len(part) == k and part_sum == n:
                answer.append(part)
                return

            if num > 9:
                return

            if len(part) < k - 1 and num + 1 > n - part_sum:
                return

            for i in range(num + 1, 10):
                bt(i, part_sum + i, part + [i])

        bt(0, 0, [])
        return answer