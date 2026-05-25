class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 0
        seen = set()
        while j<len(nums):
            if j-i<=k:
                if nums[j] in seen: return True
                seen.add(nums[j])
                j+=1
            else:
                seen.discard(nums[i])
                i+=1
        return False