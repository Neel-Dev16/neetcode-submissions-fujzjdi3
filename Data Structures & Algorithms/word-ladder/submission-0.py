class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        q=collections.deque([beginWord])
        steps=1
        while q:
            for _ in range(len(q)):
                word=q.popleft()
                if word == endWord:
                    return steps
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == word[i]:
                            continue
                        nxt = word[:i] + ch + word[i+1:]
                        if nxt in wordset:
                            q.append(nxt)
                            wordset.remove(nxt)
            steps+=1
        return 0
        