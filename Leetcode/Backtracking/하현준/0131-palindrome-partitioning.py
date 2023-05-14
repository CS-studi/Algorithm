class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []

        def is_palindrom(temp):
            for i in range(len(temp) // 2):
                if temp[i] != temp[len(temp) - 1 - i]:
                    return False
            return True

        def bt(si, part):
            if si >= len(s):
                answer.append(part)
                return

            for slen in range(1, len(s) - si + 1):
                temp = s[si:si + slen]
                if is_palindrom(temp):
                    bt(si + slen, part + [temp])

        bt(0, [])
        return answer