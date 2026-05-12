class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        storage = {}
        for char in s:
            if char in storage:
                storage[char] = storage[char] + 1
            else:
                storage[char] = 1

        for char in t:
            if char not in storage:
                return False
            else:
                val = storage[char]
                if val<=0:
                    return False
                else:
                    storage[char] -= 1

        for char in s:
            if storage[char] != 0:
                return False

        return True
        


        