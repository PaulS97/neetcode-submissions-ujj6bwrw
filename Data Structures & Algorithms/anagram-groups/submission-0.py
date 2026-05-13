class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        final = []
        def createDict(onestr):
            storage = {}
            for i in range(len(onestr)):
                storage[onestr[i]] = storage.get(onestr[i], 0) + 1
            return storage


        def isAnagram(str1, str2):
            if len(str1) != len(str2):
                return False
            else:
                return createDict(str1) == createDict(str2)

        for word in strs:
            if not final:
                final.append([word])
            else:
                foundAnagram = False
                for group in final:
                    if isAnagram(word, group[0]):
                        group.append(word)
                        foundAnagram = True
                if not foundAnagram:
                    final.append([word])

        return final
                    
