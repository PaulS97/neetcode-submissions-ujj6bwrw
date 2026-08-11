class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billDict = {}

        if bills[0] != 5:
            return False

        for bill in bills:
            print(bill, billDict)
            billDict[bill] = billDict.get(bill, 0) + 1
            if bill == 5:
                continue
            if bill == 10:
                if billDict[5]>0:
                    billDict[5] =  billDict[5]-1
                else:
                    return False
            if bill == 20:
                if (billDict[5]>0 and (10 in billDict and billDict[10]>0)):
                    billDict[5] =  billDict[5]-1
                    billDict[10] =  billDict[10]-1
                elif billDict[5]>2:
                    billDict[5] =  billDict[5]-3
                else:
                    return False

        return True
        