class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        count = len(matrix) * len(matrix[0])

        res = []
        left = 0
        right = len(matrix[0])-1
        up = 0
        down = len(matrix)-1

        counter = 10
        #print(count, counter)
        while(count>0 and counter>0):
            #move right
           
           # print("count:", count)
            counter-=1
            for i in range(left, right + 1):
                res.append(matrix[up][i])
                count-=1
            up+=1
            #print("right", res)

            if count==0:
                break

            #move down
            for i in range(up, down+1):
                res.append(matrix[i][right])
                count -= 1
            right -= 1
            #print("down", res)

            if count==0:
                break

            #move left
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
                count -=1
            down -= 1
           # print("left:", res)

            if count==0:
                break

            # move up
            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
                count -= 1
            left += 1
            if count==0:
                break
           # print("up:", res)

        return res

        
        