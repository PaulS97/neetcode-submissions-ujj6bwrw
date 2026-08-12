class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        arr = []
        negatives = []

        for asteroid in asteroids:
            if asteroid>0:
                arr.append(asteroid)
            else:
                destroyed = False
                while(arr):
                    if arr[-1] > abs(asteroid):
                        destroyed = True
                        break
                    elif arr[-1] == abs(asteroid):
                        destroyed = True
                        arr.pop()
                        break
                    else:
                        arr.pop()
                if not destroyed:
                    negatives.append(asteroid)

        return negatives + arr
            
        