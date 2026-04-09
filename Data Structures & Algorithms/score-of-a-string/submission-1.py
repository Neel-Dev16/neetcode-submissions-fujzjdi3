class Solution:
    def scoreOfString(self, s: str) -> int:
        j = 1
        i = 0
        result = 0
        while j <= len(s) - 1:
            result += abs(ord(s[j]) - ord(s[i]))
            i += 1
            j += 1
            

        return result