class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        front, back = 0, len(people)-1
        people.sort()
        boats = 0

        while(front<=back):

            if people[front] + people[back] <= limit:
                front += 1
                back -= 1
                boats += 1
            else:
                back -= 1
                boats += 1

        return boats

        