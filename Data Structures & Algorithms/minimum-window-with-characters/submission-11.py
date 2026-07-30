class Solution:
    def minWindow(self, s: str, t: str) -> str:
         
        if s==t:
            
            return s

        t_dict = {}
        s_dict = {}

        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
            s_dict[char] = 0

        #for key, value in t_dict.items():
        #    print(key, value)

        #print()

        def compare_dicts(s, t , printx=False) -> bool:
           

            for key in t.keys():
                #if printx:
                    #print("key", key, "s:", s[key], "t:", t[key])
                if s[key] < t[key]:
                    #if printx:
                        #print("False")
                    return False
            return True

        start, end = 0, 0

        equal = False

        final = ""
        length = len(s)+1
        count = 0
        while( True):
            count+=1
            #print("a", count)
            if start >= len(s)-1 or (end>=len(s) and equal==False):
                #print("break")
                break
            while((equal == False and end<len(s))):
                count+=1
                #print("b", end, count)
                #print("end:", end, "len(s):", len(s))
                #print(s[start:end+1])
                if s[end] in s_dict:
                    s_dict[s[end]] += 1
                    if compare_dicts(s_dict, t_dict, True):
                        #print("equal")
                        equal = True
                end += 1
            while(equal == True and start<len(s)):
                count += 1
                #print("c", start, count)
                #print(s[start:end])
                if s[start] in s_dict:
                    s_dict[s[start]] -= 1
                    if not compare_dicts(s_dict, t_dict, True):
                        #print("not equal")
                        equal = False
                        if end-start < length:
                            length = end-start
                            final = s[start:end]
                start+=1

        return final
                


                





            
                    
                        

            


