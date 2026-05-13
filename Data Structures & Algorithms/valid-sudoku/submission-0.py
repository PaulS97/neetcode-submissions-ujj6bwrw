class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        good = range(10)
        def isValidNine(tocheck):
            counts = 9 * [0]
            for char in tocheck:
                if char == ".":
                    continue
                else:
                    val = int(char)-1
                    #print("char:", char, "int:", val)
                    counts[val] += 1
            for count in counts:
                if count>=2:
                    return False
            return True

        print("rows start")
        for i in range(9):
            if not isValidNine(board[i]):
                return False
        print("rows finish")
        print("columns start")
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
                if not isValidNine(column):
                    return False
        print("columns finish")

        def box_to_list(i,j):
            box_list = []
            for k in range(3):
                box_list += board[i+k][j:j+3]
            return box_list

        print("boxs start")

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                print(i, j)
                box_list = box_to_list(i, j)
                print(box_list)
                if not isValidNine(box_list):
                    return False
        print("boxs finish")


        return True

                
