class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black = 0
        white = 0
        for i in range(0, k):
            if blocks[i] == "W":
                white += 1

        minwhite = white
        p1, p2 = 0, k
        res = white
        while p2<len(blocks):
            if blocks[p1] == "W":
                white -= 1
            if blocks[p2] == "W":
                white += 1
            minwhite = min(white, minwhite)
            p1+=1
            p2+=1

        return minwhite

            


        