class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = 0
        line = deque(senate)

        #print(line)
        #print(len(line)>R and len(line)>-R)
        while(len(line)>abs(R)):
            #print(line, R)
            front = line.popleft()
            if front == "R":
                if R>=0:
                    line.append(front)
                R+= 1
            else:
                if R<=0:
                    line.append(front)
                R-=1

        if line[0]=="R":
            return "Radiant"
        else:
            return "Dire"




        