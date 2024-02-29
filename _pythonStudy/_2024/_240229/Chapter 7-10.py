class Calculator:
    def __init__(self,num):
        self.num = num

    def sum(self):
        res = 0
        for i in self.num:
            res += i
        return res
    
    def avg(self):
        hap = self.sum()
        # res = 0
        # for i in self.num:
        #     res += i
        # return res / len(self.num)
        return hap / len(self.num)
    
cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg()) 