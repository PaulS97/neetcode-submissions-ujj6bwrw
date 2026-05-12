class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        
        seen = []
        change = []
        original = image[sr][sc]
        if original == color:
            return image

        def dfs(r, c) -> bool:
            if min(r,c) < 0:
                return False
            if r >= len(image):
                return False
            if c >= len(image[0]):
                return False
            curr_color = image[r][c]
            if curr_color != original:
                return False
            image[r][c] = color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        dfs(sr, sc)
        return image

            


        