class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"

        conv = {"0": 0, "1": 1, "2": 2, "3": 3, "4":4, "5":5, 
        "6":6, "7": 7, "8": 8, "9": 9}

        revcon = ["0", "1", "2", "3", "4", "5", 
        "6", "7", "8", "9"]

        def strtoint(stringint) -> int:
            mult = 1
            total = 0
            for i in range(len(stringint)-1, -1, -1):
                total += conv[stringint[i]] * mult
                mult *= 10

            return total

        res = strtoint(num1) * strtoint(num2)
        resstring = []

        while(res>0):
            val = res % 10
            resstring.append(revcon[val])
            res //=10

        return "".join(resstring[::-1])


