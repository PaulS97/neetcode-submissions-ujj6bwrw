class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        s2_dict = {}

        if len(s1)>len(s2):
            return False

        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1

        for char in s2[0:len(s1)]:
            s2_dict[char] = s2_dict.get(char, 0) + 1

        start = 0
        end = len(s1)

        if s1_dict==s2_dict:
            return True

        while(end<len(s2)):
            echar = s2[end]
            s2_dict[echar] = s2_dict.get(echar, 0) + 1

            schar = s2[start]
            if s2_dict[schar] == 1:
                del s2_dict[schar]
            else:
                s2_dict[schar] = s2_dict[schar] - 1

            if s1_dict==s2_dict:
                return True

            start+=1
            end+=1

        return False









        