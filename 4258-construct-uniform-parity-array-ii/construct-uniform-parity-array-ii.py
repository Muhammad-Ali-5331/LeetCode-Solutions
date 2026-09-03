class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        n = len(nums)
        even,odd = 0,0
        foundOdd,foundEven = False,False
        minEven,minOdd = float("inf"),float("inf")
        for i in range(n):
            if nums[i]%2 == 0:
                foundEven = True
                minEven = min(minEven,nums[i])
            else:
                foundOdd = True
                minOdd = min(minOdd,nums[i])
        if not foundEven or not foundOdd: return True
        
        # -- Even Parity -- #
        for i in range(n):
            if nums[i]%2 == 0: even+=1
            elif minOdd == nums[i]: break
            else: even+=1
        
        # -- Odd Parity -- #
        for i in range(n):
            if nums[i]%2 != 0: odd+=1
            elif nums[i]-minOdd>=1: odd+=1
            else: break
        return odd == n or even == n