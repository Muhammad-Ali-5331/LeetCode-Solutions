class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n,miElement,mxElement = len(nums),min(nums),max(nums)
        miIndex,mxIndex = nums.index(miElement)+1,nums.index(mxElement)+1 # Added 1 for 1 based indexing
        if mxIndex < miIndex: # Larger Element is before smaller Element
            leftD = miIndex # not subtracting 1 because mxElem gets deleted in it
            rightD = n-miIndex+1
            deletingmX = min(mxIndex,miIndex - mxIndex)
            return min(leftD, rightD + deletingmX)
        elif miIndex <= mxIndex: # Smaller Element is before larger element or Smaller = larger
            leftD = mxIndex # not subtracting 1 because miElem gets deleted in it
            rightD = n-mxIndex+1
            deletingmX = min(miIndex,mxIndex - miIndex)
            return min(leftD, rightD + deletingmX)