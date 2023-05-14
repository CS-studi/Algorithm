class Solution:

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        answer = []
        hours = [1, 2, 4, 8]
        minutes = [1, 2, 4, 8, 16, 32]

        def bt(hn, mn):
            if hn < 0 or hn > 4:
                return
            if mn < 0 or mn > 6:
                return
            if (hn, mn) in visited:
                return
            visited.add((hn, mn))

            hcomb = set(sum(x) for x in combinations(hours, hn) if sum(x) < 12)
            mcomb = set(sum(x) for x in combinations(minutes, mn) if sum(x) < 60)
            for h in hcomb:
                for m in mcomb:
                    mstr = f"0{m}" if m < 10 else str(m)
                    answer.append(f"{h}:{mstr}")
            bt(hn - 1, mn + 1)
            bt(hn + 1, mn - 1)
            return

        visited = set()
        for i in range(5):
            bt(i, turnedOn - i)
        return answer