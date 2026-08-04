class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        failed = set()

        def check(s, i) -> bool:
            if i in failed:
                return False
            if i ==len(s):
                return True

            for word in wordDict:
                if i+len(word) <= len(s):
                    if s[i:i+len(word)] == word:
                        if check(s, i+len(word)):
                            return True
            failed.add(i)
            return False

        return check(s, 0)
            




        