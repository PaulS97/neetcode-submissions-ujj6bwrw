class Solution:
    def tribonacci(self, n: int) -> int:
        trib_store = {}
        trib_store[0] = 0
        trib_store[1] = 1
        trib_store[2] = 1

        def tribhelper(n):
            if n in trib_store:
                return trib_store[n]
            else:
                val = tribhelper(n-1) + tribhelper(n-2) + tribhelper(n-3)
                trib_store[n] = val
                return val

        return tribhelper(n)

        
        