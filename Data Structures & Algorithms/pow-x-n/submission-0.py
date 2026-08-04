class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = n<0
        m = abs(n)

        store = {}

        def helper(x, m)->float:
            if m in store:
                return store[m]
            if m==0:
                return 1
            if m==1:
                return x
            

            half = m//2
            other = m-half
            prod = helper(x, half) * helper(x, other)
            store[m] = prod

            return prod

        val = helper(x,m)
        if negative:
            val = 1/val
        return val