class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        answer = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if answer != 0:
                    return answer
            else:
                answer += 1
        return answer