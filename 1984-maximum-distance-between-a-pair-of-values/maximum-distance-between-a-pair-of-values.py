class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        L = len(nums1)
        def BS(target):
            l = 0
            r = len(nums2)-1
            while l<=r:
                mid = (l+r)//2
                if nums2[mid]>=target:
                    l = mid + 1
                else: r = mid-1
            return l
        mx = 0
        for i in range(L):
            nxtInd = BS(nums1[i])-1
            if i<=nxtInd and nums1[i]<=nums2[nxtInd]:
                mx = max(nxtInd-i,mx)
        return mx