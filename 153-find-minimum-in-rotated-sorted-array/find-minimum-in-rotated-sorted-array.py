class Solution:
    def findMin(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        minE = float("inf")
        while l<=r:
            mid = (l+r)//2
            if arr[mid]>arr[r]: 
                l = mid+1
            else:
                minE = min(minE,arr[mid])
                r = mid-1
        return minE