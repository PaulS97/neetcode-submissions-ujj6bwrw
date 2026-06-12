class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(position)):
            time_left = (target - position[i]) / speed[i]
            pos_speed.append((position[i], speed[i], time_left))

        pos_speed.sort(reverse = True)


        #print("pos_speed:", pos_speed)
        fleets = []

        for item in pos_speed:
            if not fleets:
                fleets.append(item)
            else:
                if fleets[-1][2] < item[2]:
                    fleets.append(item)

            

        return len(fleets)




        