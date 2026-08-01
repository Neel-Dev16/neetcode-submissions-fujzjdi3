class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return ['']
            if i in memo:
                return memo[i]

            res = []
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in words:
                    for tail in dfs(j):
                        res.append(word if tail == '' else word + ' ' + tail)
            memo[i] = res
            return res

        return dfs(0)
