class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        store = {}
        for char in s:
            store[char] = store.get(char,0) + 1


        seen = set()
        subs = []
        used = 0
        for i, char in enumerate(s):
            seen.add(char)
            store[char] -= 1
            val = store[char]
            if not val:
                seen.remove(char)
            if not seen:
                subsize = i+1-used
                used+=subsize
                subs.append(subsize)

        return subs

            


        