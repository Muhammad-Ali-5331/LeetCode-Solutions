from typing import List
class Solution:
    def M(self,L,R,arr):
        if L<R:
            mid = (L+R)//2
            self.M(L,mid,arr)
            self.M(mid+1,R,arr)
            self.merge(L,R,mid,arr)
    def merge(self,l,r,mid,arr):
        Larr = arr[l:mid+1]
        Rarr = arr[mid+1:r+1]
        i,j,k = 0,0,l
        while i<len(Larr) and j<len(Rarr):
            if Larr[i]<=Rarr[j]:
                arr[k] = Larr[i]
                i+=1
            else:
                arr[k] = Rarr[j]
                j += 1
            k+=1
        while i<len(Larr):
            arr[k] = Larr[i]
            i += 1
            k+=1
        while j<len(Rarr):
            arr[k] = Rarr[j]
            j += 1
            k+=1
    def sortArray(self, nums: List[int]) -> List[int]:
        self.M(0,len(nums)-1,nums)
        return nums