class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        front = 0
        store = set()
        maxLength = 0


        for i, char in enumerate(s):
            if char in store:
                maxLength = max(maxLength, i - front)
                found = False
                while(not found):
                    front_char = s[front]
                    store.remove(front_char)
                    if front_char==char:
                        found = True
                    front += 1
            store.add(char)

        maxLength = max(maxLength, len(s)-front)

        return maxLength
                







                    


            



        