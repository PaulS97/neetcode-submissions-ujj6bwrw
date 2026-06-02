class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        storage = []

        for i, temp in enumerate(temperatures):
            if not storage:
                storage.append([temp, i, 1])
            else:
                top = storage[-1][0]
                if temp <= top:
                    storage.append([temp, i, 1])
                else:
                    days = 0
                    while(storage and top<temp):
                        days += storage[-1][2]
                        index = storage[-1][1]
                        result[index] = days
                        storage.pop()
                        if storage:
                            top = storage[-1][0]
                    if storage:
                        storage[-1][2] += days
                    storage.append([temp, i, 1])


        return result






        