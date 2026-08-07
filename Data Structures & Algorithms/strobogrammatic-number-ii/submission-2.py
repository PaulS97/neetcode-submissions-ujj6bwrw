class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        m = n//2
        curr = []
        res = []
        always = ["0","1","6","8","9"]
        mid = ["0","1","8"]
        start = ["1","6","8","9"]
        counter = {"0": "0", "1":"1", "8":"8", "6":"9", "9":"6"}


        def createstrobo(size, arr, n):
            if size==n:
                if arr[0]=="0" and size>1:
                    return
                else:
                    res.append("".join(arr))
            elif size==0 and n%2==1:
                for num in mid:
                    createstrobo(1, [num], n)
            else:
                for num in always:
                    createstrobo(size+2, [num]+arr+[counter[num]], n)

        createstrobo(0, [], n)

        return res
            




            


        