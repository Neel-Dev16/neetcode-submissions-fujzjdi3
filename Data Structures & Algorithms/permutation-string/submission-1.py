class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26
        for i in range(len(s1)):
            need[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if need[i] == window[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            i = ord(s2[r]) - ord('a')
            window[i] += 1
            if window[i] == need[i]:
                matches += 1
            elif window[i] == need[i] + 1:
                matches -= 1

            i = ord(s2[l]) - ord('a')
            window[i] -= 1
            if window[i] == need[i]:
                matches += 1
            elif window[i] == need[i] - 1:
                matches -= 1
            l += 1

        return matches == 26
