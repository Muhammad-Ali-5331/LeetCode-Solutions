class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        n = len(nums)
        even,odd = 0,0
        # Try to Make Even
        for i in range(n):
            if nums[i]%2==0: even+=1
            else:
                found = False
                for j in range(n):
                    if i == j: continue
                    if (nums[i]-nums[j])%2 == 0:
                        even+=1
                        found = True
                        break
                if not found: break
        # Try to Make Odd
        for i in range(n):
            if nums[i]%2!=0: odd+=1
            else:
                found = False
                for j in range(n):
                    if i == j: continue
                    if (nums[i]-nums[j])%2 != 0:
                        odd+=1
                        found = True
                        break
                if not found: break
        return even == n or odd == n