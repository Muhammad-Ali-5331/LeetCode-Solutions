class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        for i in range(num1,num2+1):
            num = str(i)
            if len(num)<3: continue
            for j in range(1,len(num)-1):
                total+= num[j-1]<num[j]>num[j+1]
                total+= num[j-1]>num[j]<num[j+1]
        return total