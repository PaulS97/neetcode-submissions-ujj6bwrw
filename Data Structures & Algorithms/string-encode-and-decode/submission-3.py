class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[""]:
            return "x"
        if not strs:
            return "y"

        words = "".join(strs)
        word_lengths = [str(len(word)) for word in strs]
        wl_str = ",".join(word_lengths)
        length = str(len(wl_str))


        return "".join([length, ":", wl_str, words])

    def decode(self, s: str) -> List[str]:
        if s=="x":
            return [""]
        elif s=="y":
            return []

        colon_place = s.find(":")
        word_count_length = int(s[:colon_place])

      
        word_counts = s[colon_place+1:colon_place+1+word_count_length]
        words = s[colon_place+1+word_count_length:]

        counts = word_counts.split(",")
        int_counts = [int(count) for count in counts]

        start = 0
        res=[]
        for count in int_counts:
            word = words[start:start+count]
            res.append(word)
            start = start + count

        return res
