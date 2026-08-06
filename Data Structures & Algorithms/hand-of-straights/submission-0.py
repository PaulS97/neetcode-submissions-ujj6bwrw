class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        store = {}
        for num in hand:
            store[num] = store.get(num, 0) + 1

        hand.sort()
        print(hand)

        for num in hand:
            if store[num]:
                for i in range(num, num+groupSize):
                    have = store.get(i, 0)
                    if have==0:
                        return False
                    else:
                        store[i] -= 1
                

        return True
        